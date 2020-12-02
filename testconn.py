# -*- coding: utf-8 -*-
import pymongo
import getReplicationInfo
#import pyautogui

def switch_repl(argument):
    switcher = {
        1: "Primary",
        2: "Secondary",
        3: "Recovering",
        6: "Unkown",
        8: "Down",
        9: "RollBack",
        10: "Removed"       
    }
    print(switcher.get(argument))

#client = pymongo.MongoClient("mongodb+srv://m001-student:vemara@sandbox.m8irx.mongodb.net/sandbox?retryWrites=true&w=majority") # defaults to port 27017
sum = 0

#client = pymongo.MongoClient("mongodb://test:test@localhost:27000/admin?retryWrites=true&w=majority") # defaults to port 27017

client = pymongo.MongoClient("mongodb://root:root@osboxes:27007/admin?retryWrites=true&w=majority") # defaults to port 27017

#abc = client["admin"].command({"getLog":'global'})
#print(client["admin"].command({"getLog":'global'})["log"])

abc = client["admin"].command({"replSetGetStatus": 1})["members"]
i=0
for ab in abc:
    print(ab["name"])
    switch_repl(ab["state"])
   
    
    

df = client["admin"].command({"replSetGetStatus": 1})["members"][1]["optimeDate"]
#print("logsizemb: " + str(getReplicationInfo.logsizemb(client)))
#print("usedmb: " + str(getReplicationInfo.usedmb(client)))
#print("tfirst: " + str(getReplicationInfo.tfirst(client)))
#print("tlast: " + str(getReplicationInfo.tlast(client)))
#print("timediff: " + str(getReplicationInfo.timediff(client)))

print(abc)

