# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class XicidailiSpiderPipeline(object):
    def process_item(self, item, spider):
        config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'root',
          'db':'scraping',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor
          }
        # Connect to the database
        conn = pymysql.connect(**config)
        #conn = pymysql.connect(host='localhost:3306', unix_socket='/tmp/mysql.sock', user='root', passwd='root', db='scraping', charset='utf8')
        cur = conn.cursor()
        #插入语句
        insert_sql = (
            "insert into t_proxy (ip, port, position, anonymous, type, speed, connect_time, last_check_time) "
            "values (%s,%s,%s,%s,%s,%s,%s,%s);"
        )
        insert_values = (item['ip'], item['port'], item['position'], item['anonymous'], item['type'], item['speed'], item['connect_time'], item['last_check_time'])
        #修改语句
        update_sql = (
            "update t_proxy set ip=%s, port=%s, position=%s, anonymous=%s, type=%s, speed=%s, connect_time=%s, last_check_time=%s where id=%s"
        )
        
        #查询语句
        select_sql = ("select * from t_proxy where ip=%s and port=%s");
        select_values = (item['ip'], item['port'])
        try:
            cur.execute(select_sql, select_values)
            cur.fetchall()
            print('------rowcount------'+cur.rowcount)
            if cur.rowcount >= 1 :
                update_value = (item['ip'], item['port'], item['position'], item['anonymous'], item['type'], item['speed'], item['connect_time'], item['last_check_time'], cur[0][0])
                cur.execute(update_sql, update_value)
            else:
                cur.execute(insert_sql, insert_values)
        except Exception(e):
            print("插入失败: " + e)
            conn.rollback()
        else:
            conn.commit()
        cur.close()
        conn.close()
        return item