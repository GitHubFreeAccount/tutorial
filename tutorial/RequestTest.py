# -*- coding: utf-8 -*-
import requests

# r=requests.get("https://api.github.com/events")
# print r.text
# print r.json()
# print r.content
# rpost=requests.post("http://httpbin.org/post",data={'key':'value'})

r=requests.get("http://api.bojuecar.com/api/system/sleepContact")
headers={'Content-type':'application/x-www-form-urlencoded','Content-Length':''}
