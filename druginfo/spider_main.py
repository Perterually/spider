# -*- coding:utf-8 -*-
import random

from time import sleep

import data_save
import date_list
import drug_list
import durg_info_detail


class Drug():
    def __init__(self):
        self.enable = True
        self.durglist = drug_list.DrugList()
        self.datelist = date_list.DataJson()
        self.datasave = data_save.Date()
        self.durginfodetail = durg_info_detail.Detail()
        self.prim = []

    def craw(self):
        paper = 1
        while self.enable:
            print u'已经传递到的页数是%d' % paper
            # 获取一页的数据
            data = self.durglist.get_paper_data(paper)

            # 获取一页的药品id
            drupid = self.datelist.get_id(data)
            for id in drupid:
                self.prim.append(id)
                # 根据药品id获取所有的厂家的json
                jsonlist = self.durglist.get_drup_data(id)

                durg_info = self.datelist.get_into(jsonlist, id)

                self.datasave.save_info(durg_info)
                # 获取所有药品的制造id
                drugid = self.datelist.get_drug_id(jsonlist)
                for i in drugid:
                    # 返回详细信息页面
                    try:
                        content = self.durglist.get_drup_detail(i[0], i[1])
                        # 返回使用说明list加主id
                        use = self.durginfodetail.get_drug_dict(content)

                        # 返回用药指导list
                        guide = self.durginfodetail.get_drug_use_dict(content)
                    except:
                        print u'出现错误'
                    # 保存使用说明
                    self.datasave.save_use(id, i[0], use)
                    # #保存用药指导
                    self.datasave.save_use_guide(id, i[0], guide)
                    sleep(random.uniform(0.5, 1))
            sleep(random.uniform(0.5, 1))
            paper += 1
            print '已经保存到第%d页' % paper


if __name__ == "__main__":
    drug = Drug()
    drug.craw()
