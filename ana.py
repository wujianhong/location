#!/usr/bin/env python
#conding: uft-8
import csv
with open("location1.log", "r") as f:
    lines = f.readlines()

user_dict = {}


for line in lines:
    tmp = line.split(",")
    id = tmp[0]
    if len(tmp) >= 2 :
        ip = tmp[1]
    else:
        print(tmp, end=" . ")
        ip = ""
    if len(tmp) == 3 :
        location = tmp[2]
    else:
        print(tmp)
        location = ""
    if user_dict.get(str(id), None):
        pass
    else:
        user_dict.setdefault(str(id),True)
        with open("location.csv", "a", encoding="utf-8") as f:
            f.write(",".join([id, ip, location]))
