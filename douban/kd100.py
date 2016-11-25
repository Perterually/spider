import json
import hashlib
import sys

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from base64 import standard_b64encode as base64

APP_ID = "1266271"
APP_KEY = "7526a46e-3a2a-4f5b-8659-d72f361e3386"


def sign(data):
    orig = data["RequestData"]
    orig += APP_KEY
    md5 = hashlib.md5()
    md5.update(orig.encode("utf-8"))
    data["DataSign"] = base64(md5.hexdigest().encode("utf-8")).decode("utf-8")
    return urlencode(data).encode("utf-8")


def api_res_handler(f):
    def wrapper(data, *args, **kwargs):
        try:
            req = Request(
                "http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx",
                method="POST",
                data=data
            )
            res = json.loads(urlopen(req).read().decode("utf-8", "ignore"))
            if res["Success"]:
                return f(res, *args, **kwargs)
            elif "Reason" in res:
                raise Exception(res["Reason"])
            else:
                raise Exception("未知错误，可能是快递单号未知")
        except json.JSONDecodeError:
            print("API Server 未返回正确数据，请检查网络环境是否正常")
            sys.exit(1)
        except BaseException as e:
            print(str(e))
            sys.exit(1)
    return wrapper


def api(request_type, **request_data_scheme):
    def wrappers_wrapper(f):
        def wrapper(**kwargs):
            request_data = {}
            for k, v in request_data_scheme.items():
                request_data[k] = v.format(**kwargs)
            data = sign({
                "RequestData": json.dumps(request_data),
                "EBusinessID": APP_ID,
                "RequestType": request_type,
                "DataType": "2",
            })
            return api_res_handler(f)(data)
        return wrapper
    return wrappers_wrapper


@api("2002", LogisticCode="{code}")
def recognise_shipper(res):
    for shipper in res["Shippers"]:
        yield shipper["ShipperCode"], shipper["ShipperName"]


@api("1002", LogisticCode="{code}", ShipperCode="{shipper}")
def query(res):
    for trace in res["Traces"]:
        yield trace["AcceptTime"], trace["AcceptStation"], \
              trace["Remark"] if "Remark" in trace else ""

if __name__ == "__main__":
    logistic_code = input("Input your logistic code: ")
    for shipper_code, shipper_name in recognise_shipper(code=logistic_code):
        print("尝试查询", shipper_code, shipper_name)
        for time, desc, remark in query(code=logistic_code, shipper=shipper_code):
            print(time, desc, remark)