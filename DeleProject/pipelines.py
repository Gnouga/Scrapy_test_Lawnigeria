# -*- coding: utf-8 -*-

import psycopg2

class DeleprojectPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='0000',
            dbname='postgres'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS testDele""")
        self.curr.execute("""CREATE TABLE testDele(
                                content text,
                                url text
                                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into testDele(content,url) values(%s,%s)""",
                             (item['content'], item['url']))
        self.conn.commit()

