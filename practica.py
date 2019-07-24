from flask import Flask,render_template
import pymongo
from pymongo import MongoClient
import pprint

cliente = pymongo.MongoClient("mongodb://172.16.11.20:27017")
mydb = cliente["Prueba2"]
coleccion1 = mydb["becarios"]


app = Flask(__name__)

@app.route('/')
def practica():



    return render_template("index.html")
#    return '<h1>Pratica dsadsa</h1>'

if __name__== '__main__':
    app.run(debug=True)
