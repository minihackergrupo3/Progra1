# Progra1
#Programa en python
from tkinter import *
from tkinter import messagebox
import sqlite3

fondo=Tk()
fondo.geometry("715x725")
fondo.title("VEPROEL.S.A")
fondo.config(bg="#9FA7B3")
fondo.resizable(False, False)

#scroll=Scrollbar(orient = "vertical")
#scroll.pack(side=RIGHT, fill=Y)

miframetitulo=Frame(fondo)

labelmenu=Label(miframetitulo, text="            Menu principal            ")
labelmenu.config(bg="#73C043", font=("Segoe Script", 30))
labelmenu.grid(row=1, column=1)

miframetitulo.pack()

miFrame=Frame(fondo)
miFrame.config(bg="#508BFA")
#miFrame.grid(row=2, column=1)
miFrame.config(bd=10, relief="groove")
miFrame.pack()

#---------------Variables para guardar datos---------------

nombreprueba1=StringVar()

nombVend=StringVar()
apeVend=StringVar()
telVend=IntVar()

varRegistro=IntVar()
varVis=IntVar()
varFac=IntVar()

#---------------Registro de clientes----------------

def RegistroClientes():

    def pruebafuncion1():
        nombreprueba1mas=nombreprueba1.get()
        print(nombreprueba1mas)

        conexion123=sqlite3.connect("inventario.db")
        conector123=conexion123.cursor()

        tuplaprueba=[
            (nombreprueba1mas, "perez",0, "12457896")
        ]

        conector123.execute("SELECT * FROM DVendedores")
        tuplaprueba1=conector123.fetchall()

        conector123.executemany("INSERT INTO DVendedores VALUES (NULL,?,?,?,?)", tuplaprueba)
        print(tuplaprueba1)

        conexion123.commit()
        conexion123.close()

    def salirdefinitivo():
        
        frameTitCli.destroy()
        miframeprueba1.destroy()

    frameTitCli=Frame(fondo)

    labelTCli=Label(frameTitCli, text="                    Registro de Clientes                    ")
    labelTCli.config(bg="#E59E5B", font=("Segoe Script", 20))
    labelTCli.grid(row=1, column=1)

    frameTitCli.pack()

    miframeprueba1=Frame(fondo)
    miframeprueba1.pack()

    pruebalabel=Label(miframeprueba1, text="hola")
    pruebalabel.grid(row=1, column=1)
    
    pruebaentry1=Entry(miframeprueba1, textvariable=nombreprueba1)
    pruebaentry1.grid(row=1, column=2)

    pruebaboton1=Button(miframeprueba1, text="enviar", command=pruebafuncion1)
    pruebaboton1.grid(row=1, column=3)

    botonsalirClientes=Button(miframeprueba1, text="salir", command=salirdefinitivo)
    botonsalirClientes.grid(row=1, column=4)

#---------------Registro de vendedores---------------

def RegistroVendedores():

    frameTitVend=Frame(fondo)

    labelTVend=Label(frameTitVend, text="                  Registro de Vendedores                  ")
    labelTVend.config(bg="#E59E5B", font=("Segoe Script", 20))
    labelTVend.grid(row=1, column=1)

    frameTitVend.pack()

    frameVend=Frame(fondo)
    frameVend.pack()

    #---Las funciones---

    def envioVend():
        nombVendSave=nombVend.get()
        apeVendSave=apeVend.get()
        telVendSave=telVend.get()

        conexionVend=sqlite3.connect("inventario.db")
        cursorVend=conexionVend.cursor()

        datosVend=[
            (nombVendSave, apeVendSave,0, telVendSave)
        ]

        cursorVend.execute("SELECT * FROM DVendedores")
        datosVendSave=cursorVend.fetchall()

        cursorVend.executemany("INSERT INTO DVendedores VALUES (NULL,?,?,?,?)", datosVend)
        print(datosVendSave)

        conexionVend.commit()
        conexionVend.close()

    def salirVend():
        frameVend.destroy()
        frameTitVend.destroy()

    def limpiarPantVend():
        nombVend.set("")
        apeVend.set("")
        telVend.set("")

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

    #---Los botones---

    bEnvioVend=Button(frameVend, text="* ENVIO *", command=envioVend)
    bEnvioVend.grid(row=4, column=1, padx=10, pady=10)

    bBorrarVend=Button(frameVend, text="* BORRAR *", command=limpiarPantVend)
    bBorrarVend.grid(row=4, column=2, padx=10, pady=10)

    bSalirVend=Button(frameVend, text="* SALIR *", command=salirVend)
    bSalirVend.grid(row=4, column=3, padx=10, pady=10)

#----------------Registro de Proveedores--------------------

def RegistroProveedores():

    frameTitProv=Frame(fondo)
    labelTProv=Label(frameTitProv, text="                 Registro de Proveedores                 ")
    labelTProv.config(bg="#E59E5B", font=("Segoe Script", 20))
    labelTProv.grid(row=1, column=1)
    frameTitProv.pack()

    frameRProv=Frame(fondo)
    #frameRProv.(row=1, column = 1)
    frameRProv.pack()

    #--------variabes globales
    minombre = StringVar()
    miPBX = IntVar()
    miNIT = StringVar()

    def salirRegProv():
        frameRProv.destroy()
        frameTitProv.destroy()

    def borrarRegProv():
        miNIT.set("")
        minombre.set("")
        miPBX.set("")

    def alerta1():
        messagebox.showwarning("!HECHO¡","¡Proveedores registrado con exito!")

    def alerta2():
        messagebox.showwarning("!FATAL ERROR¡","¡El proveedor ya esta registrado!")

    def codigoboton():
        global nombre, PBX, NIT 
        NIT = miNIT.get()
        nombre = minombre.get()
        PBX = miPBX.get()
    
        conexion_db()

    #------------ingreso de nombre

    def ingresos_texto(): 
        #global minombre, miPBX, miNIT

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

#-------------visualizacion de clientes registrados-----------------

def visualizacionClientes():

    frameTitCli=Frame(fondo)
    labelTVClientes=Label(frameTitCli, text="                     Cientes registrados                     ")
    labelTVClientes.config(bg="#C4CF52", font=("Segoe Script", 20))
    labelTVClientes.grid(row=1, column=1)
    frameTitCli.pack()

    frameVClientes=Frame(fondo)
    frameVClientes.pack()

    def salirVClientes():
        frameTitCli.destroy()
        frameVClientes.destroy()

    #-------los Botones---------

    bsalirVCli=Button(frameVClientes, text="* SALIR *", command= salirVClientes)
    bsalirVCli.grid(row=1, column=1, padx=10, pady=10)

#--------------Visualizacion de vendedores------------------

def visualizacionVendedores():

    frameTVVend=Frame(fondo)
    labelTVVend=Label(frameTVVend, text="                  Vendedores registrados                  ")
    labelTVVend.config(bg="#C4CF52", font=("Segoe Script", 20))
    labelTVVend.grid(row=1, column=1)
    frameTVVend.pack()

    frameVVendedores=Frame(fondo)
    
    #vertscroll = Scrollbar(frameVVendedores, orient='vertical', command=frameVVendedores.yview)
    
    #vertscroll.grid(row = 1, column = 3, sticky = "nsew")
    #vertscroll.pack()

    #frameVVendedores.configure(yscrollcommand=vertscroll.set)

    #frameVVendedores.pack()

    def salirVVend():
        frameTVVend.destroy()
        frameVVendedores.destroy()

    conexionvVend=sqlite3.connect("inventario.db")

    cursorvVend=conexionvVend.cursor()

    cursorvVend.execute("SELECT * FROM DVendedores")

    tuplavVend=cursorvVend.fetchall()
    b=0
    for i in tuplavVend:
        labelVend = Label(frameVVendedores, text= i)
        labelVend.grid(row=b, column=1, padx=20, pady=10, sticky="w")
        b += 1

    #-------los Botones---------

    bsalirVVend=Button(frameVVendedores, text="* SALIR *", command= salirVVend)
    bsalirVVend.grid(row=0, column=2, padx=10, pady=10)

#---------------Visualizacion de Proveedores---------------

def visualizacionProveedores():

    frameTVProv=Frame(fondo)
    labelTVProv=Label(frameTVProv, text="                 Proveedores Registrados                 ")
    labelTVProv.config(bg="#C4CF52", font=("Segoe Script", 20))
    labelTVProv.grid(row=1, column=1)
    frameTVProv.pack()

    frameVProv=Frame(fondo)
    frameVProv.pack()

    def salirVProv():
        frameTVProv.destroy()
        frameVProv.destroy()

    #-------los Botones---------

    bsalirVProv=Button(frameVProv, text="* SALIR *", command= salirVProv)
    bsalirVProv.grid(row=1, column=1, padx=10, pady=10)

#-----------------Productos Registrados--------------------

def visualizacionInventario():

    frameTVInv=Frame(fondo)
    labelTVInv=Label(frameTVInv, text="                          Inventario                          ")
    labelTVInv.config(bg="#C4CF52", font=("Segoe Script", 20))
    labelTVInv.grid(row=1, column=1)
    frameTVInv.pack()

    frameVInv=Frame(fondo)
    frameVInv.pack()

    def salirVInv():
        frameTVInv.destroy()
        frameVInv.destroy()

    #-------los Botones---------

    bsalirVInv=Button(frameVInv, text="* SALIR *", command= salirVInv)
    bsalirVInv.grid(row=1, column=1, padx=10, pady=10)

#-------------Facturas de compras registradas-------------------

def visualizacionFacCompras():

    frameTVFacComp=Frame(fondo)
    labelTVFacComp=Label(frameTVFacComp, text="                   Facturas de Compras                   ")
    labelTVFacComp.config(bg="#C4CF52", font=("Segoe Script", 20))
    labelTVFacComp.grid(row=1, column=1)
    frameTVFacComp.pack()

    frameVFacComp=Frame(fondo)
    frameVFacComp.pack()

    def salirVFacComp():
        frameTVFacComp.destroy()
        frameVFacComp.destroy()

    #-------los Botones---------

    bsalirVFacComp=Button(frameVFacComp, text="* SALIR *", command= salirVFacComp)
    bsalirVFacComp.grid(row=1, column=1, padx=10, pady=10)

#---------------Facturas de ventas registradas-----------------

def visualizacionFacVentas():

    frameTVFacVent=Frame(fondo)
    labelTVFacVent=Label(frameTVFacVent, text="                    Facturas de Ventas                    ")
    labelTVFacVent.config(bg="#C4CF52", font=("Segoe Script", 20))
    labelTVFacVent.grid(row=1, column=1)
    frameTVFacVent.pack()

    frameVFacVent=Frame(fondo)
    frameVFacVent.pack()

    def salirVFacVent():
        frameTVFacVent.destroy()
        frameVFacVent.destroy()

    #-------los Botones---------

    bsalirVFacVent=Button(frameVFacVent, text="* SALIR *", command= salirVFacVent)
    bsalirVFacVent.grid(row=1, column=1, padx=10, pady=10)

#-----------------------Compras-------------------------

def FacCompras():

    frameTFComp=Frame(fondo)
    labelTFComp=Label(frameTFComp, text="                           Compras                           ")
    labelTFComp.config(bg="#DC5252", font=("Segoe Script", 20))
    labelTFComp.grid(row=1, column=1)
    frameTFComp.pack()

    frameFacComp=Frame(fondo)
    frameFacComp.pack()

    def salirFacComp():
        frameTFComp.destroy()
        frameFacComp.destroy()

    #-------los Botones---------

    bsalirFacComp=Button(frameFacComp, text="* SALIR *", command= salirFacComp)
    bsalirFacComp.grid(row=1, column=1, padx=10, pady=10)

#------------------------ventas----------------------------

def FacVentas():

    frameTFVent=Frame(fondo)
    labelTFVent=Label(frameTFVent, text="                           Ventas                           ")
    labelTFVent.config(bg="#DC5252", font=("Segoe Script", 20))
    labelTFVent.grid(row=1, column=1)
    frameTFVent.pack()

    frameFacVent=Frame(fondo)
    frameFacVent.pack()

    def salirFacVent():
        frameTFVent.destroy()
        frameFacVent.destroy()

    #-------los Botones---------

    bsalirFacVent=Button(frameFacVent, text="* SALIR *", command= salirFacVent)
    bsalirFacVent.grid(row=1, column=1, padx=10, pady=10)

#---------------Las funciones principales-------------------

def salir():
    fondo.destroy()

def funcionRegistro():
    
    if varRegistro.get()==1:
        RegistroClientes()

    if varRegistro.get()==2:
        RegistroVendedores()

    if varRegistro.get()==3:
        RegistroProveedores()

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

def funcionFactura():
    if varFac.get()==1:
        FacCompras()

    if varFac.get()==2:
        FacVentas()

#---------------Los Label del menu principal-----------------

lRegistro=Label(miFrame, text="REGISTROS:")
lRegistro.config(bg="#508BFA", font = ("Dosis", 12))
lRegistro.grid(row=1, column=1, sticky="w", padx=10, pady=10)

lVisuali=Label(miFrame, text="VISUALIZACION:")
lVisuali.config(bg="#508BFA", font = ("Dosis", 12))
lVisuali.grid(row=1, column=2, sticky="w", padx=10, pady=10)

lFacturacion=Label(miFrame, text="FACTURACION:")
lFacturacion.config(bg="#508BFA", font = ("Dosis", 12))
lFacturacion.grid(row=1, column=3, sticky="w", padx=10, pady=10)

#---------------Radiobuttons del menu principal---------------

rbCLientes=Radiobutton(miFrame, text="Registro de Clientes", variable=varRegistro, value=1, command=funcionRegistro)
rbCLientes.config(bg="#508BFA")
rbCLientes.grid(row=2, column=1, sticky="w", padx=20, pady=10)

rbVend=Radiobutton(miFrame, text="Registro de vededores", variable=varRegistro, value=2, command=funcionRegistro)
rbVend.config(bg="#508BFA")
rbVend.grid(row=3, column=1, sticky="w", padx=20, pady=10)

rbProv=Radiobutton(miFrame, text="Registro de Proveedores", variable=varRegistro, value=3, command=funcionRegistro)
rbProv.config(bg="#508BFA")
rbProv.grid(row=4, column=1, sticky="w", padx=20, pady=10)


rbVisClientes=Radiobutton(miFrame, text="Clientes registrados", variable=varVis, value=1, command=funcionVisualizacion)
rbVisClientes.config(bg="#508BFA")
rbVisClientes.grid(row=2, column=2, sticky="w", padx=20, pady=10)

rbVisVend=Radiobutton(miFrame, text="Vendedores registrados", variable=varVis, value=2, command=funcionVisualizacion)
rbVisVend.config(bg="#508BFA")
rbVisVend.grid(row=3, column=2, sticky="w", padx=20, pady=10)

rbVisProv=Radiobutton(miFrame, text="Proveedores registrados", variable=varVis, value=3, command=funcionVisualizacion)
rbVisProv.config(bg="#508BFA")
rbVisProv.grid(row=4, column=2, sticky="w", padx=20, pady=10)

rbVisInv=Radiobutton(miFrame, text="Inventario", variable=varVis, value=4, command=funcionVisualizacion)
rbVisInv.config(bg="#508BFA")
rbVisInv.grid(row=5, column=2, sticky="w", padx=20, pady=10)

rbVisFacComp=Radiobutton(miFrame, text="Facturas de compras registradas", variable=varVis, value=5, command=funcionVisualizacion)
rbVisFacComp.config(bg="#508BFA")
rbVisFacComp.grid(row=6, column=2, sticky="w", padx=20, pady=10)

rbVisFacVent=Radiobutton(miFrame, text="Facturas de ventas registradas", variable=varVis, value=6, command=funcionVisualizacion)
rbVisFacVent.config(bg="#508BFA")
rbVisFacVent.grid(row=7, column=2, sticky="w", padx=20, pady=10)


rbFacComp=Radiobutton(miFrame, text="Compra:", variable=varFac, value=1, command=funcionFactura)
rbFacComp.config(bg="#508BFA")
rbFacComp.grid(row=2, column=3, sticky="w", padx=20, pady=10)

rbFacVent=Radiobutton(miFrame, text="Venta:", variable=varFac, value=2, command=funcionFactura)
rbFacVent.config(bg="#508BFA")
rbFacVent.grid(row=3, column=3, sticky="w", padx=20, pady=10)

#--------------------Botones del menu principal---------------------

botonCuadre=Button(miFrame, text="Cuadre de Caja")
botonCuadre.config(bg="#526BBF")
botonCuadre.grid(row=4, column=4, padx=20, pady=10)

botonSalida=Button(miFrame, text="Salir del programa", command=salir)
botonSalida.config(bg="#526BBF")
botonSalida.grid(row=5, column=4, padx=20, pady=10)

fondo.mainloop()
