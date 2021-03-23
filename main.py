from register import Register
from login import Login
from connect import Connect
from tkinter import * 

ventana = Tk()
connect=Connect()
ob=Register(ventana,connect)
ventana.mainloop()
