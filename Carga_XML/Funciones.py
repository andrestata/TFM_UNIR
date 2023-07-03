# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:41:53 2023

@author: ANDRES F
"""
from datetime import datetime, date, timedelta


def cargar_delitos_parcial(root, coleccionDelitos, periodo, num_registros):
    formato_fecha = "%Y-%m-%d"
    rowInsert = 0
    
    # Obtener la fecha mayor del periodo
    fecha_mayor = datetime.strptime(periodo, '%Y%m') + timedelta(days=31)
    fecha_mayor = fecha_mayor.replace(day=1) - timedelta(days=1)

    # Obtener la fecha menor del periodo
    fecha_menor = datetime.strptime(periodo, '%Y%m')

    # Cree un diccionario de mapeo de claves para renombrar las claves
    mapeo_claves = {"C0": "Fecha", "C1": "Anio", "C2": "Nro_Mes", "C3": "Mes", "C4": "Nombre_Dia", "C5": "Rango_Dia",
                    "C6": "Localidad", "C7": "UPZ", "C8": "Sexo", "C9": "Delito", "C10": "Modalidad", "C11": "Arma_Empleada", "C12": "Numero_Hechos"}

    # Iterar sobre los elementos y agregarlos a la base de datos
    for elemento in root:
        my_dict = {}  # Crear un nuevo diccionario en cada iteración
        cont = 0
        flag = False

        for hijo in elemento:
            elemento_hijo = hijo.tag.replace(
                '{urn:schemas-microsoft-com:xml-analysis:rowset}', '').strip()
            if len(elemento_hijo) > 3:
                continue
            else:
                #print(hijo.text)
                if flag:
                    my_dict[elemento_hijo] = hijo.text
                    cont += 1
                if (elemento_hijo == 'C0') and (datetime.strptime(hijo.text, formato_fecha).date() >= fecha_menor.date())\
                        and (datetime.strptime(hijo.text, formato_fecha).date() <= fecha_mayor.date()):
                    my_dict[elemento_hijo] = hijo.text
                    flag = True
                else:
                    continue

        # Insertar el documento en la base de datos
        if len(my_dict) > 0 and rowInsert < (num_registros if num_registros is not None else rowInsert+1):
            # rename() para cambiar los nombres de las claves del documento
            documento = {mapeo_claves.get(
                key, key): val for key, val in my_dict.items()}
            coleccionDelitos.insert_one(documento)
            rowInsert += 1            
                
            
    return(rowInsert)

def cargar_delitos_completa(root, coleccionDelitos):
   
    rowInsert = 0    

    # Cree un diccionario de mapeo de claves para renombrar las claves
    mapeo_claves = {"C0": "Fecha", "C1": "Anio", "C2": "Nro_Mes", "C3": "Mes", "C4": "Nombre_Dia", "C5": "Rango_Dia",
                    "C6": "Localidad", "C7": "UPZ", "C8": "Sexo", "C9": "Delito", "C10": "Modalidad", "C11": "Arma_Empleada", "C12": "Numero_Hechos"}

    # Iterar sobre los elementos y agregarlos a la base de datos
    for elemento in root:
        my_dict = {}  # Crear un nuevo diccionario en cada iteración
       
        for hijo in elemento:
            elemento_hijo = hijo.tag.replace(
                '{urn:schemas-microsoft-com:xml-analysis:rowset}', '').strip()
            if len(elemento_hijo) > 3:
                continue
            else:
                my_dict[elemento_hijo] = hijo.text              

        # Insertar el documento en la base de datos
        if len(my_dict) > 0:
            # rename() para cambiar los nombres de las claves del documento
            documento = {mapeo_claves.get(
                key, key): val for key, val in my_dict.items()}
            coleccionDelitos.insert_one(documento)
            rowInsert += 1            
                
            
    return(rowInsert)
