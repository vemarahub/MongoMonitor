# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect,url_for
import db_details


app=Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def server():
   
    
    if request.method == 'POST':
        # Then get the data from the form
    
      url = request.form['mongourl']
        
      hostname = request.form['hostname']
      username = request.form['username']
      password = request.form['password']
      port = request.form['port']
       
      if(url==""):
          url = "mongodb://"+username+":"+password+"@"+hostname+":"+port+"/admin?retryWrites=true&w=majority"
       
      
      return redirect(url_for('home', url=url))

    else:   
        return render_template('index.html')

@app.route('/home')
def home():
    final_list=[]
    tot_size=""
    instance=""
    
    url = request.args['url']
    
    final_list,tot_size,instance,version,uptime,hosts,primary,conn,user_list=db_details.db_info(url)
       
    if(instance==""):
        return render_template("error.html")
    else:
        return render_template("home.html",instance=instance,final_list=final_list,tot_size=tot_size,version=version,uptime=uptime,hosts=hosts,primary=primary,conn=conn,user_list=user_list)
      
     

if __name__ =='__main__':
    app.run(debug=True) 

