# -*- coding:utf-8 -*-

class Process():
    # 返回dict的方法
    def return_dict(self, data):
        li = []
        for i, key in data.items():
            li.append([i.encode('utf-8'), key.encode('utf-8')])
        da = dict(li)
        return da

    # 返回list
    def return_list(self, data):
        li = []
        for i in data:
            li.append(i)
        return li
