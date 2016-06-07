# -*- coding:utf-8 -*-
from openpyxl import Workbook

import process_data
import read_data


class Main():
    def __init__(self):
        self.list = []
        self.dict = {}
        self.process_data = process_data.Process()
        self.readdata = read_data.ReadData()
        self.wb = Workbook()
        self.ws = self.wb.active
        self.data = []

    # 循环所有数据把所有的
    def cycle(self, row):
        for i in range(1, row + 1):
            print i
            length = self.readdata.get_date_len(i)
            self.list.append([i, length])

    def get_maxlen(self):
        # 查询数据库得出最大的数据条数
        row = self.readdata.get_count()

        self.cycle(row)
        # 循环list给dict赋值
        for i in self.list:
            self.dict[i[0]] = i[1]
        # 值最大的dict
        ma = max(self.dict.items(), key=lambda x: x[1])
        return ma

    def get_excle_list(self, row):
        # row = 6
        max_row = (7825, 35)
        b = max_row[0]
        li5 = []
        # 获取指定行数的数据
        data = self.readdata.get_date(row)
        # 把数据转成dict
        dafter = self.process_data.return_dict(data)
        # 获取最长字段的数据
        datas = self.readdata.get_date(b)
        # 把获取指定字段的数据转成dict
        dafters = self.process_data.return_dict(datas)
        # 获取最长的字段
        field = self.process_data.return_list(dafters)
        # 循环最长的数据的字段
        for s in field:
            # 循环判断字段是否在最长字段里如果没有赋值为0并返回一个dict
            if s not in dafter:
                li5.append('')
            elif s in dafter:
                li5.append(dafter[s])
        date = li5
        return date

    def get_item(self):
        datas = self.readdata.get_date(7825)
        dafters = self.process_data.return_dict(datas)
        field = self.process_data.return_list(dafters)
        self.data.append(field)

    def main(self):
        count = self.readdata.get_count()
        self.get_item()
        for i in xrange(1, count):
            data = self.get_excle_list(i)
            self.data.append(data)
            print i
        for row in self.data:
            self.ws.append(row)
        self.wb.save('demo.xlsx')
        print u'保存完成'


if __name__ == "__main__":
    main = Main()
    main.main()
