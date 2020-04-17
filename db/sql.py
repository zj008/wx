import pymysql
import os
from configparser import ConfigParser
import logging

path = os.getcwd()
print(path, path.split("wx")[0])
path = os.path.join(path.split("wx")[0], "wx/conf/conf")
print(path)
cf = ConfigParser()
cf.read(path)


class Sql(object):
    def __init__(self):
        self.db = pymysql.connect(
            host=cf.get("sql", "host"),
            port=int(cf.get("sql", "port")),
            user=cf.get("sql", "username"),
            password=cf.get("sql", "password"),
            database=cf.get("sql", "database")
        )
        self.cursor = self.db.cursor()

    def insert_or_update(self, data):
        if self.isExists(data):
            print("exists")
            self.update(data)
            return
        table = data.pop("table")
        key = ", ".join(data.keys())
        val = ", ".join(["%s"] * len(data.keys()))
        t_val = tuple(list(data.values()))
        sql = "insert into %s (%s) values (%s)" % (table, key, val)
        print(sql)
        try:
            self.cursor.execute(sql, t_val)
            self.db.commit()
        except Exception as e:
            logging.error(e)
            return None
        return True

    def update(self, data):
        table = data.pop("table")
        for k,v in data.items():
            sql = "update %s set %s = %s where id = %s" % (table, k, "%s", data.get("id"))
            try:
                self.cursor.execute(sql, (v,))
                self.db.commit()
            except Exception as e:
                logging.error(e)
                return
        return True

    def isExists(self, data):
        sql = "select id from %s where id = %s" % (data.get("table"), data.get("id"))
        try:
            self.cursor.execute(sql)
            ret = self.cursor.fetchall()
        except Exception as e:
            logging.error(e)
            return None
        return ret

    def close(self):
        self.db.close()
        self.cursor.close()

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            return False
        return True


if __name__ == '__main__':
    pass