# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class DoubanPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        user = settings["MONGODB_USER"]
        psw = settings["MONGODB_PSW"]
        #创建数据库链接
        self.client = pymongo.MongoClient(host = host,port = port)
        self.client.admin.authenticate(user,psw)

        #指定数据库
        self.mydb = self.client[dbname]
        #存放数据库表名称
        self.post = self.mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
