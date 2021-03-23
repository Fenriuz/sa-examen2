from register import Register
from login import Login
from connect import Connect
# from register import Register
from tkinter import * 

ventana = Tk()
connect=Connect()
ob=Register(ventana,connect)
# ob=Login(ventana,connect)
ventana.mainloop()
