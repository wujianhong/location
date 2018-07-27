#!/usr/bin/env python
#conding: uft-8
import requests
import pymysql
import json
import re
from logging.handlers import RotatingFileHandler
import time
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
fh = RotatingFileHandler("/usr/local/workspace/git/location/location.log", mode='a', maxBytes=1024*1024*50, backupCount=10)
fh.setLevel(logging.DEBUG)
formatter1 = logging.Formatter("%(asctime)s - [line:%(lineno)d] : %(message)s")
formatter = logging.Formatter("%(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
class Location():
    db = pymysql.connect(host="localhost", user="root", password="123456", db="acfun", port=3306,
                                       charset='utf8')
    def get_user(self):
        user_set = []
        with self.db.cursor() as cursor:
            sql = "select id, last_login_ip from user_bak where id > 65885"
            cursor.execute(sql)
            fech = cursor.fetchall()
            for row in fech:
                # print(row[0])
                user_set.append([row[0], row[1].replace("*", "0")])
    
        return user_set
    def get_location(self, id, ip):
        try:
            url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={0}&co=&resource_id=6006&t=1531980541404&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110202514727592969903_1531980329838&_=1531980329847".format(ip)
            res = requests.get(url)
            # print(res.text)
            pattern = re.compile(r'\{.*\}')
            result = pattern.findall(res.text)
            # print("result: ", result)
            if len(result) > 0:
                data = json.loads(result[0])
                # print(data)
                if data["status"] == "0":
                    cmd = "update user_bak set city='{0}' where id={1} ;".format(data["data"][0]["location"], id)
                    # print(cmd)
                    #with self.db.cursor() as cursor:
                    #    cursor.execute(cmd)
                    #    self.db.commit()
                    print(data["data"][0]["location"])
                    return str(id)+','+ ip + ','+ data["data"][0]["location"]
                    
        except Exception as ex:
            print(ex)
            return str(id)+','+ ip

from concurrent.futures import ThreadPoolExecutor
if __name__ == '__main__':
    L = Location()
    user_set = L.get_user()
    thread_list = []
    print("==================START======================")

    for row in user_set:
        line = L.get_location(row[0], row[1])
        logger.info(line)
##    with ThreadPoolExecutor(3) as executor:
 #       for idx, tmp in enumerate(user_set):
 #           future = executor.submit(L.get_location, tmp[0], tmp[1])
 #           thread_list.append(future)
 #           if idx % 1000 == 0:
 #               print(idx)
#
#    r_l = []
#    for tmp in thread_list:
#        r_l.append(tmp.result())
#    with open("location1.txt", "w") as f:
#        f.write("\n".join(r_l))

