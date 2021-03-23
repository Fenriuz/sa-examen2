from tkinter import * 
from tkinter import ttk

class Register :
     def __init__(self,window,connect) :
         self.color="light blue"
         self.font=("Arial", 16,"bold")
         self.textName= StringVar()
         self.textUser= StringVar()
         self.textPass= StringVar()
         self.window=window
         self.window.configure(background=self.color) 
         self.window.title("Registro Usuario") 
         self.window.geometry("500x300") 
         self.id=""
         heading = Label(self.window, text="Formulario",bg=self.color,font=self.font) 
         name=Label(self.window, text="Nombre", bg=self.color) 
         user=Label(self.window, text="Usuario", bg=self.color) 
         password=Label(self.window, text="Contrasena", bg=self.color)
         heading.grid(row=0, column=1) 
         name.grid(row=1, column=0) 
         user.grid(row=2, column=0) 
         password.grid(row=3, column=0)
         name_field = Entry(self.window,textvariable=self.textName) 
         user_field = Entry(self.window,textvariable=self.textUser) 
         pass_field = Entry(self.window,textvariable=self.textPass) 
         name_field.grid(row=1, column=1, ipadx="100") 
         user_field.grid(row=2, column=1, ipadx="100") 
         pass_field.grid(row=3, column=1, ipadx="100")
         submit = Button(self.window, text="registrarse", fg="Black", bg="Green",foreground="White",command=lambda:connect.insertUser(self.textName.get(),self.textUser.get(),self.textPass.get(),self.table)) 
         submit.place(x=10,y=100)
         close= Button(self.window, text="salir", fg="Black", bg="Red",foreground="White") 
         close.place(x=110,y=100)
         Detail_Frame=Frame(self.window)
         update= Button(self.window, text="actualizar", fg="Black", bg="Red",foreground="White",command=lambda:connect.updateUser(self.textName.get(),self.textUser.get(),self.textPass.get(),self.id,self.table)) 
         update.place(x=170,y=100)
         delete= Button(self.window, text="Eliminar", fg="Black", bg="Red",foreground="White",command=lambda:connect.deleteUser(self.id,self.table)) 
         delete.place(x=260,y=100)
         Detail_Frame.place(x=0,y=130,width=500,height=300)
         Table_Frame=Frame(Detail_Frame,bd=2,relief=RIDGE, bg="crimson")
         Table_Frame.place(x=0,y=0,width=500,height=300)
         scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
         scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
         self.table=ttk.Treeview(Table_Frame,columns=("nombre","usuario", "password"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT, fill=Y)
         scroll_x.config(command=self.table.xview)
         scroll_y.config(command=self.table.yview)
         self.table.heading("nombre",text="Nombre")
         self.table.heading("usuario",text="Usuario")
         self.table.heading("password",text="password")
         self.table['show']= 'headings'
         self.table.column("nombre", width=100)
         self.table.column("usuario", width=100)
         self.table.column("password", width=100)
         self.table.pack(fill=BOTH,expand=1)
         self.table.bind("<ButtonRelease-1>",self.get_cursor)
         connect.fetch_data(self.table)

     def get_cursor(self,ev):
         cursor_row=self.table.focus()
         contents=self.table.item(cursor_row)
         row=contents['values']
         self.textName.set(row[0])
         self.textUser.set(row[1])
         self.textPass.set(row[2])
         self.id=row[3]
