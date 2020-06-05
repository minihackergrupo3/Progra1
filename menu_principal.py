from tkinter import * #Libreria Tkinter (Se usa para crear interfaces graficas)
from tkinter import messagebox # Parte de la libreria Tkinter, importa las ventanas flotantes, mensajes emergentes
import sqlite3 #Importa la libreria sqlite3 para poder unsar comandos de sql en python y asi comunicarse con la baase de datos
from tkinter import messagebox as MessageBox #Es parte de la libreria Tkinter y se usa para importar una mas amplia variedad de mensajer emergentes

fondo=Tk() #Raiz del del programa
fondo.geometry("815x725")
fondo.title("VEPROEL.S.A     V.1.00.2")
fondo.resizable(False,False)
fondo.iconbitmap("computer2.ico")
fondo.config(bg="#9FA7B3")

def salir(): 
    fondo.destroy() #Funcion para salir del programa

#----------Mensajes emergentes de ayuda----------

def AReg():
    messagebox.showinfo("Ayuda","Debe de ingresar los datos que se le solicitan, Email, Nit y Telefono no pueden ser datos repetidos")

def ACon():
    messagebox.showinfo("Ayuda","Puede visualizar los clientes, proveedores, vendedores e inventario registrado, ademas puede consultar las facturas de compra y venta")

def ACom():
    messagebox.showinfo("Ayuda", "Debe de ingresar los datos que se le solicitan, puede agregar hasta 4 productos, puede retirarlos si desea, debe de sumar y si desea comprar presione COMPRAR")

def AVen():
    messagebox.showinfo("Ayuda", "Debe de ingresar los datos que se le solicitan, puede agregar hasta 4 productos, puede retirarlos si desea, debe de sumar y si desea comprar presione VENDER")

def Ainfo():
    messagebox.showinfo("Informacion", "Desarrollado por: Herbert Perez, Julio Mulul Y Luis Mendoza, seccion:A")

#----------Menu flotante----------

barraMenu=Menu(fondo)

menuArchivo=Menu(barraMenu)
menuAyuda=Menu(barraMenu)
menuInfo=Menu(barraMenu)

menuArchivo.add_command(label="Salir", command=salir)
menuAyuda.add_command(label="Ayuda Registro", command=AReg)
menuAyuda.add_command(label="Ayuda Consulta", command=ACon)
menuAyuda.add_command(label="Ayuda Compras ", command=ACom)
menuAyuda.add_command(label="Ayuda Ventas", command=AVen)
menuInfo.add_command(label="Acerca de...", command=Ainfo)

barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
barraMenu.add_cascade(label="About", menu=menuInfo)

fondo.config(menu=barraMenu)

#----------Titulo----------

miframetitulo=Frame(fondo) #frame utilizado para mostrar en pantalla la leyenda: "Menu principal"

labelmenu=Label(miframetitulo, text="                           Menu principal                           ")
labelmenu.config(bg="#73C043", font=("Segoe Script", 20))
labelmenu.grid(row=1, column=1)

miframetitulo.pack()

miFrame=Frame(fondo)
miFrame.config(bg="#508BFA")
miFrame.config(bd=10, relief="groove")
miFrame.pack()

#---------------Variables y contadores---------------

nombreprueba1=StringVar()

varRegistro=IntVar()
varVis=IntVar()
varFac=IntVar()

contador123 = 0
contador1234 = 0 
contador12345 = 0
contador123456 = 0

contadorabc = 0
contadorabcd = 0
contadorabcde = 0
contadorabcdef = 0

contadora1 = 0
contadora2 = 0
contadora3 = 0
contadora4 = 0

contadorb1 = 0
contadorb2 = 0
contadorb3 = 0
contadorb4 = 0

subtotalFacComp2 = 0
subtotalFacComp1 = 0
subtotalFacComp3 = 0
subtotalFacComp4 = 0

subtotalFacVent1 = 0
subtotalFacVent2 = 0
subtotalFacVent3 = 0
subtotalFacVent4 = 0

zz = 0

#--------------------------Multilist mostrar compras detalle--- config con 4 filas
class MultiListboxCompD(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, height=4, borderwidth=0, selectborderwidth=5,
            relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        """
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set
        """
    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'
 
    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'
 
    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'
 
    def _scroll(self, *args):
        for l in self.lists:
            l.yview(*(args))
 
    def curselection(self):
        return self.lists[0].curselection()
 
    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)
 
    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last: 
            return map(*([None]+result))
        return result
 
    def index(self, index):
        self.lists[0].index(index)
 
    def insert(self, index, *elements):
        for e in elements:
            i = 0
        for l in self.lists:
            l.insert(index, e[i])
            i = i + 1
 
    def size(self):
        return self.lists[0].size()
 
    def see(self, index):
        for l in self.lists:
            l.see(index)
 
    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)
 
    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)
 
    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)
 
    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

#---------------------------Multilist mostrar compras vista ---------Config con 1 fila grande

class MultiListboxCompV(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, height=1, borderwidth=5, selectborderwidth=5,
            relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        """
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set
        """
    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'
 
    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'
 
    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'
 
    def _scroll(self, *args):
        for l in self.lists:
            l.yview(*(args))
 
    def curselection(self):
        return self.lists[0].curselection()
 
    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)
 
    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last: 
            return map(*([None]+result))
        return result
 
    def index(self, index):
        self.lists[0].index(index)
 
    def insert(self, index, *elements):
        for e in elements:
            i = 0
        for l in self.lists:
            l.insert(index, e[i])
            i = i + 1
 
    def size(self):
        return self.lists[0].size()
 
    def see(self, index):
        for l in self.lists:
            l.see(index)
 
    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)
 
    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)
 
    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)
 
    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

#--------------------------------multilist mostrar Inventario y personas----------------------------------
class MultiListbox(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,
            relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set
 
    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'
 
    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'
 
    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'
 
    def _scroll(self, *args):
        for l in self.lists:
            l.yview(*(args))
 
    def curselection(self):
        return self.lists[0].curselection()
 
    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)
 
    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last: 
            return map(*([None]+result))
        return result
 
    def index(self, index):
        self.lists[0].index(index)
 
    def insert(self, index, *elements):
        for e in elements:
            i = 0
        for l in self.lists:
            l.insert(index, e[i])
            i = i + 1
 
    def size(self):
        return self.lists[0].size()
 
    def see(self, index):
        for l in self.lists:
            l.see(index)
 
    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)
 
    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)
 
    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)
 
    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

def avisoexitoso1():
    messagebox.showwarning("!HECHO¡","¡Compra realizada con éxito!")

def avisoerrorComp():
    messagebox.showwarning("!ERROR¡","¡La factura no existe!")


#-------------------------Registro de clientes-------------------------

def RegistroClientes():

    frameTitCli=Frame(fondo) #frame titulo
    labelTCli=Label(frameTitCli, text="                     Registro de Clientes                     ")
    labelTCli.config(bg="#E59E5B", font=("Segoe Script", 18))
    labelTCli.grid(row=1, column=1)
    frameTitCli.pack()

    frameRCli=Frame(fondo)# frame contenido
    frameRCli.pack()

    emailCli=StringVar()
    NombreCli=StringVar()
    ApellidoCli=StringVar()
    TelefonoCli=IntVar()
    CiudadCli=StringVar()
    NITCli=StringVar()

    #---ventana emergente de exito---
    def alertaCli():
        messagebox.showwarning("!HECHO¡","¡Cliente registrado con exito!")

    #---ventana emergente de error---
    def alertaCli1():
        messagebox.showwarning("!FATAL ERROR¡","¡El Cliente ya esta registrado!")

    #---salir de la funcion registro de clientes---
    def salirRCli():
        frameRCli.destroy()
        frameTitCli.destroy()

    #---limpiar campos---
    def borrarRCli():
        emailCli.set("")
        NombreCli.set("")
        ApellidoCli.set("")
        TelefonoCli.set("")
        CiudadCli.set("")
        NITCli.set("")

    #---funcion de envio de datos---
    def botonEnvCLi():
        global emailCLiSave, NombreCliSave, ApellidoCliSave, TelefonoCliSave, CiudadCliSave, NITCliSave

        emailCLiSave=emailCli.get()
        NombreCliSave=NombreCli.get()
        ApellidoCliSave=ApellidoCli.get()
        TelefonoCliSave=TelefonoCli.get()
        CiudadCliSave=CiudadCli.get()
        NITCliSave=NITCli.get()

        envioCli()

    #---funcion para mostrar en pantalla los campos---
    def ingresoClientes():
        #------Los label-----

        lRCliEmail=Label(frameRCli, text="E-mail")
        lRCliEmail.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        lRCliNombre=Label(frameRCli, text="nombre")
        lRCliNombre.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        lRCliApellido=Label(frameRCli, text="apellido")
        lRCliApellido.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        lRCliTelefono=Label(frameRCli, text="telefono")
        lRCliTelefono.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        lRCliCiudad=Label(frameRCli, text="Ciudad")
        lRCliCiudad.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        lRCliNIT=Label(frameRCli, text="NIT")
        lRCliNIT.grid(row=6, column=1, padx=10, pady=5, sticky="w")   

        #-------Los entry-----

        eRCliEmail=Entry(frameRCli, textvariable=emailCli)
        eRCliEmail.grid(row=1, column=2, padx=10, pady=5)

        eRCliNombre=Entry(frameRCli, textvariable=NombreCli)
        eRCliNombre.grid(row=2, column=2)

        eRCliApellido=Entry(frameRCli, textvariable=ApellidoCli)
        eRCliApellido.grid(row=3, column=2)

        eRCliTelefono=Entry(frameRCli, textvariable=TelefonoCli)
        eRCliTelefono.grid(row=4, column=2)

        eRCliCiudad=Entry(frameRCli, textvariable=CiudadCli)
        eRCliCiudad.grid(row=5, column=2)

        eRCliNIT=Entry(frameRCli, textvariable=NITCli)
        eRCliNIT.grid(row=6, column=2)

        #------boton registrar----

        bRCliEnv=Button(frameRCli, text="* ENVIAR *", command=botonEnvCLi)
        bRCliEnv.grid(row=7, column=2)

    #---funcion para registrar los datos---
    def envioCli():
        global emailCLiSave, NombreCliSave, ApellidoCliSave, TelefonoCliSave, CiudadCliSave, NITCliSave

        conexionCli=sqlite3.connect("inventario.db")
        cursorCli1=conexionCli.cursor()
        cursorCli2=conexionCli.cursor()

        datosCLi=[
            (emailCLiSave, NombreCliSave, ApellidoCliSave, TelefonoCliSave, CiudadCliSave, NITCliSave)
        ]

        cursorCli2.execute("SELECT NIT FROM DClientes")
        datosCliSave=cursorCli2.fetchall()

        cc=0
        for l in datosCliSave:
            if l[0]==datosCLi[0][5]:
                cc += 1

        if cc==0:
            cursorCli1.executemany("INSERT INTO DClientes VALUES (NULL,?,?,?,?,?,?)", datosCLi)
            alertaCli()

        if cc==1:
            alertaCli1()

        conexionCli.commit()
        conexionCli.close()

    ingresoClientes()

    #--- botones---
    bRCliSalir=Button(frameRCli, text="* Salir *", command=salirRCli)
    bRCliSalir.grid(row=7, column=4, padx=10, pady=5)

    bRCliborrar=Button(frameRCli, text="* Borrar *", command=borrarRCli)
    bRCliborrar.grid(row=7, column=3, padx=10, pady=5)

#-------------------------Registro de vendedores-------------------------

def RegistroVendedores():

    frameTitVend=Frame(fondo) # frame del titulo
    labelTVend=Label(frameTitVend, text="                     Registro de Vendedores                     ")
    labelTVend.config(bg="#E59E5B", font=("Segoe Script", 18))
    labelTVend.grid(row=1, column=1)
    frameTitVend.pack()

    frameVend=Frame(fondo) # frame del contenido
    frameVend.pack()

    nombVend=StringVar()
    apeVend=StringVar()
    telVend=IntVar()

    #-----Ventana emergente de exito-----
    def alertaVend():
        messagebox.showwarning("!HECHO¡","¡Vendedor registrado con exito!")

    #-----Ventana emergente de error-----
    def alertaVend1():
        messagebox.showwarning("!FATAL ERROR¡","¡El Vendedor ya esta registrado!")

    #-----funcion salir del registro de vendedores-----
    def salirVend():
        frameVend.destroy()
        frameTitVend.destroy()

    #-----funcion borrar campos de datos-----
    def limpiarPantVend():
        nombVend.set("")
        apeVend.set("")
        telVend.set("")

    #-----funcion para guardar las variables que se usaran en el envio-----
    def botonEnvVend():
        global nombVendSave, apeVendSave, telVendSave
        nombVendSave=nombVend.get()
        apeVendSave=apeVend.get()
        telVendSave=telVend.get()
        envioVend()

    #-----funcion que crea los campos de ingreso de datos y los label con textos-----
    def ingresoVend():
        #---Los Entry---

        eNombVend=Entry(frameVend, textvariable=nombVend)
        eNombVend.grid(row=1, column=2, padx=10, pady=10)

        eApeVend=Entry(frameVend, textvariable=apeVend)
        eApeVend.grid(row=2, column=2, padx=10, pady=10)

        eTelVend=Entry(frameVend, textvariable=telVend)
        eTelVend.grid(row=3, column=2, padx=10, pady=10)

        #---Los Label---

        lNombVend=Label(frameVend, text="Nombre:")
        lNombVend.grid(row=1, column=1, padx=10, pady=10)

        lApeVend=Label(frameVend, text="Apellido:")
        lApeVend.grid(row=2, column=1, padx=10, pady=10)

        lTelVend=Label(frameVend, text="Telefono:")
        lTelVend.grid(row=3, column=1, padx=10, pady=10)

        bEnvioVend=Button(frameVend, text="* ENVIO *", command=botonEnvVend)
        bEnvioVend.grid(row=4, column=1, padx=10, pady=10)

    #----- envio de datos para ser guardados en la base de datos-----
    def envioVend():
        global nombVendSave, apeVendSave, telVendSave

        conexionVend=sqlite3.connect("inventario.db")
        cursorVend=conexionVend.cursor()
        cursor2Vend=conexionVend.cursor()

        datosVend=[
            (nombVendSave, apeVendSave,0, telVendSave)
        ]

        cursor2Vend.execute("SELECT Telefono FROM DVendedores")
        datosVendSave=cursor2Vend.fetchall()

        v=0
        for j in datosVendSave:
            if j[0] == datosVend[0][3]:
                v += 1

        if v==0: 

            cursorVend.executemany("INSERT INTO DVendedores VALUES (NULL,?,?,?,?)", datosVend)
            alertaVend()  

        if v==1:
            alertaVend1()

        conexionVend.commit()
        conexionVend.close()

    ingresoVend()

    #---Los botones---

    bBorrarVend=Button(frameVend, text="* BORRAR *", command=limpiarPantVend)
    bBorrarVend.grid(row=4, column=2, padx=10, pady=10)

    bSalirVend=Button(frameVend, text="* SALIR *", command=salirVend)
    bSalirVend.grid(row=4, column=3, padx=10, pady=10)

#-------------------------Registro de Proveedores-------------------------

def RegistroProveedores():

    #---frame del titulo---
    frameTitProv=Frame(fondo)
    labelTProv=Label(frameTitProv, text="                     Registro de Proveedores                     ")
    labelTProv.config(bg="#E59E5B", font=("Segoe Script", 18))
    labelTProv.grid(row=1, column=1)
    frameTitProv.pack()

    #---frame del contenido---
    frameRProv=Frame(fondo)
    frameRProv.pack()

    #--------variabes globales
    minombre = StringVar()
    miPBX = IntVar()
    miNIT = IntVar()

    #---funcion para salir del registro de proveedores---
    def salirRegProv():
        frameRProv.destroy()
        frameTitProv.destroy()

    #---funcion para limpiar campos
    def borrarRegProv():
        miNIT.set("")
        minombre.set("")
        miPBX.set("")

    #---ventana emergente de exito---
    def alerta1():
        messagebox.showwarning("!HECHO¡","¡Proveedor registrado con exito!")

    #---ventana emergente de error---
    def alerta2():
        messagebox.showwarning("!FATAL ERROR¡","¡El proveedor ya esta registrado!")

    #---funcion para enviar datos---
    def codigoboton():
        global nombre, PBX, NIT 
        NIT = miNIT.get()
        nombre = minombre.get()
        PBX = miPBX.get()
    
        conexion_db()
    
    #---ingresos de datos
    def ingresos_texto(): 

        lb = Label(frameRProv, text = "NIT:")
        lb.grid(row = 0, column = 1, sticky = "e",padx=20, pady=10)

        txt = Entry(frameRProv, textvariable = miNIT)
        txt.grid(row = 0,column = 2, padx=20, pady=10)

        lb = Label(frameRProv, text = "nombre:")
        lb.grid(row = 1, column = 1, sticky = "e",padx=20, pady=10)

        txt = Entry(frameRProv, textvariable = minombre)
        txt.grid(row = 1,column = 2, padx=20, pady=10)

        lb = Label(frameRProv, text = "PBX:")
        lb.grid(row = 2, column = 1, sticky = "e",padx=20, pady=10)
        
        txt = Entry(frameRProv, textvariable = miPBX)
        txt.grid(row = 2,column = 2, padx=20, pady=10)


        botton1 = Button(frameRProv, text="* ENVIAR *", command = codigoboton)
        botton1.grid(row = 3, column = 1)

    #---funcion para registrar datos a la base de datos---
    def conexion_db():
        global nombre, PBX, NIT
        conexion = sqlite3.connect("inventario.db")

        conector_Intro = conexion.cursor()#introduce datos al db 
        conector_ComProv = conexion.cursor()#busca los valores del NIT from Dproveedores

        valores = [
            (
                NIT,
                nombre,
                PBX,
                0
            )
        ]
        conector_ComProv.execute("SELECT NIT FROM DProveedores")
        tupla1 = conector_ComProv.fetchall()
        a = 0

        for i in tupla1:
            if i[0] == valores[0][0]:
                a += 1
 
        if a == 0:
            conector_Intro.executemany("insert into DProveedores values (NULL,?,?,?,?)", valores)
            alerta1()
        
        if a == 1:
            alerta2()

        conexion.commit()
        conexion.close()

    ingresos_texto()

    #--------los botones--------
    
    bBorrarRProv=Button(frameRProv, text="* BORRAR *", command=borrarRegProv)
    bBorrarRProv.grid(row=3, column=2, padx=20, pady=10)

    bSalirRProv=Button(frameRProv, text="* SALIR *", command=salirRegProv)
    bSalirRProv.grid(row=3, column=3, padx=20, pady=10)

#-------------------------Consulta de clientes registrados-------------------------

def visualizacionClientes():

    #---frame del titulo---
    frameTitCli=Frame(fondo)
    labelTVClientes=Label(frameTitCli, text="                        Cientes registrados                        ")
    labelTVClientes.config(bg="#C4CF52", font=("Segoe Script", 18))
    labelTVClientes.grid(row=1, column=1)
    frameTitCli.pack()

    #--- frame del contenido---
    frameVClientes=Frame(fondo)
    frameVClientes.pack()

    #---funcion para salir de consulta de clientes---
    def salirVClientes():
        frameTitCli.destroy()
        frameVClientes.destroy()

    conexionVCli=sqlite3.connect("inventario.db")
    cursorVCli=conexionVCli.cursor()

    cursorVCli.execute("SELECT * FROM DClientes ")
    tuplaVCli=cursorVCli.fetchall()

    mlbC = MultiListbox(frameVClientes, (('Codigo', 7), ('Email', 15), ('Nombre', 20),('Apellido', 15),('Telefono',10),('Ciudad',15),('NIT ',10)))
    b = 0
    for p in tuplaVCli:
        mlbC.insert(END, (p[0], p[1], p[2],p[3], p[4], p[5], p[6]))
        b += 1
    mlbC.grid(row=0, column=1)

    #-------los Botones---------

    bsalirVCli=Button(frameVClientes, text="* SALIR *", command= salirVClientes)
    bsalirVCli.grid(row=1, column=1, padx=10, pady=10)

#-------------------------Consulta de vendedores-------------------------

def visualizacionVendedores():

    #---frame del titulo   
    frameTVVend=Frame(fondo)
    labelTVVend=Label(frameTVVend, text="                     Vendedores registrados                     ")
    labelTVVend.config(bg="#C4CF52", font=("Segoe Script", 18))
    labelTVVend.grid(row=1, column=1)
    frameTVVend.pack()

    #---frame del contenido---
    frameVVendedores=Frame(fondo)
    frameVVendedores.config(bg="#9FA7B3")
    frameVVendedores.pack()

    #---funcion para salir de consulta de vendedores---
    def salirVVend():
        frameTVVend.destroy()
        frameVVendedores.destroy()

    conexionvVend=sqlite3.connect("inventario.db")

    cursorvVend=conexionvVend.cursor()

    cursorvVend.execute("SELECT * FROM DVendedores")

    tuplavVend=cursorvVend.fetchall()

    mlbV = MultiListbox(frameVVendedores, (('Codigo', 7), ('Nombre', 15), ('Apellido', 20),('Entrante', 10),('Telefono',10)))
    b = 0
    for j in tuplavVend:
        mlbV.insert(END, (j[0], j[1], j[2],j[3], j[4]))
        b += 1
    mlbV.grid(row=0, column=1)

    #-------los Botones---------

    bsalirVVend=Button(frameVVendedores, text="* SALIR *", command= salirVVend)
    bsalirVVend.grid(row=2, column=1, padx=10, pady=10)

#-------------------------Consulta de Proveedores-------------------------

def visualizacionProveedores():

    #---frame del titulo
    frameTVProv=Frame(fondo)
    labelTVProv=Label(frameTVProv, text="                    Proveedores Registrados                    ")
    labelTVProv.config(bg="#C4CF52", font=("Segoe Script", 18))
    labelTVProv.grid(row=1, column=1)
    frameTVProv.pack()

    #---frame del contenido---
    frameVProv=Frame(fondo)
    frameVProv.config(bg="#9FA7B3")
    frameVProv.pack()

    #---funcion para salir de consulta de proveedores---
    def salirVProv():
        frameTVProv.destroy()
        frameVProv.destroy()

    conexionvProv=sqlite3.connect("inventario.db")
    cursorvProv=conexionvProv.cursor()

    cursorvProv.execute("SELECT * FROM DProveedores")
    tuplavProv=cursorvProv.fetchall()

    mlb = MultiListbox(frameVProv, (('codigo', 7), ('NIT', 15), ('nombre', 20),('PBX',10),('Total saliente', 10)))
    b = 0
    for i in tuplavProv:
        mlb.insert(END, (i[0], i[1], i[2], i[3], i[4]))
        b += 1
    mlb.grid(row=0, column=1)
    
    #-------los Botones---------

    bsalirVProv=Button(frameVProv, text="* SALIR *", command= salirVProv)
    bsalirVProv.grid(row=1, column=1, padx=10, pady=10)
    
#-------------------------Consulta de productos registrados-------------------------

def visualizacionInventario():

    #---frame del titulo
    frameTVInv=Frame(fondo)
    labelTVInv=Label(frameTVInv, text="                             Inventario                             ")
    labelTVInv.config(bg="#C4CF52", font=("Segoe Script", 18))
    labelTVInv.grid(row=1, column=1)
    frameTVInv.pack()

    frameVInv=Frame(fondo)
    frameVInv.pack()

    #---frame del contenido---
    def salirVInv():
        frameTVInv.destroy()
        frameVInv.destroy()

    conexionVInv=sqlite3.connect("inventario.db")
    cursorVInv=conexionVInv.cursor()

    cursorVInv.execute("SELECT * FROM IInventario")
    tuplaVInv=cursorVInv.fetchall()

    mlbInv = MultiListbox(frameVInv, (('Codigo', 7), ('Descripcion', 30), ('Precio', 15),('Cantidad',8)))
    b = 0
    for k in tuplaVInv:
        mlbInv.insert(END, (k[0], k[1], k[2], k[3]))
        b += 1
    mlbInv.grid(row=0, column=1)

    #-------los Botones---------

    bsalirVInv=Button(frameVInv, text="* SALIR *", command= salirVInv)
    bsalirVInv.grid(row=1, column=1, padx=10, pady=10)

    #------ los label------------

#-------------------------Consulta de facturas de compras realizadas-------------------------

def visualizacionFacCompras():
    global Temp1
    
    #---frame del titulo---
    frameTVFacComp=Frame(fondo)
    labelTVFacComp=Label(frameTVFacComp, text="                      Facturas de Compras                      ")
    labelTVFacComp.config(bg="#C4CF52", font=("Segoe Script", 18))
    labelTVFacComp.grid(row=1, column=1)
    frameTVFacComp.pack()
   
    #---frame del contenido---
    frameVFacComp=Frame(fondo)
    frameVFacComp.place(x=37, y=362, width=740, height=260)
    Temp1 = 0
    
    #---funcion para salir de consulta de facturas de compras---
    def salirVFacComp():
        frameTVFacComp.destroy()
        frameVFacComp.destroy()

    conexionBuscar = sqlite3.connect("inventario.db")

    cursor_BusRefCom= conexionBuscar.cursor()
    cursor_tableDOrdV=conexionBuscar.cursor()
    cursor_tableDOrdD=conexionBuscar.cursor()

    #----------buscar datos
    def buscar_RefComp():
        global Temp1
        
        RefCompSave = RefComp.get()

        cursor_BusRefCom.execute("SELECT RefComp FROM DOrdenVista")
        listRefComp = cursor_BusRefCom.fetchall()

        for z in listRefComp:
                
            if z[0] == RefCompSave:
                Temp1 = z[0]
                #--------------------muestra general 
                lbVistaGen = Label(frameVFacComp, text='Vista general')
                lbVistaGen.place(x=20, y=34, width=740, height=15)


                QueryMostrarV="SELECT NumComp, Cod_Proveedor, CompNIT, CompNOM, CodTotal FROM DOrdenVista WHERE RefComp = ?"
                cursor_tableDOrdV.execute(QueryMostrarV, (z[0],))
                listDOrdenVista = cursor_tableDOrdV.fetchall()
                    
                MultilistDOrdenVista = MultiListboxCompV(frameVFacComp, (('Numero de compra', 10), ('Codigo de Proveedor', 10), ('NIT de compra', 10), ('Nombre de compra', 20), ('Total de la factura', 10)))
                        
                for t in listDOrdenVista:
                    MultilistDOrdenVista.insert(END, (t[0], t[1], t[2], t[3], t[4]))       
                MultilistDOrdenVista.place(x=100, y=52)

                    #-----------------Muestra detalle
                lbVistaDet = Label(frameVFacComp, text='Vista detallada')
                lbVistaDet.place(x=20, y=110, width=740, height=15)
                
                QueryMostrarD="SELECT LineNum, ItemCode, ItemName, Cantidad, PreioUnit, DocTotal FROM DOrdenDetalle WHERE RefComp = ?"
                cursor_tableDOrdD.execute(QueryMostrarD, (z[0],))
                listDOrdenDetalle = cursor_tableDOrdD.fetchall()

                MultilistDOrdenDetalle = MultiListboxCompD(frameVFacComp, (('Numero de Linea', 5), ("Codigo de producto",5), ("nombre de producto", 10), ("Cantidad de producto", 8), ("precio unitario", 10), ("Total del producto", 15)))

                for tt in listDOrdenDetalle:
                    MultilistDOrdenDetalle.insert(END, (tt[0], tt[1], tt[2], tt[3], tt[4], tt[5]))
                MultilistDOrdenDetalle.place(x=55, y=128)

                #---funcion para limpiar campos---
                def borrar_RefComp():
                    global Temp1
            
                    MultilistDOrdenVista.destroy()
                    MultilistDOrdenDetalle.destroy()
                    lbVistaGen.destroy()
                    lbVistaDet.destroy()
                    Temp1 = 0

                bbuscarRef_Comp=Button(frameVFacComp, text="* BORRAR *", command= borrar_RefComp)
                bbuscarRef_Comp.grid(row=0, column=3, padx=10, pady=10)
                        
        if Temp1 != RefCompSave:
            avisoerrorComp()

    #------label para refComp ------------------------
    lbRefComp = Label(frameVFacComp, text="Ref. de factura")
    lbRefComp.grid(row=0, column=0, padx=10, pady=5)

    RefComp = IntVar()
    EbRefComp = Entry(frameVFacComp, textvariable = RefComp)
    EbRefComp.grid(row = 0,column = 1, padx=20, pady=10)

    #-------los Botones---------
    bbuscarRef_Comp=Button(frameVFacComp, text="* BUSCAR *", command= buscar_RefComp)
    bbuscarRef_Comp.grid(row=0, column=2, padx=10, pady=10)

    bsalirVFacComp=Button(frameVFacComp, text="* SALIR *", command= salirVFacComp)
    bsalirVFacComp.grid(row=0, column=4, padx=10, pady=10)

#------------------------------Consulta de facturas de ventas extendidas-------------------------

def visualizacionFacVentas():

    #---frame del titulo---
    frameTVFacVent=Frame(fondo)
    labelTVFacVent=Label(frameTVFacVent, text="                        Facturas de Ventas                        ")
    labelTVFacVent.config(bg="#C4CF52", font=("Segoe Script", 18))
    labelTVFacVent.grid(row=1, column=1)
    frameTVFacVent.pack()

    #---frame del contenido---
    frameVFacVent=Frame(fondo)
    frameVFacVent.place(x=37, y=362, width=740, height=260)

    #---funcion para salir de consulta de facturas de ventas---
    def salirVFacVent():
        frameTVFacVent.destroy()
        frameVFacVent.destroy()

    global Temp21
    Temp21 = 0
    conexionBuscarV= sqlite3.connect("inventario.db")
    cursorBuscarVent1= conexionBuscarV.cursor()
    cursorBuscarVent2=conexionBuscarV.cursor()
    cursorBuscarVent3= conexionBuscarV.cursor()

    #---funcion para buscar las facturas---
    def buscarRefFac():
        global Temp21
        RefFacSave = RefFac.get()
        cursorBuscarVent1.execute("SELECT RefFac FROM VFacVista")
        listBuscarVent= cursorBuscarVent1.fetchall()
       
        for f in listBuscarVent:
            if f[0] == RefFacSave:
                Temp21 = f[0]
                lbtitle1 = Label(frameVFacVent, text='Vista general')
                lbtitle1.place(x=20, y=32, width=740, height=15)

                QueryMostrarFac1="SELECT NumFac, Cod_Cliente, FacNIT, FacNOM, FacCUI, Cod_Vendedor, DocTotal  FROM VFacVista WHERE RefFac = ?"
                cursorBuscarVent2.execute(QueryMostrarFac1, (f[0],))
                listBuscarVent2 = cursorBuscarVent2.fetchall()

                MultilistVFacVista1 = MultiListboxCompV(frameVFacVent, (('Numero de factura', 10), ('Codigo de cliente', 10), ('NIT de factura', 10), ('Nombre de factura', 20), ('Cuidad', 10), ('Codigo de vendedor', 10), ('Total de la factura', 10)))
                
                for ff in listBuscarVent2:
                    MultilistVFacVista1.insert(END, (ff[0], ff[1], ff[2], ff[3], ff[4], ff[5], ff[6]))
                MultilistVFacVista1.place(x=10, y=50)


                lbtitle2 = Label(frameVFacVent, text='Vista detallada')
                lbtitle2.place(x=20, y=108, width=740, height=15)

                QueryMostrarFac2="SELECT LineNum, ItemCode, ItemName, Cantidad, PrecioUnit, DocTotal FROM VfacDetalle WHERE RefFac = ?"
                cursorBuscarVent3.execute(QueryMostrarFac2, (f[0],))
                listBuscarVent3 = cursorBuscarVent3.fetchall()

                MultilistVFacVista2 = MultiListboxCompD(frameVFacVent, (('Numero de linea', 8), ('Codigo de producto', 10), ('Nombre de producto', 20), ('Cantidad', 10), ('Precio Unidad', 8), ('Precio total', 8)))
                
                for fff in listBuscarVent3:
                    MultilistVFacVista2.insert(END, (fff[0], fff[1], fff[2], fff[3], fff[4], fff[5]))
                MultilistVFacVista2.place(x=90, y=125)
                
                #---funcion para limpiar campos---
                def borrarRefFac():
                    global Temp21
                    MultilistVFacVista1.destroy()
                    MultilistVFacVista2.destroy()
                    lbtitle1.destroy()
                    lbtitle2.destroy()
                    Temp21 = 0
                bBorrarVFacVent=Button(frameVFacVent, text="* BORRAR *", command= borrarRefFac)
                bBorrarVFacVent.grid(row=0, column=3)

        if Temp21 == 0:
            avisoerrorComp()

    RefFac = IntVar()
    EbRefFac = Entry(frameVFacVent, textvariable = RefFac)
    EbRefFac.grid(row = 0,column = 1, padx=20, pady=10)

    #-------------------los Botones--------------

    lbRefFac = Label(frameVFacVent, text="Ref. de factura")
    lbRefFac.grid(row=0, column=0, padx=10, pady=5)

    bsalirVFacVent=Button(frameVFacVent, text="* BUSCAR *", command= buscarRefFac)
    bsalirVFacVent.grid(row=0, column=2, padx=10, pady=10)

    bsalirVFacVent=Button(frameVFacVent, text="* SALIR *", command= salirVFacVent)
    bsalirVFacVent.grid(row=0, column=4, padx=10, pady=10)

#-------------------------Compras-------------------------

def FacCompras():

    frameTFComp=Frame(fondo) #frame del titutlo
    labelTFComp=Label(frameTFComp, text="                              Compras                              ")
    labelTFComp.config(bg="#DC5252", font=("Segoe Script", 18))
    labelTFComp.grid(row=1, column=1)
    frameTFComp.pack()

    frameFacComp=Frame(fondo) #frame del contenido
    frameFacComp.pack()

    #----- algunas variables----- 
    codprovFC=IntVar()
    varCodProd1=IntVar()
    varCodProd2=IntVar()
    varCodProd3=IntVar()
    varCodProd4=IntVar()
    RefFacFC=IntVar()
    NumFacFC=IntVar()

    #---funcion para salir del control de compras---
    def salirFacComp():

        global contadora1, contadora2, contadora3, contadora4

        contadora1 = 0
        contadora2 = 0
        contadora3 = 0
        contadora4 = 0

        frameTFComp.destroy()
        frameFacComp.destroy()

    #---ventana emergente de error---
    def aviso1FC():
        messagebox.showwarning("!Error¡","¡Proveedor no encontrado!")

    #---busqueda del proveedor---
    def busquedaprov():

        global busquedaInv

        busquedaInv=codprovFC.get()

        conexionInv=sqlite3.connect("inventario.db") 
        cursor1inv=conexionInv.cursor()
        cursor2inv=conexionInv.cursor()

        cursor1inv.execute("SELECT Cod_Proveedor FROM DProveedores")
        tuplaInv=cursor1inv.fetchall()

        bca=0
        for abc in tuplaInv:
            if abc[0] == busquedaInv:
                bca += 1

                global subtotalFacComp2, subtotalFacComp1, subtotalFacComp3, subtotalFacComp4

                cursor2inv.execute("SELECT * FROM DProveedores")
                tupla2Inv=cursor2inv.fetchall()   

                #------------datos del proveedor---------------

                lbFCN=Listbox(frameFacComp)
                lbFCN.insert(0,tupla2Inv[busquedaInv-1][1])
                lbFCN.config(width="18", height="1")
                lbFCN.grid(row=2, column=3)

                lbFCNom=Listbox(frameFacComp)
                lbFCNom.insert(0,tupla2Inv[busquedaInv-1][2])
                lbFCNom.config(width="18", height="1")
                lbFCNom.grid(row=3, column=3)

                lbFCPbx=Listbox(frameFacComp)
                lbFCPbx.insert(0,tupla2Inv[busquedaInv-1][3])
                lbFCPbx.config(width="18", height="1")
                lbFCPbx.grid(row=4, column=3)

                def borrarInvCP(): # borrar los campos de datos del proveedor
                    lbFCN.destroy()
                    lbFCNom.destroy()
                    lbFCPbx.destroy()
                    codprovFC.set("")

                def agregarProd1(): # agregar el primer producto

                    global contador123, contadora1

                    contadora1 += 1

                    if contador123 == 0:

                        varCant1=IntVar()

                        def llamarInv1():# conectando con inventario
                            global varCodProd1Save
                            varCodProd1Save=varCodProd1.get()

                            conexionFacCompInv1=sqlite3.connect("inventario.db")
                            cursor1FacCompInv1=conexionFacCompInv1.cursor()
                            cursor2FacCompInv1=conexionFacCompInv1.cursor()

                            cursor1FacCompInv1.execute("SELECT ItemCode From IInventario")
                            lista1FacCompCP1=cursor1FacCompInv1.fetchall()

                            fed=0

                            def aviso1FCInv():
                                messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                            for q in lista1FacCompCP1:
                                
                                if str(q[0])==str(varCodProd1Save):
                                    fed += 1

                                    #---subtotal---
                                    def STotalFacComp1():

                                        global subtotalFacComp1, subtotalFacComp2, subtotalFacComp3, subtotalFacComp4, varCant1Save, varCant1Save2, variableCifrada21, variableCifrada22, varCant1Save3
                                        global variableCifrada32, variableCifrada31, varCodProd2Save3, varCodProd2Save4, variableCifrada41, variableCifrada42
                                        global varCant1Save4

                                        #---ventana emergente de error---
                                        def alerta3():
                                            messagebox.showwarning("!Error¡","¡Referencia de factura ya registrada!")

                                        #---ventana emergente de error---
                                        def alerta4():
                                            messagebox.showwarning("!Error¡","¡Numero de factura ya registrado!")

                                        def borrarProd1(): # limpiar datos de productos mostrados 
                                            global contador123, subtotalFacComp1, contadora1
                                            entryCompCP1.destroy()
                                            lbFCInv1Pre1.destroy()
                                            lbFCInv1Nom1.destroy()
                                            eCompCan1.destroy()
                                            bBuscarFC1.destroy()
                                            b1CalSTot1.destroy()
                                            lbFCSTot1.destroy()

                                            subtotalFacComp1=0

                                            contadora1 = 0

                                        #---total final---
                                        def totalfinal():
                                            global subtotalFacComp2, subtotalFacComp1, subtotalFacComp3, subtotalFacComp4
                                            sumatotalfinal=(subtotalFacComp1+subtotalFacComp2+subtotalFacComp3+subtotalFacComp4) # total comprado

                                            #---registro de la compra---
                                            def regFacComp():

                                                #--- insertar datos a la tabla DOrdenVista
                                                NumCompFCSave=NumFacFC.get()
                                                RefCompFCSave=RefFacFC.get()
                                                
                                                conexionSegura=sqlite3.connect("inventario.db")
                                                cursor1FacCompReg=conexionSegura.cursor()
                                                cursor2FacCompReg=conexionSegura.cursor()

                                                cursor1FacCompReg.execute("SELECT RefComp FROM DOrdenVista")
                                                lista1RefComp=cursor1FacCompReg.fetchall()

                                                cursor2FacCompReg.execute("SELECT NumComp FROM DOrdenVista")
                                                lista2RefComp=cursor2FacCompReg.fetchall()

                                                mmm=0
                                                for o in lista1RefComp:
                                                    if o[0]==NumCompFCSave:
                                                        alerta3()
                                                        mmm += 1
                                                        
                                                    if mmm==0:
                                                        for r in lista2RefComp:
                                                            if r[0]==RefCompFCSave:
                                                                alerta4()
                                                                mmm += 1
                                                if mmm == 0:
                                                    global varCodProd1Save, varCodProd2Save, varCodProd2Save3, varCodProd2Save4
                                                    global subtotalFacComp2, subtotalFacComp1, subtotalFacComp3, subtotalFacComp4
                                                    global varCant1Save, varCant1Save2, varCant1Save3, varCant1Save4
                                                    global variableCifrada21, variableCifrada22, variableCifrada32, variableCifrada31, variableCifrada41, variableCifrada42
                                                    global busquedaInv

                                                    avisoexitoso1()

                                                    conexionSegura1=sqlite3.connect("inventario.db")
                                                    cursor3FacCompReg=conexionSegura1.cursor()

                                                    tupla1FacComp=[
                                                        (NumCompFCSave, RefCompFCSave,  busquedaInv, tupla2Inv[busquedaInv-1][1], tupla2Inv[busquedaInv-1][2], sumatotalfinal)
                                                    ]

                                                    cursor3FacCompReg.executemany("INSERT INTO DOrdenVista VALUES (?,?,?,?,?,?)", tupla1FacComp)   

                                                    conexionSegura1.commit()
                                                    conexionSegura1.close()

                                                    #--- insertar datos en la tabla DOrdenDetalle---
                                                    #--- insertando el producto 1---
                                                    if contadora1 == 1:

                                                        conexionCifrada1=sqlite3.connect("inventario.db")
                                                        cursor4FacCompReg=conexionCifrada1.cursor()
                                                        cursorInvComp=conexionCifrada1.cursor()
                                                        cursorInvCompBusc=conexionCifrada1.cursor()
                                                        cursorInvCompUpd=conexionCifrada1.cursor()

                                                        #---lista para guardar los datos del producto 1---
                                                        tupla2FacComp=[
                                                            (1, NumCompFCSave, varCodProd1Save, lista2FacCompCP1[varCodProd1Save-1][1], varCant1Save, lista2FacCompCP1[varCodProd1Save-1][2], subtotalFacComp1)
                                                        ]

                                                        cursor4FacCompReg.executemany("INSERT INTO DOrdenDetalle VALUES(?,?,?,?,?,?,?)", tupla2FacComp)
                                                        #-------------------actualizar inventario-----
                                                        cursorInvComp.execute("SELECT ItemCode FROM IInventario")
                                                        tuplaCantProd = cursorInvComp.fetchall()
                                                        varCodProd1SaveTemp = varCodProd1Save

                                                        query= """
                                                        SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                        """

                                                        cursorInvCompBusc.execute(query, (varCodProd1SaveTemp,))
                                                        CantInv = cursorInvCompBusc.fetchall()
                                                        sumaCantComp = CantInv[0][0] + varCant1Save

                                                        for ppp in tuplaCantProd:
                                                            if str(ppp[0]) == str(varCodProd1Save):
                                                                query1 = """
                                                                UPDATE IInventario SET Cantidad = :sumaCantComp WHERE ItemCode = :varCodProd1SaveTemp
                                                                """
                                                                cursorInvCompUpd.execute(query1, {'sumaCantComp':sumaCantComp, 'varCodProd1SaveTemp':varCodProd1SaveTemp})

                                                        conexionCifrada1.commit()
                                                        conexionCifrada1.close()

                                                    #---insertando el producto 2---
                                                    if contadora2 ==1 :

                                                        conexionCifrada2=sqlite3.connect("inventario.db")
                                                        cursor5FacCompReg=conexionCifrada2.cursor()
                                                        cursorInvComp2=conexionCifrada2.cursor()
                                                        cursorInvCompBusc2=conexionCifrada2.cursor()
                                                        cursorInvCompUpd2=conexionCifrada2.cursor()

                                                        #---lista para guardar datos del producto 2---
                                                        tupla3FacComp=[
                                                            (2, NumCompFCSave, varCodProd2Save, variableCifrada21, varCant1Save2,variableCifrada22, subtotalFacComp2)
                                                        ]

                                                        cursor5FacCompReg.executemany("INSERT INTO DOrdenDetalle VALUES(?,?,?,?,?,?,?)", tupla3FacComp)
                                                        #----------actualizar inventario--------------
                                                        cursorInvComp2.execute("SELECT ItemCode FROM IInventario")
                                                        tuplaCantProd2 = cursorInvComp2.fetchall()
                                                        varCodProd2SaveTemp = varCodProd2Save

                                                        query21= """
                                                        SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                        """

                                                        cursorInvCompBusc2.execute(query21, (varCodProd2SaveTemp,))
                                                        CantInv2 = cursorInvCompBusc2.fetchall()
                                                        sumaCantComp2 = CantInv2[0][0] + varCant1Save2

                                                        for pppp in tuplaCantProd2:
                                                            if str(pppp[0]) == str(varCodProd2Save):
                                                                query22 = """
                                                                UPDATE IInventario SET Cantidad = :sumaCantComp2 WHERE ItemCode = :varCodProd2SaveTemp
                                                                """
                                                                cursorInvCompUpd2.execute(query22, {'sumaCantComp2':sumaCantComp2, 'varCodProd2SaveTemp':varCodProd2SaveTemp})

                                                        conexionCifrada2.commit()
                                                        conexionCifrada2.close()

                                                    #--- producto 3---
                                                    if contadora3 ==1 :
                                                    
                                                        conexionCifrada3=sqlite3.connect("inventario.db")
                                                        cursor6FacCompReg=conexionCifrada3.cursor()
                                                        cursorInvComp3=conexionCifrada3.cursor()
                                                        cursorInvCompBusc3=conexionCifrada3.cursor()
                                                        cursorInvCompUpd3=conexionCifrada3.cursor()

                                                        #---lista para guardar los datos del producto 3
                                                        tupla4FacComp=[
                                                            (3, NumCompFCSave, varCodProd2Save3, variableCifrada31, varCant1Save3,variableCifrada32,subtotalFacComp3)
                                                        ]
                                                        
                                                        cursor6FacCompReg.executemany("INSERT INTO DOrdenDetalle VALUES(?,?,?,?,?,?,?)", tupla4FacComp)
                                                        #----------actualizar inventario--------------
                                                        cursorInvComp3.execute("SELECT ItemCode FROM IInventario")
                                                        tuplaCantProd3 = cursorInvComp3.fetchall()
                                                        varCodProd3SaveTemp = varCodProd2Save3

                                                        query31= """
                                                        SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                        """

                                                        cursorInvCompBusc3.execute(query31, (varCodProd3SaveTemp,))
                                                        CantInv3 = cursorInvCompBusc3.fetchall()
                                                        sumaCantComp3 = CantInv3[0][0] + varCant1Save3

                                                        for ppppp in tuplaCantProd3:
                                                            if str(ppppp[0]) == str(varCodProd2Save3):
                                                                query32 = """
                                                                UPDATE IInventario SET Cantidad = :sumaCantComp3 WHERE ItemCode = :varCodProd3SaveTemp
                                                                """
                                                                cursorInvCompUpd3.execute(query32, {'sumaCantComp3':sumaCantComp3, 'varCodProd3SaveTemp':varCodProd3SaveTemp})

                                                        conexionCifrada3.commit()
                                                        conexionCifrada3.close()

                                                    #---producto 4---
                                                    if contadora4 == 1:

                                                        conexionCifrada4=sqlite3.connect("inventario.db")
                                                        cursor7FacCompReg=conexionCifrada4.cursor()
                                                        cursorInvComp4=conexionCifrada4.cursor()
                                                        cursorInvCompBusc4=conexionCifrada4.cursor()
                                                        cursorInvCompUpd4=conexionCifrada4.cursor()

                                                        #---lista para guardas datos del producto 4
                                                        tupla5FacComp=[
                                                            (4, NumCompFCSave, varCodProd2Save4, variableCifrada41,varCant1Save4,variableCifrada42, subtotalFacComp4)
                                                        ]

                                                        cursor7FacCompReg.executemany("INSERT INTO DOrdenDetalle VALUES(?,?,?,?,?,?,?)", tupla5FacComp)
                                                        #----------actualizar inventario--------------
                                                        cursorInvComp4.execute("SELECT ItemCode FROM IInventario")
                                                        tuplaCantProd4 = cursorInvComp4.fetchall()
                                                        varCodProd4SaveTemp = varCodProd2Save4

                                                        query41= """
                                                        SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                        """

                                                        cursorInvCompBusc4.execute(query41, (varCodProd4SaveTemp,))
                                                        CantInv4 = cursorInvCompBusc4.fetchall()
                                                        sumaCantComp4 = CantInv4[0][0] + varCant1Save4

                                                        for pppppp in tuplaCantProd4:
                                                            if str(pppppp[0]) == str(varCodProd2Save4):
                                                                query42 = """
                                                                UPDATE IInventario SET Cantidad = :sumaCantComp4 WHERE ItemCode = :varCodProd4SaveTemp
                                                                """
                                                                cursorInvCompUpd4.execute(query42, {'sumaCantComp4':sumaCantComp4, 'varCodProd4SaveTemp':varCodProd4SaveTemp})

                                                        conexionCifrada4.commit()
                                                        conexionCifrada4.close()   

                                                    scactualizar=(contadora1+contadora2+contadora3+contadora4)

                                                    #--- actualizar el total saliente----
                                                    if scactualizar>0:

                                                        conexionUDFC=sqlite3.connect("inventario.db")
                                                        cursorUPFC1=conexionUDFC.cursor()
                                                        cursorUPFC2=conexionUDFC.cursor()
                                                        cursorUPFC3=conexionUDFC.cursor()

                                                        cursorUPFC1.execute("SELECT Cod_Proveedor FROM DProveedores")
                                                        tuplaUPFC1 = cursorUPFC1.fetchall()
                                                        busquedaInvTemp = busquedaInv

                                                        queryUDFC1= """
                                                        SELECT TotalSaliente FROM DProveedores WHERE Cod_Proveedor = ?
                                                        """

                                                        cursorUPFC2.execute(queryUDFC1, (busquedaInvTemp,))
                                                        tuplaUDFC2 = cursorUPFC2.fetchall()
                                                        sumaTSal = tuplaUDFC2[0][0] + sumatotalfinal

                                                        for hh1 in tuplaUPFC1:
                                                            if str(hh1[0]) == str(busquedaInv):
                                                                queryUDFC2 = """
                                                                UPDATE DProveedores SET TotalSaliente = :sumaTSal WHERE Cod_Proveedor = :busquedaInvTemp
                                                                """
                                                                cursorUPFC3.execute(queryUDFC2, {'sumaTSal':sumaTSal, 'busquedaInvTemp':busquedaInvTemp})

                                                        conexionUDFC.commit()
                                                        conexionUDFC.close()

                                            #---listbox muestra del total sumado---
                                            lbSumaTotalFinal=Listbox(frameFacComp)
                                            lbSumaTotalFinal.insert(0,sumatotalfinal)
                                            lbSumaTotalFinal.config(width="8", height="1")
                                            lbSumaTotalFinal.grid(row=11, column=7)

                                            #---boton para realizar la compra
                                            bcomprar=Button(frameFacComp, text="* COMPRAR *", command=regFacComp)
                                            bcomprar.grid(row=11, column=5)
                                        
                                        #--- boton de eliminar un producto
                                        b1BorProd=Button(frameFacComp, text="-", command = borrarProd1)
                                        b1BorProd.grid(row=7, column=1)

                                        varCant1Save=varCant1.get()

                                        subtotalFacComp1=(varCant1Save*lista2FacCompCP1[varCodProd1Save-1][2])
                                        
                                        lbFCSTot1=Listbox(frameFacComp)
                                        lbFCSTot1.insert(0,subtotalFacComp1)
                                        lbFCSTot1.config(width="8", height="1")
                                        lbFCSTot1.grid(row=7, column=7)

                                        #---boton para sumar los subtotales
                                        bsumatotal=Button(frameFacComp, text="SUMAR", command=totalfinal)
                                        bsumatotal.grid(row=11, column=8)

                                    cursor2FacCompInv1.execute("SELECT * FROM IInventario")
                                    lista2FacCompCP1=cursor2FacCompInv1.fetchall()

                                    #---listbox para mostrar el precio del producto buscado---
                                    lbFCInv1Pre1=Listbox(frameFacComp)
                                    lbFCInv1Pre1.insert(0,lista2FacCompCP1[varCodProd1Save-1][2])
                                    lbFCInv1Pre1.config(width="18", height="1")
                                    lbFCInv1Pre1.grid(row=7, column=3)

                                    #---listbox para mostrar el nombre del producto buscado---
                                    lbFCInv1Nom1=Listbox(frameFacComp)
                                    lbFCInv1Nom1.insert(0,lista2FacCompCP1[varCodProd1Save-1][1])
                                    lbFCInv1Nom1.config(width="18", height="1")
                                    lbFCInv1Nom1.grid(row=7, column=4)

                                    b1CalSTot1=Button(frameFacComp, text="Calcular", command=STotalFacComp1)
                                    b1CalSTot1.grid(row=7, column=6)

                            if fed==0:
                                aviso1FCInv()

                        entryCompCP1=Entry(frameFacComp, textvariable=varCodProd1)
                        entryCompCP1.grid(row=7, column=2, padx=10, pady=5)

                        eCompCan1=Entry(frameFacComp, textvariable=varCant1)
                        eCompCan1.grid(row=7, column=5, padx=10, pady=5)
                        contador123 += 1 
                    
                        bBuscarFC1=Button(frameFacComp, text="Buscar", command=llamarInv1)
                        bBuscarFC1.grid(row=7, column=8)

                #---agregar un segundo producto---
                def agregarProd2():

                    global contador1234, contadora2

                    contadora2 += 1

                    if contador1234 == 0:

                        varCant2=IntVar()

                        #---llamar a inventario---
                        def llamarInv2():
                            global varCodProd2Save
                            varCodProd2Save=varCodProd2.get()

                            conexionFacCompInv2=sqlite3.connect("inventario.db")
                            cursor1FacCompInv2=conexionFacCompInv2.cursor()
                            cursor2FacCompInv2=conexionFacCompInv2.cursor()

                            cursor1FacCompInv2.execute("SELECT ItemCode From IInventario")
                            lista1FacCompCP2=cursor1FacCompInv2.fetchall()

                            feda=0

                            #---ventana emergente de error---
                            def aviso1FCInv2():
                                messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                            for p in lista1FacCompCP2:
                                
                                if str(p[0])==str(varCodProd2Save):
                                    feda += 1

                                    #---subtotal---
                                    def STotalFacComp2():
                                        global subtotalFacComp2, variableCifrada21, variableCifrada22, varCant1Save2

                                        #---funcion de limpiar campos del producto buscado---
                                        def borrarProd2():
                                            global contador1234, subtotalFacComp2, contadora2
                                            entryCompCP2.destroy()
                                            lbFCInv1Pre2.destroy()
                                            lbFCInv1Nom2.destroy()
                                            eCompCan2.destroy()
                                            bBuscarFC2.destroy()
                                            b1CalSTot2.destroy()
                                            lbFCSTot2.destroy()
                                            subtotalFacComp2=0

                                            contadora2 = 0

                                        varCant1Save2=varCant2.get()

                                        variableCifrada21=lista2FacCompCP2[varCodProd2Save-1][1]
                                        variableCifrada22=lista2FacCompCP2[varCodProd2Save-1][2]

                                        subtotalFacComp2=(varCant1Save2*lista2FacCompCP2[varCodProd2Save-1][2])
                                        
                                        lbFCSTot2=Listbox(frameFacComp)
                                        lbFCSTot2.insert(0,subtotalFacComp2)
                                        lbFCSTot2.config(width="8", height="1")
                                        lbFCSTot2.grid(row=8, column=7)

                                        b1BorProd2=Button(frameFacComp, text="-", command = borrarProd2)
                                        b1BorProd2.grid(row=8, column=1)

                                    cursor2FacCompInv2.execute("SELECT * FROM IInventario")
                                    lista2FacCompCP2=cursor2FacCompInv2.fetchall()

                                    lbFCInv1Pre2=Listbox(frameFacComp)
                                    lbFCInv1Pre2.insert(0,lista2FacCompCP2[varCodProd2Save-1][2])
                                    lbFCInv1Pre2.config(width="18", height="1")
                                    lbFCInv1Pre2.grid(row=8, column=3)

                                    lbFCInv1Nom2=Listbox(frameFacComp)
                                    lbFCInv1Nom2.insert(0,lista2FacCompCP2[varCodProd2Save-1][1])
                                    lbFCInv1Nom2.config(width="18", height="1")
                                    lbFCInv1Nom2.grid(row=8, column=4)

                                    b1CalSTot2=Button(frameFacComp, text="Calcular", command=STotalFacComp2)
                                    b1CalSTot2.grid(row=8, column=6)

                            if feda==0:
                                aviso1FCInv2()

                        entryCompCP2=Entry(frameFacComp, textvariable=varCodProd2)
                        entryCompCP2.grid(row=8, column=2, padx=10, pady=5)

                        eCompCan2=Entry(frameFacComp, textvariable=varCant2)
                        eCompCan2.grid(row=8, column=5, padx=10, pady=5)
                        contador1234 += 1 
                    
                        bBuscarFC2=Button(frameFacComp, text="Buscar", command=llamarInv2)
                        bBuscarFC2.grid(row=8, column=8)

                #---agregar un tercer producto---
                def agregarProd3():

                    global contador12345, contadora3

                    contadora3 += 1
                    if contador12345 == 0:

                        varCant3=IntVar()

                        #---llamar a inventario---
                        def llamarInv3():

                            global varCodProd2Save3
                            varCodProd2Save3=varCodProd3.get()

                            conexionFacCompInv3=sqlite3.connect("inventario.db")
                            cursor1FacCompInv3=conexionFacCompInv3.cursor()
                            cursor2FacCompInv3=conexionFacCompInv3.cursor()

                            cursor1FacCompInv3.execute("SELECT ItemCode From IInventario")
                            lista1FacCompCP3=cursor1FacCompInv3.fetchall()

                            fedb=0

                            #---ventana emergente de error---
                            def aviso1FCInv3():
                                messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                            for ee in lista1FacCompCP3:
                                
                                if str(ee[0])==str(varCodProd2Save3):
                                    fedb += 1

                                    #---subtotal
                                    def STotalFacComp3():
                                        global subtotalFacComp3, varCant1Save3, variableCifrada32, variableCifrada31

                                        #---limpiar campos del producto buscado---
                                        def borrarProd3():
                                            global contador12345, subtotalFacComp3, contadora3
                                            entryCompCP3.destroy()
                                            lbFCInv1Pre3.destroy()
                                            lbFCInv1Nom3.destroy()
                                            eCompCan3.destroy()
                                            bBuscarFC3.destroy()
                                            b1CalSTot3.destroy()
                                            lbFCSTot3.destroy()
                                            subtotalFacComp3=0

                                            contador12345 = contador12345 - 1

                                            contadora3 = 0

                                        varCant1Save3=varCant3.get()

                                        variableCifrada31=lista2FacCompCP3[varCodProd2Save3-1][1]
                                        variableCifrada32=lista2FacCompCP3[varCodProd2Save3-1][2]

                                        subtotalFacComp3=(varCant1Save3*lista2FacCompCP3[varCodProd2Save3-1][2])
                                        
                                        lbFCSTot3=Listbox(frameFacComp)
                                        lbFCSTot3.insert(0,subtotalFacComp3)
                                        lbFCSTot3.config(width="8", height="1")
                                        lbFCSTot3.grid(row=9, column=7)

                                        b1BorProd3=Button(frameFacComp, text="-", command = borrarProd3)
                                        b1BorProd3.grid(row=9, column=1)

                                    cursor2FacCompInv3.execute("SELECT * FROM IInventario")
                                    lista2FacCompCP3=cursor2FacCompInv3.fetchall()

                                    lbFCInv1Pre3=Listbox(frameFacComp)
                                    lbFCInv1Pre3.insert(0,lista2FacCompCP3[varCodProd2Save3-1][2])
                                    lbFCInv1Pre3.config(width="18", height="1")
                                    lbFCInv1Pre3.grid(row=9, column=3)

                                    lbFCInv1Nom3=Listbox(frameFacComp)
                                    lbFCInv1Nom3.insert(0,lista2FacCompCP3[varCodProd2Save3-1][1])
                                    lbFCInv1Nom3.config(width="18", height="1")
                                    lbFCInv1Nom3.grid(row=9, column=4)

                                    b1CalSTot3=Button(frameFacComp, text="Calcular", command=STotalFacComp3)
                                    b1CalSTot3.grid(row=9, column=6)

                            if fedb==0:
                                aviso1FCInv3()

                        entryCompCP3=Entry(frameFacComp, textvariable=varCodProd3)
                        entryCompCP3.grid(row=9, column=2, padx=10, pady=5)

                        eCompCan3=Entry(frameFacComp, textvariable=varCant3)
                        eCompCan3.grid(row=9, column=5, padx=10, pady=5)
                        contador12345 += 1 
                    
                        bBuscarFC3=Button(frameFacComp, text="Buscar", command=llamarInv3)
                        bBuscarFC3.grid(row=9, column=8)

                #---agregar un cuarto producto---
                def agregarProd4():

                    global contador123456, contadora4

                    contadora4 +=1

                    if contador123456 == 0:

                        varCant4=IntVar()

                        #---llamar a inventario---
                        def llamarInv4():
                            global varCodProd2Save4

                            varCodProd2Save4=varCodProd4.get()

                            conexionFacCompInv4=sqlite3.connect("inventario.db")
                            cursor1FacCompInv4=conexionFacCompInv4.cursor()
                            cursor2FacCompInv4=conexionFacCompInv4.cursor()

                            cursor1FacCompInv4.execute("SELECT ItemCode From IInventario")
                            lista1FacCompCP4=cursor1FacCompInv4.fetchall()

                            fedc=0

                            #---ventana emergente de error---
                            def aviso1FCInv4():
                                messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                            for rr in lista1FacCompCP4:
                                
                                if str(rr[0])==str(varCodProd2Save4):
                                    fedc += 1

                                    #---subtotal---
                                    def STotalFacComp4():
                                        global subtotalFacComp4, variableCifrada41, variableCifrada42, varCant1Save4

                                        #---limpiar campos del producto buscado---
                                        def borrarProd4():
                                            global contador123456, subtotalFacComp4, contadora4
                                            entryCompCP4.destroy()
                                            lbFCInv1Pre4.destroy()
                                            lbFCInv1Nom4.destroy()
                                            eCompCan4.destroy()
                                            bBuscarFC4.destroy()
                                            b1CalSTot4.destroy()
                                            lbFCSTot4.destroy()
                                            subtotalFacComp4=0

                                            contador123456 = contador123456 - 1

                                            contadora4 = 0

                                        varCant1Save4=varCant4.get()

                                        variableCifrada41 = lista2FacCompCP4[varCodProd2Save4-1][1]
                                        variableCifrada42 = lista2FacCompCP4[varCodProd2Save4-1][2]

                                        subtotalFacComp4=(varCant1Save4*lista2FacCompCP4[varCodProd2Save4-1][2])
                                        
                                        lbFCSTot4=Listbox(frameFacComp)
                                        lbFCSTot4.insert(0,subtotalFacComp4)
                                        lbFCSTot4.config(width="8", height="1")
                                        lbFCSTot4.grid(row=10, column=7)

                                        b1BorProd4=Button(frameFacComp, text="-", command = borrarProd4)
                                        b1BorProd4.grid(row=10, column=1)

                                    cursor2FacCompInv4.execute("SELECT * FROM IInventario")
                                    lista2FacCompCP4=cursor2FacCompInv4.fetchall()

                                    lbFCInv1Pre4=Listbox(frameFacComp)
                                    lbFCInv1Pre4.insert(0,lista2FacCompCP4[varCodProd2Save4-1][2])
                                    lbFCInv1Pre4.config(width="18", height="1")
                                    lbFCInv1Pre4.grid(row=10, column=3)

                                    lbFCInv1Nom4=Listbox(frameFacComp)
                                    lbFCInv1Nom4.insert(0,lista2FacCompCP4[varCodProd2Save4-1][1])
                                    lbFCInv1Nom4.config(width="18", height="1")
                                    lbFCInv1Nom4.grid(row=10, column=4)

                                    b1CalSTot4=Button(frameFacComp, text="Calcular", command=STotalFacComp4)
                                    b1CalSTot4.grid(row=10, column=6)

                            if fedc==0:
                                aviso1FCInv4()

                        entryCompCP4=Entry(frameFacComp, textvariable=varCodProd4)
                        entryCompCP4.grid(row=10, column=2, padx=10, pady=5)

                        eCompCan4=Entry(frameFacComp, textvariable=varCant4)
                        eCompCan4.grid(row=10, column=5, padx=10, pady=5)
                        contador123456 += 1 
                    
                        bBuscarFC4=Button(frameFacComp, text="Buscar", command=llamarInv4)
                        bBuscarFC4.grid(row=10, column=8)

                lCod_prod=Label(frameFacComp, text="Codigo del producto")
                lCod_prod.grid(row=6, column=2, padx=10, pady=5)

                lpriceProd=Label(frameFacComp, text="Precio P/U")
                lpriceProd.grid(row=6, column=3, padx=10, pady=5)

                lItemNam=Label(frameFacComp, text="Descripcion")
                lItemNam.grid(row=6, column=4, padx=10, pady=5)

                lcantProd=Label(frameFacComp, text="Cantidad")
                lcantProd.grid(row=6, column=5, padx=10, pady=5)

                ltotalparcial=Label(frameFacComp, text="Sub-Total")
                ltotalparcial.grid(row=6, column=7, padx=10, pady=5)

                ltotal=Label(frameFacComp, text="TOTAL")
                ltotal.grid(row=11, column=6, padx=10, pady=5)

                bsalirFacComp=Button(frameFacComp, text="* BORRAR *", command=borrarInvCP)
                bsalirFacComp.grid(row=5, column=4, padx=10, pady=10)

                b1AgProd=Button(frameFacComp, text="+", command=agregarProd1)
                b1AgProd.grid(row=7, column=0)

                b2AgProd=Button(frameFacComp, text="+", command=agregarProd2)
                b2AgProd.grid(row=8, column=0)

                b3AgProd=Button(frameFacComp, text="+", command=agregarProd3)
                b3AgProd.grid(row=9, column=0)

                b4AgProd=Button(frameFacComp, text="+", command=agregarProd4)
                b4AgProd.grid(row=10, column=0)

        if bca==0:
            aviso1FC()

    #--------Los label-----------

    lCodProv=Label(frameFacComp, text="Codigo del Proveedor:")
    lCodProv.grid(row=1, column=2, sticky="e")

    lNitProv=Label(frameFacComp, text="Nit: ")
    lNitProv.grid(row=2, column=2, sticky="e")

    lNomProv=Label(frameFacComp, text="Nombre: ")
    lNomProv.grid(row=3, column=2, sticky="e")

    lPbxProv=Label(frameFacComp, text="PBX:")
    lPbxProv.grid(row=4, column=2, sticky="e")

    lRefFac=Label(frameFacComp, text="No. Factura:")
    lRefFac.grid(row=1, column=5)

    lCodLine=Label(frameFacComp, text="Ref Fac:")
    lCodLine.grid(row=2, column=5)

    #--------los entry-------------

    eCodProv=Entry(frameFacComp, textvariable= codprovFC)
    eCodProv.grid(row=1, column=3)

    eRefFac=Entry(frameFacComp, textvariable=NumFacFC)
    eRefFac.grid(row=2, column=6)

    eCodLine=Entry(frameFacComp, textvariable=RefFacFC)
    eCodLine.grid(row=1, column=6)

    #-------los Botones---------

    bBuscarFacComp=Button(frameFacComp, text="* BUSCAR *", command= busquedaprov)
    bBuscarFacComp.grid(row=1, column=4, padx=10, pady=10)

    bsalirFacComp=Button(frameFacComp, text="* SALIR *", command= salirFacComp)
    bsalirFacComp.grid(row=5, column=5, padx=10, pady=10)

#-------------------------ventas------------------------

def FacVentas():

    #---frame del titulo---
    frameTFVent=Frame(fondo)
    labelTFVent=Label(frameTFVent, text="                                Ventas                                ")
    labelTFVent.config(bg="#DC5252", font=("Segoe Script", 18))
    labelTFVent.grid(row=1, column=1)
    frameTFVent.pack()

    #---frame del contenido---
    frameFacVent=Frame(fondo)
    frameFacVent.pack()

    codProdFC=IntVar()
    cantProdFV=IntVar()

    codCliFV=IntVar()
    codVenFv=IntVar()

    codProdFC2=IntVar()
    cantProdFV2=IntVar()

    cantProdFV3=IntVar()
    codProdFC3=IntVar()

    codProdFC4=IntVar()
    cantProdFV4=IntVar()

    NumFacV=IntVar()
    RefFacV=IntVar()

    #---funcion para salir de ventas---
    def salirFacVent():

        global contadorb1, contadorb2, contadorb3, contadorb4
        
        contadorb1=0
        contadorb2=0
        contadorb3=0
        contadorb4=0
        
        frameTFVent.destroy()
        frameFacVent.destroy()

    #---ventana emergente de error---
    def alerta5():
        messagebox.showwarning("!Error¡","¡Cliente no encontrado!") 

    #---ventana emergente de exito---
    def alerta13():
        messagebox.showwarning("!Hecho¡","¡Venta realizada con exito!") 

    #---busqueda del cliente---
    def busquedaClientes():

        global codCliFVSave

        codCliFVSave=codCliFV.get()

        conexionFCCli=sqlite3.connect("inventario.db")
        cursorFCCli1=conexionFCCli.cursor()
        cursorFCCli2=conexionFCCli.cursor()

        cursorFCCli1.execute("SELECT Cod_Cliente FROM DClientes")
        tupla1FacVen1=cursorFCCli1.fetchall()

        bbb=0
        for ccc in tupla1FacVen1:
            if ccc[0]==codCliFVSave:
                bbb += 1

                cursorFCCli2.execute("SELECT * FROM DClientes")
                tupla1FacVen2=cursorFCCli2.fetchall()

                #--------------------------------datos del cliente------------------------------
                
                lbFCompNit=Listbox(frameFacVent)
                lbFCompNit.insert(0, tupla1FacVen2[codCliFVSave-1][6])
                lbFCompNit.config(width="18", height="1")
                lbFCompNit.grid(row=1, column=4)

                lbFCompNom=Listbox(frameFacVent)
                lbFCompNom.insert(0, tupla1FacVen2[codCliFVSave-1][2])
                lbFCompNom.config(width="18", height="1")
                lbFCompNom.grid(row=2, column=4)

                lbFCompCiu=Listbox(frameFacVent)
                lbFCompCiu.insert(0, tupla1FacVen2[codCliFVSave-1][5])
                lbFCompCiu.config(width="18", height="1")
                lbFCompCiu.grid(row=3, column=4)

                #---limpiar campos de cliente buscado---
                def borrarDatCli():
                    lbFCompNit.destroy()
                    lbFCompNom.destroy()
                    lbFCompCiu.destroy()
                    codCliFV.set("")

                #---ventana emergente de error---
                def alerta6():
                    messagebox.showwarning("!Error¡","¡Vendedor no encontrado!")

                #---busqueda del vendedor---
                def busquedaVend():

                    global codVenFvSave

                    codVenFvSave=codVenFv.get()

                    conexionFCVend=sqlite3.connect("inventario.db")
                    cursorFCVend1=conexionFCVend.cursor()
                    cursorFCVend2=conexionFCVend.cursor()

                    cursorFCVend1.execute("SELECT Cod_Vendedor FROM DVendedores")
                    listaFVVend1=cursorFCVend1.fetchall()

                    ddd=0
                    for eee in listaFVVend1:
                        if eee[0]==codVenFvSave:
                            ddd += 1

                            cursorFCVend2.execute("SELECT * FROM DVendedores")
                            listaFVVend2=cursorFCVend2.fetchall()

                            lbFCVenNom=Listbox(frameFacVent)
                            lbFCVenNom.insert(0, listaFVVend2[codVenFvSave-1][1])
                            lbFCVenNom.config(width="18", height="1")
                            lbFCVenNom.grid(row=2, column=6)

                            #---limpiar campos del vendedor---
                            def borrarDatVend():
                                lbFCVenNom.destroy()
                                codVenFv.set("")

                            #---agregar el primer producto---
                            def venderProd1():

                                global contadorabc, contadorb1

                                contadorb1 += 1

                                if contadorabc == 0:

                                    #---llamar a inventario---
                                    def llamar2Inv1():

                                        global codProdFCSave

                                        codProdFCSave=codProdFC.get()

                                        conexionFacVentInv1=sqlite3.connect("inventario.db")
                                        cursor1FacVentInv1=conexionFacVentInv1.cursor()
                                        cursor2FacVentInv1=conexionFacVentInv1.cursor()

                                        cursor1FacVentInv1.execute("SELECT ItemCode FROM IInventario")
                                        lista1FacVentInv1=cursor1FacVentInv1.fetchall()

                                        fed1 = 0

                                        #---ventana emergente de error---
                                        def alerta7():
                                            messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                                        for qq in lista1FacVentInv1:
                                            if str(qq[0]) == str(codProdFCSave):
                                                fed1 +=1

                                                #---subtotal---
                                                def STotalFacVent1():

                                                    global cantProdFVSave, subtotalFacVent1

                                                    #---limpiar campos del producto buscado---
                                                    def borrarProdFV1():
                                                        global subtotalFacVent1, contadorabc, contadorb1

                                                        subtotalFacVent1 = 0

                                                        eCodProdFC1.destroy()
                                                        eCantProdFC1.destroy()
                                                        lbSubTotalFV1.destroy()
                                                        lbPrecProdFV1.destroy()
                                                        lbDescFV1.destroy()
                                                        bCalcFV1.destroy()
                                                        bBuscarInvFC1.destroy()

                                                        contadorabc = contadorabc - 1

                                                        contadorb1 = 0

                                                    #---total sumado---
                                                    def totalfinalFV():

                                                        global subtotalFacVent1, subtotalFacVent2, subtotalFacVent3, subtotalFacVent4, sumatotalfinalFV, gananciaFV

                                                        gananciaFV=(((subtotalFacVent1 + subtotalFacVent2 + subtotalFacVent3 + subtotalFacVent4)*10)/100)

                                                        sumatotalfinalFV=(subtotalFacVent1 + subtotalFacVent2 + subtotalFacVent3 + subtotalFacVent4 +gananciaFV)

                                                        #---ventana emergente de error---
                                                        def alerta11():
                                                            messagebox.showwarning("!Error¡","¡Factura ya registrada!")

                                                        #---ventana emergente de error---
                                                        def alerta12():
                                                            messagebox.showwarning("!Error¡","¡Referencia de factura ya registrada!")

                                                        #---registro de ventas---
                                                        def regVentasFV():
                                                            
                                                            global contadorb1, contadorb2, contadorb3, contadorb4, codVenFvSave, codProdFCSave4
                                                            global codCliFVSave, cantProdFVSave, cantProdFVSave2, codProdFCSave3, cantProdFVSave3
                                                            global sumatotalfinalFV, subtotalFacVent1, subtotalFacVent2, subtotalFacVent3
                                                            global variableCifradaVa1, variableCifradaVa2, variableCifradaVb1, variableCifradaVb2
                                                            global variableCifradaVc1, variableCifradaVc2, cantProdFVSave4, subtotalFacVent4

                                                            NumFacVSave=NumFacV.get()
                                                            RefFacVSave=RefFacV.get()                                                         
                                                        
                                                            conexionsegura2=sqlite3.connect("inventario.db")
                                                            cursor1FacVenReg=conexionsegura2.cursor()
                                                            cursor2FacVenReg=conexionsegura2.cursor()

                                                            cursor1FacVenReg.execute("SELECT NumFac FROM VFacVista")
                                                            lista1NumFac=cursor1FacVenReg.fetchall()

                                                            cursor2FacVenReg.execute("SELECT RefFac FROM VFacVista")
                                                            lista1RefFacV=cursor2FacVenReg.fetchall()

                                                            nnn=0
                                                            for g in lista1NumFac:
                                                                if g[0]==NumFacVSave:
                                                                    alerta11()
                                                                    nnn += 1

                                                                if nnn == 0:

                                                                    for ss in lista1RefFacV:
                                                                        if ss[0]==RefFacVSave:
                                                                            alerta12()
                                                                            nnn += 1
                                                            
                                                            #---insertar datos en la tabla VFacVista---
                                                            if nnn==0:

                                                                conexionsegura3=sqlite3.connect("inventario.db")
                                                                cursor1FVIntro=conexionsegura3.cursor()

                                                                tupla1FacVenIntro=[
                                                                    (RefFacVSave, NumFacVSave, codCliFVSave, tupla1FacVen2[codCliFVSave-1][6], tupla1FacVen2[codCliFVSave-1][2], tupla1FacVen2[codCliFVSave-1][5], codVenFvSave, sumatotalfinalFV)
                                                                ]

                                                                cursor1FVIntro.executemany("INSERT INTO VFacVista VALUES(?,?,?,?,?,?,?,?)", tupla1FacVenIntro)

                                                                conexionsegura3.commit()
                                                                conexionsegura3.close()

                                                                if contadorb1 == 1:

                                                                    conexionCifrada5=sqlite3.connect("inventario.db")
                                                                    cursorFacVentReg1=conexionCifrada5.cursor()
                                                                    cursorInvVent1=conexionCifrada5.cursor()
                                                                    cursorInvVentBusc1=conexionCifrada5.cursor()
                                                                    cursorInvVentUpd1=conexionCifrada5.cursor()

                                                                    tupla2FacVent1=[
                                                                        (1, RefFacVSave, codProdFCSave, lista2FacVentInv1[codProdFCSave-1][1], cantProdFVSave, lista2FacVentInv1[codProdFCSave-1][2], subtotalFacVent1)
                                                                    ]

                                                                    cursorFacVentReg1.executemany("INSERT INTO VFacDetalle VALUES(?,?,?,?,?,?,?)", tupla2FacVent1)
                                                                    #-------------------actualizar inventario-----
                                                                    cursorInvVent1.execute("SELECT ItemCode FROM IInventario")
                                                                    tuplaCantProdFV1 = cursorInvVent1.fetchall()
                                                                    codProdFCSaveTemp = codProdFCSave

                                                                    querya= """
                                                                    SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                                    """

                                                                    cursorInvVentBusc1.execute(querya, (codProdFCSaveTemp,))
                                                                    CantInvFV1 = cursorInvVentBusc1.fetchall()
                                                                    restaCantVent1 = CantInvFV1[0][0] - cantProdFVSave

                                                                    for ppp1 in tuplaCantProdFV1:
                                                                        if str(ppp1[0]) == str(codProdFCSave):
                                                                            query1a = """
                                                                            UPDATE IInventario SET Cantidad = :restaCantVent1 WHERE ItemCode = :codProdFCSaveTemp
                                                                            """
                                                                            cursorInvVentUpd1.execute(query1a, {'restaCantVent1':restaCantVent1, 'codProdFCSaveTemp':codProdFCSaveTemp})

                                                                    conexionCifrada5.commit()
                                                                    conexionCifrada5.close()

                                                                #---insertar datos en la tabla VFacDetalle---
                                                                if contadorb2 == 1:

                                                                    conexionCifrada6=sqlite3.connect("inventario.db")
                                                                    cursorFacVentReg2=conexionCifrada6.cursor()
                                                                    cursorInvVent2=conexionCifrada6.cursor()
                                                                    cursorInvVentBusc2=conexionCifrada6.cursor()
                                                                    cursorInvVentUpd2=conexionCifrada6.cursor()

                                                                    tupla2FacVent2=[
                                                                        (2, RefFacVSave, codProdFCSave2, variableCifradaVa1, cantProdFVSave2 ,variableCifradaVa2, subtotalFacVent2)
                                                                    ]

                                                                    cursorFacVentReg2.executemany("INSERT INTO VFacDetalle VALUES(?,?,?,?,?,?,?)", tupla2FacVent2)
                                                                    #-------------------actualizar inventario-----
                                                                    cursorInvVent2.execute("SELECT ItemCode FROM IInventario")
                                                                    tuplaCantProdFV2 = cursorInvVent2.fetchall()
                                                                    codProdFCSaveTemp2 = codProdFCSave2

                                                                    queryab= """
                                                                    SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                                    """

                                                                    cursorInvVentBusc2.execute(queryab, (codProdFCSaveTemp2,))
                                                                    CantInvFV2 = cursorInvVentBusc2.fetchall()
                                                                    restaCantVent2 = CantInvFV2[0][0] - cantProdFVSave2

                                                                    for ppp2 in tuplaCantProdFV2:
                                                                        if str(ppp2[0]) == str(codProdFCSave2):
                                                                            query1ab = """
                                                                            UPDATE IInventario SET Cantidad = :restaCantVent2 WHERE ItemCode = :codProdFCSaveTemp2
                                                                            """
                                                                            cursorInvVentUpd2.execute(query1ab, {'restaCantVent2':restaCantVent2, 'codProdFCSaveTemp2':codProdFCSaveTemp2})

                                                                    conexionCifrada6.commit()
                                                                    conexionCifrada6.close()

                                                                if contadorb3 == 1:

                                                                    conexionCifrada7=sqlite3.connect("inventario.db")
                                                                    cursorFacVentReg3=conexionCifrada7.cursor()
                                                                    cursorInvVent3=conexionCifrada7.cursor()
                                                                    cursorInvVentBusc3=conexionCifrada7.cursor()
                                                                    cursorInvVentUpd3=conexionCifrada7.cursor()

                                                                    tupla2FacVent3=[
                                                                        (3, RefFacVSave, codProdFCSave3, variableCifradaVb1, cantProdFVSave3 ,variableCifradaVb2, subtotalFacVent3)
                                                                    ]

                                                                    cursorFacVentReg3.executemany("INSERT INTO VFacDetalle VALUES(?,?,?,?,?,?,?)", tupla2FacVent3)
                                                                    #-------------------actualizar inventario-----
                                                                    cursorInvVent3.execute("SELECT ItemCode FROM IInventario")
                                                                    tuplaCantProdFV3 = cursorInvVent3.fetchall()
                                                                    codProdFCSaveTemp3 = codProdFCSave3

                                                                    queryabc= """
                                                                    SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                                    """

                                                                    cursorInvVentBusc3.execute(queryabc, (codProdFCSaveTemp3,))
                                                                    CantInvFV3 = cursorInvVentBusc3.fetchall()
                                                                    restaCantVent3 = CantInvFV3[0][0] - cantProdFVSave3

                                                                    for ppp3 in tuplaCantProdFV3:
                                                                        if str(ppp3[0]) == str(codProdFCSave3):
                                                                            query1abc = """
                                                                            UPDATE IInventario SET Cantidad = :restaCantVent3 WHERE ItemCode = :codProdFCSaveTemp3
                                                                            """
                                                                            cursorInvVentUpd3.execute(query1abc, {'restaCantVent3':restaCantVent3, 'codProdFCSaveTemp3':codProdFCSaveTemp3})

                                                                    conexionCifrada7.commit()
                                                                    conexionCifrada7.close()

                                                                if contadorb4 == 1:

                                                                    conexionCifrada8=sqlite3.connect("inventario.db")
                                                                    cursorFacVentReg4=conexionCifrada8.cursor()
                                                                    cursorInvVent4=conexionCifrada8.cursor()
                                                                    cursorInvVentBusc4=conexionCifrada8.cursor()
                                                                    cursorInvVentUpd4=conexionCifrada8.cursor()

                                                                    tupla2FacVent4=[
                                                                        (4, RefFacVSave, codProdFCSave4, variableCifradaVc1, cantProdFVSave4,variableCifradaVc2, subtotalFacVent4)
                                                                    ]

                                                                    cursorFacVentReg4.executemany("INSERT INTO VFacDetalle VALUES(?,?,?,?,?,?,?)", tupla2FacVent4)
                                                                    #-------------------actualizar inventario-----
                                                                    cursorInvVent4.execute("SELECT ItemCode FROM IInventario")
                                                                    tuplaCantProdFV4 = cursorInvVent4.fetchall()
                                                                    codProdFCSaveTemp4 = codProdFCSave4

                                                                    queryabcd= """
                                                                    SELECT cantidad FROM IInventario WHERE ItemCode = ?
                                                                    """

                                                                    cursorInvVentBusc4.execute(queryabcd, (codProdFCSaveTemp4,))
                                                                    CantInvFV4 = cursorInvVentBusc4.fetchall()
                                                                    restaCantVent4 = CantInvFV4[0][0] - cantProdFVSave4

                                                                    for ppp4 in tuplaCantProdFV4:
                                                                        if str(ppp4[0]) == str(codProdFCSave4):
                                                                            query1abcd = """
                                                                            UPDATE IInventario SET Cantidad = :restaCantVent4 WHERE ItemCode = :codProdFCSaveTemp4
                                                                            """
                                                                            cursorInvVentUpd4.execute(query1abcd, {'restaCantVent4':restaCantVent4, 'codProdFCSaveTemp4':codProdFCSaveTemp4})

                                                                    conexionCifrada8.commit()
                                                                    conexionCifrada8.close()

                                                                ventActualizar=(contadorb1+contadorb2+contadorb3+contadorb4)

                                                                if ventActualizar > 0:

                                                                    conexionUDFV=sqlite3.connect("inventario.db")
                                                                    cursorUPFV1=conexionUDFV.cursor()
                                                                    cursorUPFV2=conexionUDFV.cursor()
                                                                    cursorUPFV3=conexionUDFV.cursor()

                                                                    #----------actualizar inventario--------------
                                                                    cursorUPFV1.execute("SELECT Cod_Vendedor FROM DVendedores")
                                                                    tuplaUPFV1 = cursorUPFV1.fetchall()
                                                                    codVenFvSaveTemp = codVenFvSave

                                                                    queryUDFV1= """
                                                                    SELECT TotalEntrante FROM DVendedores WHERE Cod_Vendedor = ?
                                                                    """

                                                                    cursorUPFV2.execute(queryUDFV1, (codVenFvSaveTemp,))
                                                                    tuplaUDFV2 = cursorUPFV2.fetchall()
                                                                    sumaTEnt = tuplaUDFV2[0][0] + sumatotalfinalFV

                                                                    for hh2 in tuplaUPFV1:
                                                                        if str(hh2[0]) == str(codVenFvSave):
                                                                            queryUDFV2 = """
                                                                            UPDATE DVendedores SET TotalEntrante = :sumaTEnt WHERE Cod_Vendedor = :codVenFvSaveTemp
                                                                            """
                                                                            cursorUPFV3.execute(queryUDFV2, {'sumaTEnt':sumaTEnt, 'codVenFvSaveTemp':codVenFvSaveTemp})

                                                                    conexionUDFV.commit()
                                                                    conexionUDFV.close()

                                                                    alerta13()

                                                        lsumaTotalFinalFC=Label(frameFacVent, text="TOTAL")
                                                        lsumaTotalFinalFC.grid(row=11, column=7)

                                                        lsumaGananciaFC=Label(frameFacVent, text="GANANCIA")
                                                        lsumaGananciaFC.grid(row=10, column=7)

                                                        lbTotalSumaFC=Listbox(frameFacVent)
                                                        lbTotalSumaFC.insert(0, sumatotalfinalFV)
                                                        lbTotalSumaFC.config(width="10", height="1")
                                                        lbTotalSumaFC.grid(row=11, column=8)

                                                        lbTotalGananciaFC=Listbox(frameFacVent)
                                                        lbTotalGananciaFC.insert(0, gananciaFV)
                                                        lbTotalGananciaFC.config(width="8", height="1")
                                                        lbTotalGananciaFC.grid(row=10, column=8)

                                                        bvenderFC=Button(frameFacVent, text="*VENDER*", command=regVentasFV)
                                                        bvenderFC.grid(row=11, column=6)

                                                    bBorProdFV1=Button(frameFacVent, text="-", command = borrarProdFV1)
                                                    bBorProdFV1.grid(row=6, column=1)

                                                    cantProdFVSave=cantProdFV.get()

                                                    subtotalFacVent1=(cantProdFVSave * lista2FacVentInv1[codProdFCSave-1][2])

                                                    lbSubTotalFV1=Listbox(frameFacVent)
                                                    lbSubTotalFV1.insert(0, subtotalFacVent1)
                                                    lbSubTotalFV1.config(width="10", height="1")
                                                    lbSubTotalFV1.grid(row=6, column=8)

                                                    bsumaTotalFV=Button(frameFacVent, text="SUMAR", command=totalfinalFV)
                                                    bsumaTotalFV.grid(row=11, column=9)

                                                cursor2FacVentInv1.execute("SELECT * FROM IInventario")
                                                lista2FacVentInv1=cursor2FacVentInv1.fetchall()

                                                lbPrecProdFV1=Listbox(frameFacVent) 
                                                lbPrecProdFV1.insert(0, lista2FacVentInv1[codProdFCSave-1][2])
                                                lbPrecProdFV1.config(width="10", height="1")
                                                lbPrecProdFV1.grid(row=6, column=4)

                                                lbDescFV1=Listbox(frameFacVent)
                                                lbDescFV1.insert(0, lista2FacVentInv1[codProdFCSave-1][1])
                                                lbDescFV1.config(width="18", height="1")
                                                lbDescFV1.grid(row=6, column=5)

                                                bCalcFV1=Button(frameFacVent, text="Calcular", command=STotalFacVent1)
                                                bCalcFV1.grid(row=6, column=7)

                                        if fed1 == 0:
                                            alerta7()

                                    eCodProdFC1=Entry(frameFacVent, textvariable=codProdFC)
                                    eCodProdFC1.grid(row=6, column=3)

                                    eCantProdFC1=Entry(frameFacVent, textvariable=cantProdFV)
                                    eCantProdFC1.grid(row=6, column=6)

                                    bBuscarInvFC1=Button(frameFacVent, text="Buscar", command=llamar2Inv1)
                                    bBuscarInvFC1.grid(row=6, column=2)

                                    contadorabc += 1

                            #---agregar un producto a la venta---
                            def venderProd2():

                                global contadorabcd, contadorb2

                                contadorb2 += 1

                                if contadorabcd == 0:

                                    #---llamar a inventario---
                                    def llamar2Inv2():

                                        global codProdFCSave2

                                        codProdFCSave2=codProdFC2.get()

                                        conexionFacVentInv2=sqlite3.connect("inventario.db")
                                        cursor1FacVentInv2=conexionFacVentInv2.cursor()
                                        cursor2FacVentInv2=conexionFacVentInv2.cursor()

                                        cursor1FacVentInv2.execute("SELECT ItemCode FROM IInventario")
                                        lista1FacVentInv2=cursor1FacVentInv2.fetchall()

                                        fed12 = 0

                                        #---ventana emergente de error---
                                        def alerta8():
                                            messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                                        for qqqq in lista1FacVentInv2:
                                            if str(qqqq[0]) == str(codProdFCSave2):
                                                fed12 +=1

                                                global variableCifradaVa1, variableCifradaVa2

                                                #---subtotal---
                                                def STotalFacVent2():

                                                    global cantProdFVSave2, subtotalFacVent2

                                                    #---limpiar campos del producto buscado---
                                                    def borrarProdFV2():
                                                        global subtotalFacVent2, contadorabcd, contadorb2

                                                        subtotalFacVent2 = 0

                                                        eCodProdFC2.destroy()
                                                        eCantProdFC2.destroy()
                                                        lbSubTotalFV2.destroy()
                                                        lbPrecProdFV2.destroy()
                                                        lbDescFV2.destroy()
                                                        bCalcFV2.destroy()
                                                        bBuscarInvFC2.destroy()

                                                        contadorabcd = contadorabcd - 1

                                                        contadorb2 = 0

                                                    bBorProdFV2=Button(frameFacVent, text="-", command = borrarProdFV2)
                                                    bBorProdFV2.grid(row=7, column=1)

                                                    cantProdFVSave2=cantProdFV2.get()

                                                    subtotalFacVent2=(cantProdFVSave2 * lista2FacVentInv2[codProdFCSave2-1][2])

                                                    lbSubTotalFV2=Listbox(frameFacVent)
                                                    lbSubTotalFV2.insert(0, subtotalFacVent2)
                                                    lbSubTotalFV2.config(width="10", height="1")
                                                    lbSubTotalFV2.grid(row=7, column=8)

                                                cursor2FacVentInv2.execute("SELECT * FROM IInventario")
                                                lista2FacVentInv2=cursor2FacVentInv2.fetchall()

                                                variableCifradaVa1=lista2FacVentInv2[codProdFCSave2-1][1]
                                                variableCifradaVa2=lista2FacVentInv2[codProdFCSave2-1][2]

                                                lbPrecProdFV2=Listbox(frameFacVent) 
                                                lbPrecProdFV2.insert(0, lista2FacVentInv2[codProdFCSave2-1][2])
                                                lbPrecProdFV2.config(width="10", height="1")
                                                lbPrecProdFV2.grid(row=7, column=4)

                                                lbDescFV2=Listbox(frameFacVent)
                                                lbDescFV2.insert(0, lista2FacVentInv2[codProdFCSave2-1][1])
                                                lbDescFV2.config(width="18", height="1")
                                                lbDescFV2.grid(row=7, column=5)

                                                bCalcFV2=Button(frameFacVent, text="Calcular", command=STotalFacVent2)
                                                bCalcFV2.grid(row=7, column=7)

                                        if fed12 == 0:
                                            alerta8()

                                    eCodProdFC2=Entry(frameFacVent, textvariable=codProdFC2)
                                    eCodProdFC2.grid(row=7, column=3)

                                    eCantProdFC2=Entry(frameFacVent, textvariable=cantProdFV2)
                                    eCantProdFC2.grid(row=7, column=6)

                                    bBuscarInvFC2=Button(frameFacVent, text="Buscar", command=llamar2Inv2)
                                    bBuscarInvFC2.grid(row=7, column=2)

                                    contadorabcd += 1

                            #---agregar un porducto para vender---
                            def venderProd3():

                                global contadorabcde, contadorb3

                                contadorb3 += 1

                                if contadorabcde == 0:

                                    #---llamar a inventario---
                                    def llamar2Inv3():

                                        global codProdFCSave3

                                        codProdFCSave3=codProdFC3.get()

                                        conexionFacVentInv3=sqlite3.connect("inventario.db")
                                        cursor1FacVentInv3=conexionFacVentInv3.cursor()
                                        cursor2FacVentInv3=conexionFacVentInv3.cursor()

                                        cursor1FacVentInv3.execute("SELECT ItemCode FROM IInventario")
                                        lista1FacVentInv3=cursor1FacVentInv3.fetchall()

                                        fed13 = 0

                                        #---ventana emergente de error
                                        def alerta9():
                                            messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                                        for qqqqq in lista1FacVentInv3:
                                            if str(qqqqq[0]) == str(codProdFCSave3):
                                                fed13 +=1

                                                global variableCifradaVb1, variableCifradaVb2

                                                #---subtotal---
                                                def STotalFacVent3():

                                                    global cantProdFVSave3, subtotalFacVent3

                                                    #---limpiar campos del producto buscado---
                                                    def borrarProdFV3():
                                                        global subtotalFacVent3, contadorabcde, contadorb3

                                                        subtotalFacVent3 = 0

                                                        eCodProdFC3.destroy()
                                                        eCantProdFC3.destroy()
                                                        lbSubTotalFV3.destroy()
                                                        lbPrecProdFV3.destroy()
                                                        lbDescFV3.destroy()
                                                        bCalcFV3.destroy()
                                                        bBuscarInvFC3.destroy()

                                                        contadorabcde = contadorabcde - 1

                                                        contadorb3 = 0

                                                    bBorProdFV3=Button(frameFacVent, text="-", command = borrarProdFV3)
                                                    bBorProdFV3.grid(row=8, column=1)

                                                    cantProdFVSave3=cantProdFV3.get()

                                                    subtotalFacVent3=(cantProdFVSave3 * lista2FacVentInv3[codProdFCSave3-1][2])

                                                    lbSubTotalFV3=Listbox(frameFacVent)
                                                    lbSubTotalFV3.insert(0, subtotalFacVent3)
                                                    lbSubTotalFV3.config(width="10", height="1")
                                                    lbSubTotalFV3.grid(row=8, column=8)

                                                cursor2FacVentInv3.execute("SELECT * FROM IInventario")
                                                lista2FacVentInv3=cursor2FacVentInv3.fetchall()

                                                variableCifradaVb1=lista2FacVentInv3[codProdFCSave3-1][1]
                                                variableCifradaVb2=lista2FacVentInv3[codProdFCSave3-1][2]

                                                lbPrecProdFV3=Listbox(frameFacVent) 
                                                lbPrecProdFV3.insert(0, lista2FacVentInv3[codProdFCSave3-1][2])
                                                lbPrecProdFV3.config(width="10", height="1")
                                                lbPrecProdFV3.grid(row=8, column=4)

                                                lbDescFV3=Listbox(frameFacVent)
                                                lbDescFV3.insert(0, lista2FacVentInv3[codProdFCSave3-1][1])
                                                lbDescFV3.config(width="18", height="1")
                                                lbDescFV3.grid(row=8, column=5)

                                                bCalcFV3=Button(frameFacVent, text="Calcular", command=STotalFacVent3)
                                                bCalcFV3.grid(row=8, column=7)

                                        if fed13 == 0:
                                            alerta9()

                                    eCodProdFC3=Entry(frameFacVent, textvariable=codProdFC3)
                                    eCodProdFC3.grid(row=8, column=3)

                                    eCantProdFC3=Entry(frameFacVent, textvariable=cantProdFV3)
                                    eCantProdFC3.grid(row=8, column=6)

                                    bBuscarInvFC3=Button(frameFacVent, text="Buscar", command=llamar2Inv3)
                                    bBuscarInvFC3.grid(row=8, column=2)

                                    contadorabcde += 1

                            #---agregar otro producto a la venta---
                            def venderProd4():

                                global contadorabcdef, contadorb4

                                contadorb4 += 1

                                if contadorabcdef == 0:

                                    #---llamar a inventario---
                                    def llamar2Inv4():

                                        global codProdFCSave4

                                        codProdFCSave4=codProdFC4.get()

                                        conexionFacVentInv4=sqlite3.connect("inventario.db")
                                        cursor1FacVentInv4=conexionFacVentInv4.cursor()
                                        cursor2FacVentInv4=conexionFacVentInv4.cursor()

                                        cursor1FacVentInv4.execute("SELECT ItemCode FROM IInventario")
                                        lista1FacVentInv4=cursor1FacVentInv4.fetchall()

                                        fed14 = 0

                                        #---ventana emergente de error---
                                        def alerta10():
                                            messagebox.showwarning("!Error¡","¡Producto no encontrado!")

                                        for qqqqqq in lista1FacVentInv4:
                                            if str(qqqqqq[0]) == str(codProdFCSave4):
                                                fed14 += 1

                                                global variableCifradaVc1, variableCifradaVc2

                                                #---subtotal---
                                                def STotalFacVent4():

                                                    global cantProdFVSave4, subtotalFacVent4

                                                    #---limpiar campos del producto buscado---
                                                    def borrarProdFV4():
                                                        global subtotalFacVent4, contadorabcdef, contadorb4

                                                        subtotalFacVent4 = 0

                                                        eCodProdFC4.destroy()
                                                        eCantProdFC4.destroy()
                                                        lbSubTotalFV4.destroy()
                                                        lbPrecProdFV4.destroy()
                                                        lbDescFV4.destroy()
                                                        bCalcFV4.destroy()
                                                        bBuscarInvFC4.destroy()

                                                        contadorabcdef = contadorabcdef - 1

                                                        contadorb4 = 0

                                                    bBorProdFV4=Button(frameFacVent, text="-", command = borrarProdFV4)
                                                    bBorProdFV4.grid(row=9, column=1)

                                                    cantProdFVSave4=cantProdFV4.get()

                                                    subtotalFacVent4=(cantProdFVSave4 * lista2FacVentInv4[codProdFCSave4-1][2])

                                                    lbSubTotalFV4=Listbox(frameFacVent)
                                                    lbSubTotalFV4.insert(0, subtotalFacVent4)
                                                    lbSubTotalFV4.config(width="10", height="1")
                                                    lbSubTotalFV4.grid(row=9, column=8)

                                                cursor2FacVentInv4.execute("SELECT * FROM IInventario")
                                                lista2FacVentInv4=cursor2FacVentInv4.fetchall()

                                                variableCifradaVc1=lista2FacVentInv4[codProdFCSave4-1][1]
                                                variableCifradaVc2=lista2FacVentInv4[codProdFCSave4-1][2]

                                                lbPrecProdFV4=Listbox(frameFacVent) 
                                                lbPrecProdFV4.insert(0, lista2FacVentInv4[codProdFCSave4-1][2])
                                                lbPrecProdFV4.config(width="10", height="1")
                                                lbPrecProdFV4.grid(row=9, column=4)

                                                lbDescFV4=Listbox(frameFacVent)
                                                lbDescFV4.insert(0, lista2FacVentInv4[codProdFCSave4-1][1])
                                                lbDescFV4.config(width="18", height="1")
                                                lbDescFV4.grid(row=9, column=5)

                                                bCalcFV4=Button(frameFacVent, text="Calcular", command=STotalFacVent4)
                                                bCalcFV4.grid(row=9, column=7)

                                        if fed14 == 0:
                                            alerta10()

                                    eCodProdFC4=Entry(frameFacVent, textvariable=codProdFC4)
                                    eCodProdFC4.grid(row=9, column=3)

                                    eCantProdFC4=Entry(frameFacVent, textvariable=cantProdFV4)
                                    eCantProdFC4.grid(row=9, column=6)

                                    bBuscarInvFC4=Button(frameFacVent, text="Buscar", command=llamar2Inv4)
                                    bBuscarInvFC4.grid(row=9, column=2)

                                    contadorabcdef += 1

                            lCodProdFV=Label(frameFacVent, text="Codigo del producto")
                            lCodProdFV.grid(row=5, column=3)

                            lPrecProdFV=Label(frameFacVent, text="Precio P/U")
                            lPrecProdFV.grid(row=5, column=4)

                            lNomProdFV=Label(frameFacVent, text="Descripcion")
                            lNomProdFV.grid(row=5, column=5)

                            lCantFC=Label(frameFacVent, text="Cantidad")
                            lCantFC.grid(row=5, column=6)

                            lsubtotalFC=Label(frameFacVent, text="Subtotal")
                            lsubtotalFC.grid(row=5, column=8)

                            bvenderProd1=Button(frameFacVent,text="+", command=venderProd1)
                            bvenderProd1.grid(row=6, column=0)

                            bvenderProd2=Button(frameFacVent,text="+", command=venderProd2)
                            bvenderProd2.grid(row=7, column=0)

                            bvenderProd3=Button(frameFacVent,text="+", command=venderProd3)
                            bvenderProd3.grid(row=8, column=0)

                            bvenderProd4=Button(frameFacVent,text="+", command=venderProd4)
                            bvenderProd4.grid(row=9, column=0)

                            bborrarDatVend=Button(frameFacVent, text="Borrar", command=borrarDatVend)
                            bborrarDatVend.grid(row=1, column=7)

                    if ddd == 0:
                        alerta6()

                #--------------------label"s-----------------------------------------
                lCodVend=Label(frameFacVent, text="Codigo del vendedor")
                lCodVend.grid(row=0, column=6)

                #------------------------entry's------------------------------------

                eCodVend=Entry(frameFacVent, textvariable=codVenFv)
                eCodVend.grid(row=1, column=6)

                #---------------------------------buton's-----------------------------------

                bBuscarVendFV=Button(frameFacVent, text="Buscar", command=busquedaVend)
                bBuscarVendFV.grid(row=0, column=7)

                bBorrarFacVent=Button(frameFacVent, text="Borrar", command=borrarDatCli)
                bBorrarFacVent.grid(row=1, column=5)

        
        if bbb==0:
            alerta5()


    #---------los label-----------

    lCodCli=Label(frameFacVent, text="Codigo del Cliente")
    lCodCli.grid(row=0, column=3, sticky="e")

    lNitCli=Label(frameFacVent, text="Nit:")
    lNitCli.grid(row=1, column=3, sticky="e")

    lNomCli=Label(frameFacVent, text="Nombre:")
    lNomCli.grid(row=2, column=3, sticky="e")

    lCiuCLi=Label(frameFacVent, text="Ciudad:")
    lCiuCLi.grid(row=3, column=3, sticky="e")

    lNumFacV=Label(frameFacVent, text="No. Factura")
    lNumFacV.grid(row=0, column=8)

    lRefFacV=Label(frameFacVent, text="Ref. Factura")
    lRefFacV.grid(row=1, column=8)

    #-----------los entry-------

    eCodCli=Entry(frameFacVent, textvariable=codCliFV)
    eCodCli.grid(row=0, column=4)

    eNumFacV=Entry(frameFacVent, textvar=NumFacV)
    eNumFacV.grid(row=0, column=9)

    eRefFacV=Entry(frameFacVent, textvariable=RefFacV)
    eRefFacV.grid(row=1, column=9)

    #-------los Botones---------

    bBuscarFacVent=Button(frameFacVent, text="Buscar", command=busquedaClientes)
    bBuscarFacVent.grid(row=0, column=5)

    bsalirFacVent=Button(frameFacVent, text="* SALIR *", command= salirFacVent)
    bsalirFacVent.grid(row=4, column=8, padx=10, pady=10)

#-------------------------cuadre de caja-------------------------

def cuadreCaja():

    #---frame del titulo---
    frameTitCCaj=Frame(fondo)
    labelTCCaj=Label(frameTitCCaj, text="                            Cuadre de Caja                            ")
    labelTCCaj.config(bg="#5E67F1", font=("Segoe Script", 18))
    labelTCCaj.grid(row=1, column=1)
    frameTitCCaj.pack()

    #---frame del contenido---
    framecuadre=Frame(fondo)
    framecuadre.config(bg="#6BD2D9")
    framecuadre.pack()

    #---funcion salir del cuadre de caja---
    def salircuadre():
        framecuadre.destroy()
        frameTitCCaj.destroy()

    conexionCuadre1=sqlite3.connect("inventario.db")
    cursorCuadreC1=conexionCuadre1.cursor()
    cursorCuadreC2=conexionCuadre1.cursor()

    cursorCuadreC1.execute("SELECT TotalEntrante FROM DVendedores")
    listaCuadreTE1=cursorCuadreC1.fetchall()

    kkk=0

    for lll in listaCuadreTE1:
        kkk =kkk + lll[0]
        
    cursorCuadreC2.execute("SELECT TotalSaliente FROM DProveedores")
    listaCuadreTE2=cursorCuadreC2.fetchall()

    rrr=0

    for www in listaCuadreTE2:
        rrr = rrr + www[0]

    gan=((kkk*10)/100)

    kkksg=(kkk - gan)

    totMerc=(rrr-kkksg)

    gtotMerc=((totMerc*10)/100)

    totMercGan=(totMerc+gtotMerc)

    #-----total en mercaderia-----
    lcuadre1=Label(framecuadre, text="Total en mercaderia (sin ganancias):")
    lcuadre1.config(bg="#6BD2D9")
    lcuadre1.grid(row=0, column=0)

    lbcuadre2=Listbox(framecuadre)
    lbcuadre2.insert(0,totMerc)
    lbcuadre2.config(width="18", height="1")
    lbcuadre2.grid(row=0, column=1)

    #-----total en mercaderia con ganancias-----
    lcuadre2=Label(framecuadre, text="Total en mercaderia (con ganancias):")
    lcuadre2.config(bg="#6BD2D9")
    lcuadre2.grid(row=1, column=0)

    lbcuadre2=Listbox(framecuadre)
    lbcuadre2.insert(0, totMercGan)
    lbcuadre2.config(width="18", height="1")
    lbcuadre2.grid(row=1, column=1)

    #-----total vendido sin ganacias
    lcuadre3=Label(framecuadre, text="Total vendido(sin ganancias):")
    lcuadre3.config(bg="#6BD2D9")
    lcuadre3.grid(row=2, column=0)

    lbcuadre3=Listbox(framecuadre)
    lbcuadre3.insert(0, kkksg)
    lbcuadre3.config(width="18", height="1")
    lbcuadre3.grid(row=2, column=1)

    #-----total vendido con ganancias-----
    lcuadre4=Label(framecuadre, text="Total vendido(con ganancias):")
    lcuadre4.config(bg="#6BD2D9")
    lcuadre4.grid(row=3, column=0)

    lbcuadre4=Listbox(framecuadre)
    lbcuadre4.insert(0, kkk)
    lbcuadre4.config(width="18", height="1")
    lbcuadre4.grid(row=3, column=1)

    #-----ganancias obtenidas-----
    lcuadre5=Label(framecuadre, text="Ganancias Obtenidas:")
    lcuadre5.config(bg="#6BD2D9")
    lcuadre5.grid(row=4, column=0)

    lbcuadre5=Listbox(framecuadre)
    lbcuadre5.insert(0, gan)
    lbcuadre5.config(width="18", height="1")
    lbcuadre5.grid(row=4, column=1)

    #-----boton salir-----
    bsalirCuadre=Button(framecuadre, text="SALIR", command=salircuadre)
    bsalirCuadre.grid(row=6, column=2)

#-------------------------Las funciones del menu principal-------------------------

#-----registros-----
def funcionRegistro():
    
    if varRegistro.get()==1:
        RegistroClientes()

    if varRegistro.get()==2:
        RegistroVendedores()

    if varRegistro.get()==3:
        RegistroProveedores()

#-----consultas-----
def funcionVisualizacion():
    
    if varVis.get()==1:
        visualizacionClientes()

    if varVis.get()==2:
        visualizacionVendedores()

    if varVis.get()==3:
        visualizacionProveedores()

    if varVis.get()==4:
        visualizacionInventario()

    if varVis.get()==5:
        visualizacionFacCompras()

    if varVis.get()==6:
        visualizacionFacVentas()

#-----compras y ventas-----
def funcionFactura():
    if varFac.get()==1:
        FacCompras()

    if varFac.get()==2:
        FacVentas()

#---------------Los Label del menu principal-----------------

lRegistro=Label(miFrame, text="REGISTROS:")
lRegistro.config(bg="#508BFA", font = ("Dosis", 12))
lRegistro.grid(row=1, column=1, sticky="w", padx=10, pady=5)

lVisuali=Label(miFrame, text="CONSULTA:")
lVisuali.config(bg="#508BFA", font = ("Dosis", 12))
lVisuali.grid(row=1, column=2, sticky="w", padx=10, pady=5)

lFacturacion=Label(miFrame, text="FACTURACION:")
lFacturacion.config(bg="#508BFA", font = ("Dosis", 12))
lFacturacion.grid(row=1, column=3, sticky="w", padx=10, pady=5)

#---------------Radiobuttons del menu principal---------------

rbCLientes=Radiobutton(miFrame, text="Registro de Clientes", variable=varRegistro, value=1, command=funcionRegistro)
rbCLientes.config(bg="#508BFA")
rbCLientes.grid(row=2, column=1, sticky="w", padx=20, pady=5)

rbVend=Radiobutton(miFrame, text="Registro de Vendedores", variable=varRegistro, value=2, command=funcionRegistro)
rbVend.config(bg="#508BFA")
rbVend.grid(row=3, column=1, sticky="w", padx=20, pady=5)

rbProv=Radiobutton(miFrame, text="Registro de Proveedores", variable=varRegistro, value=3, command=funcionRegistro)
rbProv.config(bg="#508BFA")
rbProv.grid(row=4, column=1, sticky="w", padx=20, pady=5)


rbVisClientes=Radiobutton(miFrame, text="Clientes registrados", variable=varVis, value=1, command=funcionVisualizacion)
rbVisClientes.config(bg="#508BFA")
rbVisClientes.grid(row=2, column=2, sticky="w", padx=20, pady=5)

rbVisVend=Radiobutton(miFrame, text="Vendedores registrados", variable=varVis, value=2, command=funcionVisualizacion)
rbVisVend.config(bg="#508BFA")
rbVisVend.grid(row=3, column=2, sticky="w", padx=20, pady=5)

rbVisProv=Radiobutton(miFrame, text="Proveedores registrados", variable=varVis, value=3, command=funcionVisualizacion)
rbVisProv.config(bg="#508BFA")
rbVisProv.grid(row=4, column=2, sticky="w", padx=20, pady=5)

rbVisInv=Radiobutton(miFrame, text="Inventario", variable=varVis, value=4, command=funcionVisualizacion)
rbVisInv.config(bg="#508BFA")
rbVisInv.grid(row=5, column=2, sticky="w", padx=20, pady=5)

rbVisFacComp=Radiobutton(miFrame, text="Facturas de compras registradas", variable=varVis, value=5, command=funcionVisualizacion)
rbVisFacComp.config(bg="#508BFA")
rbVisFacComp.grid(row=6, column=2, sticky="w", padx=20, pady=5)

rbVisFacVent=Radiobutton(miFrame, text="Facturas de ventas realizadas", variable=varVis, value=6, command=funcionVisualizacion)
rbVisFacVent.config(bg="#508BFA")
rbVisFacVent.grid(row=7, column=2, sticky="w", padx=20, pady=5)

rbFacComp=Radiobutton(miFrame, text="Compra:", variable=varFac, value=1, command=funcionFactura)
rbFacComp.config(bg="#508BFA")
rbFacComp.grid(row=2, column=3, sticky="w", padx=20, pady=5)

rbFacVent=Radiobutton(miFrame, text="Venta:", variable=varFac, value=2, command=funcionFactura)
rbFacVent.config(bg="#508BFA")
rbFacVent.grid(row=3, column=3, sticky="w", padx=20, pady=5)

#--------------------Botones del menu principal---------------------

botonCuadre=Button(miFrame, text="Cuadre de Caja", command=cuadreCaja)
botonCuadre.config(bg="#526BBF")
botonCuadre.grid(row=4, column=4, padx=20, pady=5)

botonSalida=Button(miFrame, text="Salir del programa", command=salir)
botonSalida.config(bg="#526BBF")
botonSalida.grid(row=5, column=4, padx=20, pady=5)

fondo.mainloop()
