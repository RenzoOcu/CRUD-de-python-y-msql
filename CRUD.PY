#CRUD create (insertar )Read (leer) Update (Actualizar )Delete (eliminar )

import os
import  time
import mysql.connector



#creamos l conexion a la base de datos 
mysb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tiendaperu"
    
)
#para recoger un a tabla  crearemos  un objetos de tipo cursor

mycursor=mysb.cursor()

#creamos nuestro front end
while True:
    print('--menu del sistemas--'
          '\n1 agregar un producto'
          '\n2 eliminar un producto'
          '\n3 buscar  un producto'
          '\n4 actualizar  un producto'
          '\n5 mostrarel catalogo de  un producto'
          '\n6 salir del producto.')
    opcion= int (input("elige una opcion:"))
    #ahora programamos nuestro back end 
    
    if opcion==1 :
        clave=input("ingresa la clave del producto")
        nombre= input("ingresa el nombre del producto")
        sql='INSERT INTO productos(clave, nombre)VALUES(%s,%s)'
        #guadamos los datos  a insertar
        val = (clave, nombre)
        #listos para ejecutar laq instruccion
        
        mycursor.execute(sql,val)
        #se realizaran cambios  en la base de datos
        mysb.commit()
        #avisamos al usuario
        print(mycursor.rowcount,'registro modificado')
        #pausa de dos segundos
        time.sleep(2)
        #limpiamos 
        os.system('cls')
    elif opcion==2:
        clave= input("ingresa  la clave del producto a eliminar:")
        sql='DELETE FROM productos WHERE clave=%s'
        val = (clave,) 
        mycursor.execute(sql, val)
        mysb.commit()
        print(mycursor.rowcount,'registro eliminado ')
        time.sleep(2)
        os.system('cls')
    elif opcion ==3:
        clave= input('ingresa la clave del producto que estas buscando')
        sql='SELECT *from productos WHERE clave =%s'
        val=(clave,)
        myresult= mycursor.fetchone()
        if myresult:
            print(f'el producto exite  en la base de datos , nombre: {myresult[1]}')
        else:
            print('el producto no existe en la base de datos ')    
        time.sleep(2)
        os.system('cls')
    elif opcion==4:
        clave=input('ingresa la clave del producto a modificar:')
        nombre=input('ingresa el nuevo nombre del producto  a modificar:')
        sql='UPDATE productos  SET nombres =%s WHERE clave=%s '
        val=(nombre,clave)
        mycursor.execute(sql,val)
        mysb.commit()
        print(mycursor.rowcount,'registro modificado') 
        time.sleep(2)
        os.system('cls')
    elif opcion ==5:
        mycursor.execute('SELECT *FROM productos')    
        myresult=mycursor.fetchall()
        print('catalogo de productos es ')
        for x in mycursor:
            print(x)
        time.sleep(3)
        os.system('cls')
    elif opcion==6:
        respuesta=input("estas seguro ?(s/n)")
        if respuesta.upper()=='s':
            print('saliendo del sistema')
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')
    else:
      print('opcion no valida , intenta de nuevo ')
      time.sleep(2)
      os.system('cls')

mysb.close()      
      
      
                          
        
        
        
    