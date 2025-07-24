import array as ar

var = ar.array('i', [1,2,3,4,5])
print(var)


import random
print(random.randint(1,898989))
print(random.choice(['efwf0','f3ef']))


import os 
print(os.getcwd())
#os.mkdir("test1.py")

import shutil
#shutil.copyfile('Lists.py', 'destination.py')



import json 
data = {'name': "aryan", 'age':25}
#converting this dict into a json that is by default in str form
str_json = json.dumps(data)
print(str_json)
print(type(json.dumps(data)))

#converting bsck the str_json into the data it was before
data_parsed = json.loads(str_json)
print(data_parsed)
print(type(data_parsed))


# write and read files
import csv 

with open ('example.csv', mode = 'w', newline='') as file:

    write = csv.writer(file)
    write.writerow(["name", "age"])
    write.writerow(["aryan", 21])

with open ('example.csv', mode='r') as file:

    read = csv.reader(file)
    for row in read:
        print(row)


import datetime as dt

from datetime import datetime, timedelta

now = datetime.now()
print(now)

yesterday = now - timedelta(days = 1)
print(yesterday)


import time as tt
print(tt.time())
tt.sleep(1)
print("after sleep time",tt.time())

#regular expresiion 

import re

pattern=r'\d+'
text = " hwloo 123 love"
match = re.search(pattern, text)
print(match.group())