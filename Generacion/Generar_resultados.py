# Estadisticas probabilisticas eliminatorias sudamericanas
# Autor Ing. Eligio Cazo Tel 595981500340
#22/06/2023
# Revision 11/09/2023 se corrigio funcion puntajes, posiciones

import csv
import math
import operator
import os
import random
import sqlite3
import tkinter as tk
from tkinter import ttk

import pandas as pd
from openpyxl import load_workbook


def estadistica_real():
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Estadistica_real'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Estadistica_real"
        cur.execute(drop_sql)
        con.commit()

    tabla_sql ='''
    CREATE TABLE Estadistica_real (
    Anio TEXT,
    Pos1 INTEGER,
    Pos2 INTEGER,
    Pos3 INTEGER,
    Pos4 INTEGER,
    Pos5 INTEGER,
    Pos6 INTEGER,
    Pos7 INTEGER,
    Pos8 INTEGER,
    Pos9 INTEGER,
    Pos10 INTEGER
    )'''
    cur.execute(tabla_sql)
    anio_2002=('2002',43,31,30,30,27,27,18,16,16,12)
    anio_2006=('2006',34,34,28,28,25,24,22,18,18,14)
    anio_2010=('2010',34,33,33,28,24,23,23,22,15,13)
    anio_2018=('2018',41,31,28,27,26,26,24,20,14,12)
    anio_2022=('2022',45,39,28,26,24,23,19,16,15,10)

    insert_sql = "INSERT INTO Estadistica_real (Anio,Pos1,Pos2,Pos3,Pos4,Pos5,Pos6,Pos7,Pos8,Pos9,Pos10) VALUES (? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    lista=anio_2002
    valores=(lista[0], lista[1],lista[2],lista[3],lista[4], lista[5],lista[6],lista[7], lista[8],lista[9],lista[10])
    cur.execute(insert_sql, valores)
    
    insert_sql = "INSERT INTO Estadistica_real (Anio,Pos1,Pos2,Pos3,Pos4,Pos5,Pos6,Pos7,Pos8,Pos9,Pos10) VALUES (? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    lista=anio_2006
    valores=(lista[0], lista[1],lista[2],lista[3],lista[4], lista[5],lista[6],lista[7], lista[8],lista[9],lista[10])
    cur.execute(insert_sql, valores)
    
    insert_sql = "INSERT INTO Estadistica_real (Anio,Pos1,Pos2,Pos3,Pos4,Pos5,Pos6,Pos7,Pos8,Pos9,Pos10) VALUES (? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    lista=anio_2010
    valores=(lista[0], lista[1],lista[2],lista[3],lista[4], lista[5],lista[6],lista[7], lista[8],lista[9],lista[10])
    cur.execute(insert_sql, valores)
    
    insert_sql = "INSERT INTO Estadistica_real (Anio,Pos1,Pos2,Pos3,Pos4,Pos5,Pos6,Pos7,Pos8,Pos9,Pos10) VALUES (? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    lista=anio_2018
    valores=(lista[0], lista[1],lista[2],lista[3],lista[4], lista[5],lista[6],lista[7], lista[8],lista[9],lista[10])
    cur.execute(insert_sql, valores)
    
    insert_sql = "INSERT INTO Estadistica_real (Anio,Pos1,Pos2,Pos3,Pos4,Pos5,Pos6,Pos7,Pos8,Pos9,Pos10) VALUES (? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    lista=anio_2022
    valores=(lista[0], lista[1],lista[2],lista[3],lista[4], lista[5],lista[6],lista[7], lista[8],lista[9],lista[10])
    cur.execute(insert_sql, valores)
    
    con.commit()

def genera_resultado():
    resultados=[1,2,3]
    return random.choice(resultados)

def gana(stats):
    #diccionario={}
    global primero
    global segundo
    global tercero
    global cuarto
    global quinto
    global sexto
    global septimo
    
    diccionario = stats.copy()

    max_key = max(diccionario.items(), key=operator.itemgetter(1))[0]
    primero=max_key
    diccionario[max_key]=0

    max_key = max(diccionario.items(), key=operator.itemgetter(1))[0]
    segundo=max_key
    diccionario[max_key]=0

    max_key = max(diccionario.items(), key=operator.itemgetter(1))[0]
    tercero=max_key
    diccionario[max_key]=0

    max_key = max(diccionario.items(), key=operator.itemgetter(1))[0]
    cuarto=max_key
    diccionario[max_key]=0

    max_key = max(diccionario.items(), key=operator.itemgetter(1))[0]
    quinto=max_key
    diccionario[max_key]=0

    max_key = max(diccionario.items(), key=operator.itemgetter(1))[0]
    sexto=max_key
    diccionario[max_key]=0

    max_key = max(diccionario.items(), key=operator.itemgetter(1))[0]
    septimo=max_key
    diccionario[max_key]=0

    resultado=[primero, segundo, tercero, cuarto, quinto, sexto, septimo]
    
    #print ("orden:" + primero+","+segundo+","+tercero+","+cuarto+","+quinto+","+sexto+"," +septimo)

def ordena_matriz(stats):
    valores_ordenados = sorted(stats.values(), reverse=True)
    return valores_ordenados

def color():
    # Definir un color RGB
    color_rgb = (255, 153, 51)  # Rojo

    # Convertir el color RGB a código hexadecimal
    color_hex = '#{:02x}{:02x}{:02x}'.format(*color_rgb)

    print(color_hex)  # Imprimir el código hexadecimal del color

def puntajes():
    equipos = {'Brasil':0,'Argentina':1,'Uruguay':2,'Ecuador':3,'Colombia':4,'Chile':5,'Paraguay':6,'Bolivia':7,'Venezuela':8,'Peru':9}
    suma= {'0':0,'1':0,'2':0,'3':-3,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    pjugados= {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    pganados= {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    pempatados= {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    pperdidos= {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    golesafavor= {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    golescontra= {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    indices= ['0','1','2','3','4','5','6','7','8','9']
    pos= ['1','2','3','4','5','6','7','8','9','10']

    a=[]
    b=[]
    r=[]

    df = pd.read_excel(io = "fixture.xlsx", sheet_name="Fechas",header = 0)
    df.fillna(999, inplace=True)
    fecha = df['Fecha'].values
    local = df['EquipoLocal'].values
    marcador1 = df['Marcador1'].values
    marcador2 = df['Marcador2'].values
    visitante = df['EquipoVisitante'].values

    for i in range(0,90):
        l=local[i]
        indice1=equipos[local[i]]
        indice2=equipos[visitante[i]]
        v1=marcador1[i]
        v2=marcador2[i]
        if v1>v2:
            r1=1
        if v1==v2:
            r1=2
        if v1<v2:
            r1=3
        if v1==999 or v2==999:
            r1=0
        a.append(indice1)
        b.append(indice2)
        r.append(r1)

    for i in range(0,90):
        v1=marcador1[i]
        v2=marcador2[i]
        if r[i]==0:
            y=0
        else:
            y=r[i]
        
        indicea = str(a[i])
        indiceb = str(b[i])
        indice1 = indicea.replace(" ", "")
        indice2 = indiceb.replace(" ", "")
        
        if y == 1:
            suma[indice1] = suma[indice1] + 3
            pganados[indice1] = pganados[indice1]+1
            pperdidos[indice2] =pperdidos[indice2]+1
            pjugados[indice1] = pjugados[indice1]+1
            pjugados[indice2] = pjugados[indice2]+1
            golesafavor[indice1]=golesafavor[indice1]+v1
            golescontra[indice1]=golescontra[indice1]-v2
            golesafavor[indice2]=golesafavor[indice2]+v2
            golescontra[indice2]=golescontra[indice2]-v1

        if y == 2:
            suma[indice1] = suma[indice1] + 1
            suma[indice2] = suma[indice2] + 1
            pempatados[indice1] = pempatados[indice1] + 1
            pempatados[indice2] = pempatados[indice2] + 1
            pjugados[indice1] = pjugados[indice1]+1
            pjugados[indice2] = pjugados[indice2]+1
            golesafavor[indice1]=golesafavor[indice1]+v1
            golescontra[indice1]=golescontra[indice1]-v2
            golesafavor[indice2]=golesafavor[indice2]+v2
            golescontra[indice2]=golescontra[indice2]-v1

        if y == 3:
            suma[indice2] = suma[indice2] + 3
            pganados[indice2] = pganados[indice2]+1
            pperdidos[indice1] =pperdidos[indice1]+1
            pjugados[indice1] = pjugados[indice1]+1
            pjugados[indice2] = pjugados[indice2]+1
            golesafavor[indice1]=golesafavor[indice1]+v1
            golescontra[indice1]=golescontra[indice1]-v2
            golesafavor[indice2]=golesafavor[indice2]+v2
            golescontra[indice2]=golescontra[indice2]-v1
        
    indice=posiciones(suma)
    lista=ordena_matriz(suma)
    listapais=[]
    puntaje=[]
    pj=[]
    pg=[]
    pe=[]
    pp=[]
    gf=[]
    gc=[]
    dg=[]

    for i in indice:
        claves = [clave for clave, val in equipos.items() if val == int(i)]
        contenido=claves[0] + " " + str(suma[i]) +" "+str(pjugados[i])+" "+str(pganados[i])+" "+str(pempatados[i])+" "+str(pperdidos[i])+" "+str(golesafavor[i])+" " + str(abs(golescontra[i]))+ " "+ str(golesafavor[i]+golescontra[i])
        listapais.append(claves[0])
        puntaje.append(int(suma[i]))
        pj.append(int(pjugados[i]))
        pg.append(int(pganados[i]))
        pe.append(int(pempatados[i]))
        pp.append(int(pperdidos[i]))
        gf.append(int(golesafavor[i]))
        gc.append(int(golescontra[i]))
        dg.append(int(golesafavor[i]+golescontra[i]))

    if pg[0]==0:
        listapais=[]
        puntaje=[]
        for i in indices:
            claves = [clave for clave, val in equipos.items() if val == int(i)]
            listapais.append(claves[0])
            #print(claves[0])
            puntaje.append(suma[i])

    # Crear el DataFrame a partir de las listas
    df = pd.DataFrame({
        "PAIS": listapais,
        "PUNTAJE": puntaje,
        "PJ": pj,
        "PG": pg,
        "PE": pe,
        "PP": pp,
        "GF": gf,
        "GC": gc,
        "DG": dg
    })
    df_ordenado = df.sort_values(['PUNTAJE', 'DG', 'GF',"PAIS"], ascending=[False, False, False,True])
    df_ordenado = df_ordenado.reset_index(drop=True)
    df_ordenado.index = df_ordenado.index + 1


    archivo_excel = 'fixture.xlsx'
    book = load_workbook(archivo_excel)
    writer = pd.ExcelWriter(archivo_excel, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df_ordenado.to_excel(writer, sheet_name='Posiciones', index=True)
    writer.save()

    # Crear la ventana principal de tkinter
    ventana = tk.Tk()
    text_widget = tk.Text(ventana)
    text_widget.pack()
    df_texto = df_ordenado.to_string()
    text_widget.insert(tk.END, df_texto)
    ancho_ventana = 500
    alto_ventana = 200
    posicion_x = (ventana.winfo_screenwidth() - ancho_ventana) // 2
    posicion_y = (ventana.winfo_screenheight() - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
    ventana.title("Posiciones Eliminatorias Mundial 2026")
    ventana.mainloop()

def posiciones(stats):
    claves_ordenadas = sorted(stats, key=lambda x: stats[x], reverse=True)
    return claves_ordenadas

def inicializar_tablas():
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Resultados'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Resultados"
        cur.execute(drop_sql)
        con.commit()

    tabla_sql ='''
    CREATE TABLE Resultados (
    Pos1 INTEGER,
    Pos2 INTEGER,
    Pos3 INTEGER,
    Pos4 INTEGER,
    Pos5 INTEGER,
    Pos6 INTEGER,
    Pos7 INTEGER,
    Pos8 INTEGER,
    Pos9 INTEGER,
    Pos10 INTEGER
    )'''
    cur.execute(tabla_sql)

    #*********************************************************Paraguay Pos1*************************
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Paraguay1'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Paraguay1"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Paraguay1 (
    Puntaje INTEGER
    )'''
    cur.execute(tabla_sql)
    #*********************************************************Paraguay Pos1*************************
    
    #*********************************************************Paraguay Pos2*************************
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Paraguay2'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Paraguay2"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Paraguay2 (
    Puntaje INTEGER
    )'''
    cur.execute(tabla_sql)
    #*********************************************************Paraguay Pos2*************************

    #*********************************************************Paraguay Pos3*************************
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Paraguay3'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Paraguay3"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Paraguay3 (
    Puntaje INTEGER
    )'''
    cur.execute(tabla_sql)
    #*********************************************************Paraguay Pos3*************************

    #*********************************************************Paraguay Pos4*************************
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Paraguay4'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Paraguay4"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Paraguay4 (
    Puntaje INTEGER
    )'''
    cur.execute(tabla_sql)
    #*********************************************************Paraguay Pos4*************************
    
    #*********************************************************Paraguay Pos5*************************
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Paraguay5'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Paraguay5"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Paraguay5 (
    Puntaje INTEGER
    )'''
    cur.execute(tabla_sql)
    #*********************************************************Paraguay Pos5*************************

    #*********************************************************Paraguay Pos6*************************
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Paraguay6'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Paraguay6"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Paraguay6 (
    Puntaje INTEGER
    )'''
    cur.execute(tabla_sql)
    #*********************************************************Paraguay Pos6*************************

    #*********************************************************Paraguay Pos7*************************
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Paraguay7'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Paraguay7"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Paraguay7 (
    Puntaje INTEGER
    )'''
    cur.execute(tabla_sql)
    #*********************************************************Paraguay Pos7*************************

    con.commit()
    con.close()
    
    # Crea tabla de posiciones de paises *******************************************************************************
    con = sqlite3.connect('Paises.db')
    cur = con.cursor()
    consulta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='Resultados'"
    cur.execute(consulta_sql)
    tabla_existe = cur.fetchone()
    if tabla_existe:
        drop_sql = "DROP TABLE Resultados"
        cur.execute(drop_sql)

    tabla_sql ='''
    CREATE TABLE Resultados (
    Pos1 TEXT,
    Pos2 TEXT,
    Pos3 TEXT,
    Pos4 TEXT,
    Pos5 TEXT,
    Pos6 TEXT,
    Pos7 TEXT,
    Pos8 TEXT,
    Pos9 TEXT,
    Pos10 TEXT
    )'''
    cur.execute(tabla_sql)
    con.commit()
    con.close()

    estadistica_real()

#version SQL en Sqlite3 26/06/2023
def fixture3():
    #version sql y sqlite3 26/06/2023
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    global cant
        
    equipos = {'Brasil':0,'Argentina':1,'Uruguay':2,'Ecuador':3,'Colombia':4,'Chile':5,'Paraguay':6,'Bolivia':7,'Venezuela':8,'Peru':9}
    suma = {'0':0,'1':0,'2':0,'3':-3,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    indices=['0','1','2','3','4','5','6','7','8','9']
    a=[]
    b=[]
    r=[]
    f1 = "fixture2.txt"

    df = pd.read_excel(io = "fixture.xlsx", sheet_name="Fechas",header = 0)
    df.fillna(999, inplace=True)
    local = df['EquipoLocal'].values
    marcador1 = df['Marcador1'].values
    marcador2 = df['Marcador2'].values
    visitante = df['EquipoVisitante'].values

    for i in range(0,90):
        l=local[i]
        indice1=equipos[local[i]]
        indice2=equipos[visitante[i]]
        v1=marcador1[i]
        v2=marcador2[i]
    
        if v1>v2:
            r1=1
        if v1==v2:
            r1=2
        if v1<v2:
            r1=3
        if v1==999 or v2==999:
            r1=0
        a.append(indice1)
        b.append(indice2)
        r.append(r1)

        with open(f1, "a") as archivo:
            archivo.write(str(indice1) +";" + str(indice2)+";"+str(r1)+ "\n")
    
    archivo.close()
    
    # Generar resultados
    global cant
    global primero
    global segundo
    global tercero
    global cuarto
    global quinto
    global sexto
    global septimo

    #ciclo de gneracion de varlores ****************************************************************************
    for m in range (0 , cant):
        for i in range(0,90):
            if r[i]==0:
                nohay=1
                y=genera_resultado()
            else:
                y=r[i]
            
            indicea = str(a[i])
            indiceb = str(b[i])
            indice1 = indicea.replace(" ", "")
            indice2 = indiceb.replace(" ", "")
            
            
            if y == 1:
                suma[indice1] = suma[indice1] + 3
            
            if y == 2:
                suma[indice1] = suma[indice1] + 1
                suma[indice2] = suma[indice2] + 1
            
            if y == 3:
                suma[indice2] = suma[indice2] + 3
        
        
        indice_gana=posiciones(suma)
        gana(suma)
        
        lista=ordena_matriz(suma)
        
        if indice_gana[0]=='6':
            valor = lista[0]
            insert_sql = "INSERT INTO Paraguay1 (Puntaje) VALUES (?)"
            cur.execute(insert_sql, (valor,))

        if indice_gana[1]=='6':
            insert_sql = "INSERT INTO Paraguay2 (Puntaje) VALUES (?)"
            valores_py=lista[1]
            cur.execute(insert_sql, (valores_py,))
        
        if indice_gana[2]=='6':
            insert_sql = "INSERT INTO Paraguay3 (Puntaje) VALUES (?)"
            valores_py=lista[2]
            cur.execute(insert_sql, (valores_py,))
        
        if indice_gana[3]=='6':
            insert_sql = "INSERT INTO Paraguay4 (Puntaje) VALUES (?)"
            valores_py=lista[3]
            cur.execute(insert_sql, (valores_py,))
        
        if indice_gana[4]=='6':
            insert_sql = "INSERT INTO Paraguay5 (Puntaje) VALUES (?)"
            valores_py=lista[4]
            cur.execute(insert_sql, (valores_py,))
        
        if indice_gana[5]=='6':
            insert_sql = "INSERT INTO Paraguay6 (Puntaje) VALUES (?)"
            valores_py=lista[5]
            cur.execute(insert_sql, (valores_py,))
        
        if indice_gana[6]=='6':
            insert_sql = "INSERT INTO Paraguay7 (Puntaje) VALUES (?)"
            valores_py=lista[6]
            cur.execute(insert_sql, (valores_py,))
                
        insert_sql = "INSERT INTO Resultados (Pos1,Pos2,Pos3,Pos4,Pos5,Pos6,Pos7,Pos8,Pos9,Pos10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        valores=(lista[0], lista[1],lista[2],lista[3],lista[4], lista[5],lista[6],lista[7], lista[8],lista[9])
        cur.execute(insert_sql, valores)
    
        for i in indices:
            suma[i]=0
    
    con.commit()
    con.close()
    print("Proceso terminado")


if __name__ == '__main__':
    global cant
    cant=10000000
    inicializar_tablas()
    fixture3()
    