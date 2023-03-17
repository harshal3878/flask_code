import mysql.connector
from flask import Flask,  request
from flask_cors import CORS
import json
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