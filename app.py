import mysql.connector
from flask import Flask,  request
from flask_cors import CORS
import json
from werkzeug.serving import make_server
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/order_vehicle',methods = ['POST'])
def order_vehicle():
   try:
      data = request.json
      person_name = str(data["person_name"])
      model = str(data["model"])
      trim = str(data["trim"])
      mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="car_registration")
      
      mycursor = mydb.cursor()
      sql = ("INSERT INTO ordered_cars (user_name, model, trim) VALUES (%s, %s, %s)")
      val = (person_name, model, trim)
      print(type(val))
      mycursor.execute(sql, val)
      mydb.commit()
      return {"status_code" : 200}
   except Exception as e:
      return {"error" : e, "status_code":500}

@app.post('/shutdown')
def shutdown():
   data = request.json
   password = str(data["password"])
   
   if password == "harshal":
      print("shutting down")
      shutdown_server()
      return " stopped"
   else :
      print("wrong password")
      return "password is not correct"

def shutdown_server():
   func = request.environ.get('werkzeug.server.shutdown')
   if func is None:
      raise RuntimeError('Not running with the Werkzeug Server')
   func()