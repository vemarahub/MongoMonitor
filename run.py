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
        hostname = request.form['hostname']
        username = request.form['username']
        password = request.form['password']
        port = request.form['port']
       
      
        url = "mongodb://"+username+":"+password+"@"+hostname+":"+port+"/admin?retryWrites=true&w=majority"
        final_list,tot_size,instance=db_details.db_info(url,hostname,port)
        print("The URL",url)
        return home(final_list,tot_size,instance)
      

    else:   
        return render_template('login.html')


#@app.route('/home') 
def home(final_list,tot_size,instance):
  #  final_list,tot_size,instance=db_details.db_info()
    return render_template("home.html",instance=instance,final_list=final_list,tot_size=tot_size)

if __name__ =='__main__':
    app.run(debug=True) 

