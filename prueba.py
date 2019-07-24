import pymongo
import pprint
cliente = pymongo.MongoClient("mongodb://172.16.11.20:27017")
mydb = cliente["Prueba2"]
coleccion1 = mydb["becarios"]
coleccion2 = mydb["empleados"]

archivo = 'C:/Users/dgarcia/Desktop/Prueba2/prueba.txt'
archivo2 = 'C:/Users/dgarcia/Desktop/Prueba2/prueba2.txt'

archivoold= open(archivo, "r")
archivonew =open(archivo2,"w")
for line in archivoold:
    archivonew.write(line.replace('=', ':'))
#archivoold.close()


mydb = cliente ['Prueba2']
coleccion = mydb["becarios"]

collection = {
'nombre':'Diana',
'edad': 24,
'area': 'desarrollo',
'rating':4.31
}

result = coleccion.find()

result = coleccion.find()
result = list(result)
#pprint.pprint (result)
#archivonew= {"nombre":'Joshua',"edad":24,"area":'desarrollo',"rating":4.31}
archivonew =open(archivo2,"r")

lectura = archivonew.read()
print (lectura)
