from db.sql import Sql
import json

def get_info(path):
    with open(path) as f:
        for i in f:
            yield i



if __name__ == '__main__':
    ret = get_info("/Users/aibyte/Documents/code/python/wx/info/media.txt")
    for d in ret:
        data = json.loads(d)
        data = json.loads(data)
        del data["item"]
        data["table"] = "media"
        sql = Sql()
        sql.save(data)
        sql.close()