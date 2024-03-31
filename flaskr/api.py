#!/usr/bin/python3

import requests
import json

def get_address(zipcode):
    r = requests.get(" https://zipcloud.ibsnet.co.jp/api/search?zipcode={}".format(zipcode))
    j = json.loads(r.text)
    if j["status"] != 200:
        return "error"
    elif j["results"] == None:
        return "error"
    else:
        return j["results"][0]["address1"] + j["results"][0]["address2"] + j["results"][0]["address3"]
