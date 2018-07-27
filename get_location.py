#!/usr/bin/env python
#conding: uft-8
import requests
import pymysql
import re
def get_user():
    user_set = []
    db = pymysql.connect(host="localhost", user="root", password="123456", db="acfun", port=3306,
                                   charset='utf8')
    with db.cursor() as cursor:
        sql = "select id, last_login_ip from user_bak"
        cursor.execute(sql)
        fech = cursor.fetchall()
        for row in fech:
            # print(row[0])
            user_set.append([row[0], row[1].replace("*", "0")])

    return user_set
import json
def get_location(id, ip):
    time.sleep(0.01)
    try:
        url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={0}&co=&resource_id=6006&t=1531980541404&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110202514727592969903_1531980329838&_=1531980329847".format(ip)
        res = requests.get(url)
        # print(res.text)
        pattern = re.compile(r'\{.*\}')
        result = pattern.findall(res.text)
        # print("result: ", result)
        # print(id)
        if len(result) > 0:
            data = json.loads(result[0])
            # print(data)
            if data["status"] == "0":
                line =  str(id)+','+ ip + ','+ data["data"][0]["location"]
                with open("location.txt", "a") as f:
                    f.write(line)
                    f.write("\n")
                return line

    except Exception as ex:
        return str(id)+','+ ip
from datetime import datetime
import jian
import time
from concurrent.futures import ThreadPoolExecutor
if __name__ == '__main__':
    user_set = get_user()
    thread_list = []
    with ThreadPoolExecutor(2) as executor:
        for idx, tmp in enumerate(user_set):
            if idx % 1000 == 0:
                print(idx)
            future = executor.submit(get_location, tmp[0], tmp[1])
            thread_list.append(future)
    r_l = []
    for tmp in thread_list:
        r_l.append(tmp.result())
    # for tmp in r_l:
