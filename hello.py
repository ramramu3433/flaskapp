from flask import Flask,render_template
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

app=Flask(__name__,template_folder=BASE_DIR+"/templates")

@app.route('/')
def hello():
   return("hello world")

@app.route('/hello/<user>')
def name(user):
    return  render_template('name.html',name=user)
       

if(__name__=="__main__"):
  app.run(host='0.0.0.0',port='5000')

