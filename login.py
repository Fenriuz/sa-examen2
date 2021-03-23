from tkinter import * 
import os

class Login:
     def __init__(self,window,connect) :
         self.color="light blue"
         self.font=("Arial", 16,"bold")
         self.textName= StringVar()
         self.textUser= StringVar()
         self.textPass= StringVar()
         self.window=window
         self.window.configure(background=self.color) 
         self.window.title("Login Usuario") 
         self.window.geometry("500x300") 
         heading = Label(self.window, text="Formulario",bg=self.color,font=self.font) 
         user=Label(self.window, text="Usuario", bg=self.color) 
         password=Label(self.window, text="Contrasena", bg=self.color)
         heading.grid(row=0, column=1) 
         user.grid(row=2, column=0) 
         password.grid(row=3, column=0)
         user_field = Entry(self.window,textvariable=self.textUser) 
         pass_field = Entry(self.window,textvariable=self.textPass) 
         user_field.grid(row=2, column=1, ipadx="100") 
         pass_field.grid(row=3, column=1, ipadx="100")
         submit = Button(self.window, text="Iniciar Sesion", fg="Black", bg="Green",foreground="White",command=lambda:connect.insertUser(self.textUser.get(),self.textPass.get())) 
         submit.place(x=10,y=100)
         close= Button(self.window, text="salir", fg="Black", bg="Red",foreground="White") 
         close.place(x=110,y=100)
         register= Button(self.window, text="Registrarse", fg="Black", bg="Red",foreground="White",command=lambda:self.registerPage()) 
         register.place(x=170,y=100)

     def registerPage(self):
         os.system('python register.py')
