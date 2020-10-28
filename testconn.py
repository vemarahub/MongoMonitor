# -*- coding: utf-8 -*-
import pymongo
import pyautogui


#client = pymongo.MongoClient("mongodb+srv://m001-student:vemara@sandbox.m8irx.mongodb.net/sandbox?retryWrites=true&w=majority") # defaults to port 27017
sum = 0

client = pymongo.MongoClient("mongodb://test:test@localhost:27000/admin?retryWrites=true&w=majority") # defaults to port 27017
try:
    result = client["admin"].system.users.find({},{"_id":0,"user":1,"db":1,"roles":1})
    for res in result:
        print(res)
except KeyError:
    result=""
        
print(result)

"""
for db in client.list_databases():
    #Total Size on Disk
    sum = sum + round(db["sizeOnDisk"]/1024/1024/1024,2)
   
    print()
    
    #Database List
    print(db["name"]," ",round(db["sizeOnDisk"]/1024/102:4/1024,2),"GB")
    
    #Collections in each DB
    print("No Of Collections :",client[db["name"]].command("dbstats")["collections"])
    print("No Of Indexes :",client[db["name"]].command("dbstats")["indexes"])
    print("No Of Documents in DB :",client[db["name"]].command("dbstats")["objects"])
    print()
    print("Collections :",list(client[db["name"]].list_collection_names()))
   
    #for col in client[db["name"]].list_collection_names():
        #print(col)
     
print()  
print("-----------------------------------------")   
print("Total Size on Disk for all DBs : ",sum,"GB") 
 

# print the number of documents in a collection





#print(db.sales.count_documents({"customer":{"$exists": "false"}}))

#returnList = db.sales.find({"customer":{"$exists": "false"}})
#print(returnList[0])
"""
