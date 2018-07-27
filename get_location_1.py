#!/usr/bin/env python
#conding: uft-8
import re
import time

import pymysql
import requests
import threadpool

result = []
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
                resp =  str(id)+','+ ip + ','+ data["data"][0]["location"]
                result.append(resp)

    except Exception as ex:
        resp = str(id)+','+ ip
        result.append(resp)

if __name__ == '__main__':
    user_set = get_user()
    pool = threadpool.ThreadPool(3)
    req = threadpool.makeRequests(get_location, user_set)
    request_list = []
    for device in user_set:
        request_list.append(threadpool.makeRequests(get_location, device))
    map(pool.putRequest,request_list)
    pool.poll()
    print(result)
