from flask import Flask,render_template
import pymongo
from pymongo import MongoClient

app = Flask(__name__)


#cliente = pymongo.MongoClient("mongodb://localhost:27017")
client = MongoClient('mongodb://localhost:27017')
db = client.Prueba2
#mydb = cliente["Prueba2"]
#db = mydb["respaldo"]
@app.route('/')
def practica():

    result = db.respaldo.aggregate([
{"$group":{"_id":{"NOMBRE":"$nombre","EDAD":"$edad"}}}
])

    result = list(result)

    return render_template("index.html",result=result)
@app.route('/base')
def p():
    return render_template("base.html")


if __name__== '__main__':
    app.run(debug=True)
print(list(result))
