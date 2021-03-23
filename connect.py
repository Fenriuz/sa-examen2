from tkinter import *
import mysql.connector
from tkinter import messagebox

class Connect :
     def __init__(self): 
         self.connectV =None 
         try:
          connection_config_dict = {
          'user': 'cesar',
          'password': 'cesar',
          'host': 'localhost',
          'port': '3306',
          'database': 'examen',
          }
          self.connectV = mysql.connector.connect(**connection_config_dict)
         except:
          print("Error while connecting to MySQL")

     def getConnect(self):
         return self.connectV

     def insertUser(self,name,username,password,table):
         if name=="" or username=="" or password=="" :
            messagebox.showerror("Error", "Campos Vacios!")
         else:
            cursor =self.connectV.cursor()
            mySql_insert_query = """INSERT INTO user(name, username, password) 
                           VALUES (%s,%s,%s);"""
            cursor.execute(mySql_insert_query,(name,username,password))
            self.connectV.commit()
            self.fetch_data(table)
            messagebox.showerror("Exito!", "Registro Ingresado!")

     def updateUser(self,name,username,password,id,table):
         if name=="" or username=="" or password=="" :
            messagebox.showerror("Error", "Campos Vacios!")
         else:
           cursor = self.connectV.cursor()
           mySql_insert_query = """UPDATE `user` SET name=%s,username=%s,password=%s WHERE id=%s"""
           record = (name, username, password,id)
           cursor.execute(mySql_insert_query, record)
           self.connectV.commit()
           self.fetch_data(table)
           messagebox.showerror("Exito!", "Registro Actualizado!")

     def deleteUser(self,id,table):
        print(id)
        cursor = self.connectV.cursor()
        cursor.execute("DELETE  from `user` WHERE id=%s", id)
        self.connectV.commit()
        self.fetch_data(table)
        messagebox.showerror("Exito!", "Registro Borrado!")

     def fetch_data(self,tabla):
        cursor = self.connectV.cursor()
        cursor.execute("select name,username,password,id from user")
        tabla.delete(*tabla.get_children()) 
        rows=cursor.fetchall()
        if len(rows)!=-1:
	         for row in rows:
                     tabla.insert('',END,values=row)
        self.connectV.commit()
