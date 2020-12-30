# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import os
#import scrapy
import requests
from fake_useragent import UserAgent
from urllib.request import urlretrieve


class MyspiderPipeline:
    def process_item(self, item, spider):
        
        wenjian_path = r"E:\monalisa"
        if not os.path.exists(wenjian_path):
            os.mkdir(wenjian_path)
        
        os.chdir(wenjian_path)
        
        #保存文本数据
        txtpath = r"E:\monalisa\monalisatxt.txt"
        with open(txtpath,'a') as f:
            f.write(str(item) + '\n\n')
        print(str(item) + '\n\n')
        
        #保存图片
        # picresult = requests.get(item["pic_href1"]
        #                          ,headers = {"User-Agent":UserAgent().random}
        #                          )
        # with open(item["name"] + ".jpg","wb") as f:
        #     f.write(picresult.content)
        
        #保存图片
        urlretrieve(item["pic_href1"],item["name"] + "_1.jpg")
        urlretrieve(item["pic_href2"],item["name"] + "_2.jpg")

        return item
    
