#!/usr/bin/env python
#conding: uft-8
xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
id = '44512119940322031'
s = 0

for idx, tmp in enumerate(id):
    print(tmp)
    s = s + int(tmp) * xishu[idx]
print(s)
print(s%11)
