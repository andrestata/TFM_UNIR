import xmltodict
import pymongo
import pandas as pd
import Funciones
import xml.etree.ElementTree as ET

#Conecta al cliente Mongo
client = pymongo.MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)

#Carga la base de datos siedco
dbSiedco = client["siedco"]
#Carga la coleccion delitos
coleccionDelitos = dbSiedco["delitos"]

# Borrar todos los documentos de la colección
#result = coleccionDelitos.delete_many({})
#print(result.deleted_count, "documentos borrados.") 
    
# Abrir el archivo XML
#with open('C:/Users/ANDRES F/Downloads/Siedco_Prueba.xml', 'r', encoding='utf-8') as archivo:
with open('D:/Datos_Siedco/2019.xml', 'r', encoding='utf-8') as archivo:
    xml_string = archivo.read()

# Parsear el archivo XML en un árbol de elementos
root = ET.fromstring(xml_string)

#print("{} documentos insertados.".format(Funciones.cargar_delitos_parcial(root, coleccionDelitos, "202205", None)))
#print("{} documentos insertados.".format(Funciones.cargar_delitos_completa(root, coleccionDelitos)))
