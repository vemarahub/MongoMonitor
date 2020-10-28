# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import db_details


app=Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def server():
    final_list=[]
    tot_size=""
    instance=""
    
    if request.method == 'POST':
        # Then get the data from the form
        url = request.form['mongourl']
        
        hostname = request.form['hostname']
        username = request.form['username']
        password = request.form['password']
        port = request.form['port']
       
        if(url==""):
            url = "mongodb://"+username+":"+password+"@"+hostname+":"+port+"/admin?retryWrites=true&w=majority"
       
        final_list,tot_size,instance,version,uptime,hosts,primary,conn=db_details.db_info(url)
        
        if(instance==""):
            return render_template("error.html")
        else:
            return render_template("home.html",instance=instance,final_list=final_list,tot_size=tot_size,version=version,uptime=uptime,hosts=hosts,primary=primary,conn=conn)
      

    else:   
        return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True) 

