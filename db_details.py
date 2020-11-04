# -*- coding: utf-8 -*-
from pymongo import MongoClient


def db_info(url):
   
    final_list=[]
    ops_list=[]
    user_list=[]
    tot_size=""
    instance=""
    version=""
    uptime=""
    hosts=""
    primary=""
    conn=""
    
    
    db_list=["DB NAME"]
    col_count=["COLL COUNT"]
    db_size=[]
    db_size.append(0)
    idx_count=["INDEX COUNT"]
    doc_count=["DOC COUNT"]
    col_list=["COLLECTIONS"]
    
    op_ops=["OPERATION"]
    op_commands=["COMMAND"]
    op_nss=["NAMESPACE"]
    op_currentOpTimes=["CURRENT OP TIME"]
    op_secrunnings=["SECS RUNNING"]
    
    #client = MongoClient("mongodb+srv://m001-student:vemara@sandbox.m8irx.mongodb.net/sandbox?retryWrites=true&w=majority") # defaults to port 27017
    try:
        client = MongoClient(url,serverSelectionTimeoutMS = 50000)
        client.server_info()
        
        with client.admin.aggregate([{"$currentOp": {}}]) as cursor:
            for operation in cursor:
                if "$currentOp" in str(operation["command"]):
                    continue
                else:    
                    op_ops.append(operation["op"])
                    op_commands.append(operation["command"])
                    op_nss.append(operation["ns"])
                    op_currentOpTimes.append(operation["currentOpTime"])            
                    op_secrunnings.append(operation["secs_running"])
        
    except:
        return final_list,tot_size,instance,version,uptime,hosts,primary,conn,user_list,ops_list
            
  
    
    instance=client["admin"].command("serverStatus")["host"]
    version=client["admin"].command("serverStatus")["version"]
    conn = client["admin"].command("serverStatus")["connections"]
    uptime = round(client["admin"].command("serverStatus")["uptime"] / 86400)
    user_list = client["admin"].system.users.find({},{"_id":0,"user":1,"db":1,"roles":1})
    try:
        primary = client["admin"].command("serverStatus")["repl"]["primary"]
        hosts =  client["admin"].command("serverStatus")["repl"]["hosts"]
    except KeyError:
        primary=""
        hosts=""
    
    final_list=[]

    for db in client.list_databases():
        db_list.append(db["name"])
        db_size.append(round(db["sizeOnDisk"]/1024/1024/1024,2))
             
        col_count.append(client[db["name"]].command("dbstats")["collections"])
        idx_count.append(client[db["name"]].command("dbstats")["indexes"])
        doc_count.append(client[db["name"]].command("dbstats")["objects"]) 
        col_list.append(list(client[db["name"]].list_collection_names()))
        
    
    

    tot_size= (sum(db_size)) 
    db_size[0]="DB SIZE (GB)"
    final_list.append(db_list)
    final_list.append(db_size)
    final_list.append(col_count)
    final_list.append(idx_count)
    final_list.append(doc_count)
    final_list.append(col_list)

    ops_list.append(op_ops)
    ops_list.append(op_commands)
    ops_list.append(op_nss)
    ops_list.append(op_currentOpTimes)
    ops_list.append(op_secrunnings)
    return final_list,tot_size,instance,version,uptime,hosts,primary,conn,user_list,ops_list

