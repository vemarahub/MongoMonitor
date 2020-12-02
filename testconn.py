# -*- coding: utf-8 -*-
import pymongo
import getReplicationInfo
#import pyautogui


#client = pymongo.MongoClient("mongodb+srv://m001-student:vemara@sandbox.m8irx.mongodb.net/sandbox?retryWrites=true&w=majority") # defaults to port 27017
sum = 0

#client = pymongo.MongoClient("mongodb://test:test@localhost:27000/admin?retryWrites=true&w=majority") # defaults to port 27017

client = pymongo.MongoClient("mongodb://root:root@osboxes:27007/admin?retryWrites=true&w=majority") # defaults to port 27017

#abc = client["admin"].command({"getLog":'global'})
#print(client["admin"].command({"getLog":'global'})["log"])

abc = client["admin"].command({"replSetGetStatus": 1})
#print("logsizemb: " + str(getReplicationInfo.logsizemb(client)))
#print("usedmb: " + str(getReplicationInfo.usedmb(client)))
#print("tfirst: " + str(getReplicationInfo.tfirst(client)))
#print("tlast: " + str(getReplicationInfo.tlast(client)))
#print("timediff: " + str(getReplicationInfo.timediff(client)))

print(abc)
