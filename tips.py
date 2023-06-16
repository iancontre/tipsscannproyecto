
#Mensaje de bienvenida
print("BIENVENIDO A TIPS-SCAN ¡REGÍSTRATE!")
print("""""""""""")
#Registro e inicio de sesión
registros = {} #Aquí almaceno los registros como (Diccionario)
#Registro Cliente
def registro():
    nombre = input("Ingresa tu nombre completo: ")
    correo = input("Ingresa tu correo electrónico: ")
    telefono = input("Ingresa número de teléfono: ")
    contraseña = input("Ingresa contraseña que deseas asignar: ")
    registros[correo] = (nombre, telefono, contraseña)
    print("¡Muy bien!, ya eres parte de nuestro sistema, ¡registro exitoso!")

print("""""""""""")
#Inicio de Sesión usuario(correo y contraseña)
def sesion():
    print("BIENVENIDO A TIPS-SCAN ¡inicia Sesión!")
    correo = input("Ingresa tu correo electrónico que registraste con nosotros: ")
    contraseña = input("Ingrese tu contraseña: ")
    if correo in registros and registros[correo][2] == contraseña:
        print("¡Inicio de sesión exitoso!")
        nombre, telefono, _ = registros[correo]
        print("Nombre:", nombre)
         
    if sesion != correo and contraseña:
        print("Correo o contraseña incorrecto")
        
    def recuperar_contrasena():
        recuperar=input("¿Desea recuperar contrasena? :")
        if recuperar== "si":
            nuevacontra=input("Digite la nueva contraseña: ")
            print("Contraseña actualizada")
        else:
            print("Te devolveremos al inicio de sesión para que vuelvas a intentar")
            sesion()
        
    recuperar_contrasena()
    
    
        
    
    
        
        
    
       
   
        
    
    
    
    
    
        
       

        

registro()
sesion()



 


#Manual interactivo 
manual = {
    "consejería": {
        "descripción": "En nuestro apartado de Consejería deberás llenar cada uno de los campos del formulario y luego seleccionar el botón enviar formulario, para luego recibier los dos consejos de tecnología que el sistema pudo detectar segun la información suministrada ",
        "siguiente": "historial"
    },
    "historial": {
        "descripción": "Aquí podrás ver las últimos consejo de tecnología que fueron realizado en 1 mes, después del mes se renuevan a recientes.",
        "siguiente": "ayuda"
    },
    "ayuda": {
        "descripción": "Comunícate con nuestros asesores en tiempo real",
        "siguiente": "fin"
    },
    "fin": {
        "descripción": "¡Ya has terminado nuestro manual ! puedes continuar utilizando nuestro sistema"
    }
}
#(Bucle y función para mostrar el)
def mostrar_manual():
    seccionmanual = "consejería"
    while seccionmanual != "fin":
        print("Bienvenido a nuestra Manual interactivo")
        print("""""""""""")
        print(manual[seccionmanual]["descripción"])
        print("""""""""""")
        print("Siguiente sección:", manual[seccionmanual]["siguiente"])
        print("""""""""""")
        input("Presione Enter para continuar...")
        seccionmanual = manual[seccionmanual]["siguiente"]


mostrar_manual()

#FormularioConsejeria
consejos = {
    "celular": "Consejo 1: Celular XIAOMI Redmi Note 12 128GB ",
    "computador": "Consejo 2: FUENTE REAL 300W, BOARD AMD A320M, PROCESADOR AMD RYZEN 5 5600G, GRAFICOS INTEGRADOS AMD RADEON VEGA 7, RAM DDR4 16GB BLINDADA 3200MHZ 1X16GB (Ó 2X8GB), SSD 240GB (Ó DISCO DURO 1TB), MONITOR LED 22" ,
    "tableta": "Consejo 3: Tablet LENOVO 10 Pulgadas M10 Plus" ,
    "portatil": "Consejo 4: Portátil ASUS 14 Pulgadas X415JA - Intel Core i5 - RAM 8GB - Disco SSD 256 GB"
}
#Formulario preguntas
def consejeria():
    print(" Bienvenido al Formulario de Consejería")
    especificaciones = input("¿Para qué necesitas el equipo?: ")
    tipo_equipo = seleccionartipo_equipo()
    presupuesto = float(input("¿Qué presupuesto tienes para el equipo?: "))
    profesion = input("Escribenos más detalles de tu profesión: ")

    
 #Respuestadespuésde seleccionar el consejo
    print("Según la información suministrada el consejo de tecnología que se adecúa a la información registrada es : ")
    consejo = consejotipo_equipo(tipo_equipo)
    print(consejo)

#Función para diferenciar los consejos y exigir una opción, de lo contrario no hay consejo
def seleccionartipo_equipo():
    tipos_validos = ["celular", "computador", "tableta", "portatil"]
    tipo_equipo = ""
    while tipo_equipo not in tipos_validos:
        tipo_equipo = input("¿Qué tipo de equipo deseas comprar? (celular, computador, tableta, portatil): ").lower()
    return tipo_equipo

def consejotipo_equipo(tipo_equipo):
    return consejos.get(tipo_equipo, "No se encontró un consejo para el tipo de equipo seleccionado.")


consejeria()
print("""""""""""")
print("""""""""""")
#Rentabilidad EMPRESA

total_ventas = 10000  
ganancias = 5000  
costos = 3000  #Costos asociados a nuestro sistema de consejería
inversion_inicial = 2000  

#Cálculos
ingresos = total_ventas * ganancias
gastos = costos + inversion_inicial
rentabilidad = (ingresos - gastos) / gastos * 100

# Resultado final e informe
print("Cálculo de Rentabilidad mensual")
print("Ingresos: $", ingresos)
print("Gastos: $", gastos)
print("Rentabilidad: ", round(rentabilidad, 2), "%")

print("""""""""""")
print("""""""""""")
#modulo de ventas
print("Bienvenido al modulo de ventas")
contraseña=input("Digite su contraseña para que pueda conocer los productos disponibles,productos Nuevos y los descuentos de estos ")
print("")
print("\n")
print("PRODUCTOS DISPONIBLES")
# 0,1,2,3,4
productos_disponibles= ["1. Lenovo ideacentre Aio 3¡ ma Gen 24: $ 5,199,901",
"2. portatil HP 15.6 pulgadas: $1,699,900" ,
"3. All in Onelenovo 23.8 PUL: $3,999,000",
"4. Xiaomi Smartwatch multitech con termometro: $279,900",
"5. ¡Phone 14 pro max 128 Gb e-SIM A16 Bionic camara: $5,999,900" ]
print(productos_disponibles[0])
print(productos_disponibles[1])
print(productos_disponibles[2])
print(productos_disponibles[3])
print(productos_disponibles[4])
print("\n")

#acceso a nuevos productos disponibles

print(f"NUEVOS PRODUCTOS")
productosnuevos=["1. Samsung Galaxy A14 $684,000",
"2. Xiaomi Redmi 9c 3+64Gb aurora $389,900",
"3. Portatil Lenovo Ryzen 55500U Ram $2,199,900",
"4. Lenovo ThinkpadX1 Fold (13.3 Intel) $8,499,900"]
print(productosnuevos[0])
print(productosnuevos[1])
print(productosnuevos[2])
print(productosnuevos[3])
print("\n")

#Acceso a productos de otras tiendas
print("Aqui podras ver la cantidad de productos disponibles en otros almacenes")
print("")
Cantidad= { "Bosa":123, "Tintal":678, "Chapinero": 1322, "Engativa":765 }
for k,v in Cantidad.items():
    print(k,v)
print("")
Busca=input("Escriba el nombre de la tienda que quiere ver")
print("Resultado:",Cantidad.get(Busca, "No se encontro la tienda"))
print("")

# Datos de usuario

print("Aqui podras encontrar los datos de usuarios ")
print("")
Datos= {"Martin mendoza":3125433345, "paula Diaz":3165873342, "Rodolfo peréz":3225478977, "Juan jose":3225764355, "Maria de Peréz":3225436789 }
for k,v in Datos.items():
    print(k,v)
print("")
Buscar=input("Escriba el nombre de la persona que desea buscar")
print("Resultado:",Datos.get(Buscar, "No se encontro el usuario por favor verifica el nombre"))
print("")


# numero de asesorias realizadas

lunes=int(input("Ingrese el total de asesorias del dia lunes"))
Martes=int(input("Ingrese cuantas asesorias realizo el dia martes"))
Miercoles=int(input("ingrese las asesorias del dia miercoles"))
Jueves=int(input("Ingrese las asesorias del dia Jueves"))
Viernes=int(input ("Ingrese las asesorias del dia Viernes"))

suma=lunes+Martes+Miercoles+Jueves+ Viernes
print("Durante la semana usted realizo un total de  Asesorias ", suma ,"En breve enviaremos el reporte a la empresa")
print("")


#Metodos de pago 
print("Aqui vas a encontar los metodos de pago que tenemos disponibles")
print("")
def Efectivo():
    print()
def Tarjetadebito():
    print()
def Tarjetacrédito():
    print()
def PSE():
    print()
def Sistecrédito():
    print()
metodo_pago={"Efectivo":Efectivo, "Tarjetadebito":Tarjetadebito, "Tarjetacréddito":Tarjetacrédito, "PSE":PSE, "Sistecrédito":Sistecrédito, }
for k,v in  metodo_pago.items():
    print(k)
print("")
Pagos=input("Escriba el metodo de pago con el que desea cancelar")
print("Resultado:",metodo_pago.get(Pagos, "Gracias por visitar nuestras tiendas , en breve continuaremos con el proceso"))
print("")

#acceso a descuentos
Ingreso=input("Digite su nombre para que pueda acceder a los descuentos de los productos")
print("")
print("Aqui podras encontar el descuento que tiene cada producto y saber  el valor final con el descuento ")
print("")
Descuentos=["1.computadores: (10%)", "2.Celulares: (20%)", "3.Televisores: (15%)", "4.tablets (25%)", "5.relojes_inteligentes (30%)",]
print(Descuentos[0])
print(Descuentos[1])
print(Descuentos[2])
print(Descuentos[3])
print(Descuentos[4])
print("\n")

print("Aqui podras verificar el precio final del producto según su descuento")
nombre_producto=print(input("Ingrese el nombre del producto "))
precio=int(input("Ingrese el precio del producto"))
descuento=int(input("Ingrese el descuento que tiene el producto"))
precio_final=precio - (precio*descuento)/100
print("el precio final del producto con el descuento es de $",precio_final)

print("""""""""""")
print("""""""""""")
#Marca mas vendida
print("Aqui vas a encontrar las marcas más vendidas")
print("")
Ventas=["Lenovo: Con un 30% , en equipos vendidos", "HP inc: con un 25% ,en equipos vendidoss ", "Apple : con 20% ,en equipos vendidos",]
print(Ventas[0])
print(Ventas[1])
print(Ventas[2])







print("""""""""""")
print("""""""""""")
#Admin e inventario
#ADMINISTRADOR

print("Bienvenido a la pestaña de Administrador")
contraseña=input("Digite su contraseña para entrar a la pestaña de Administrador:")

#Primera historia 

contraseña=input("Digite su contraseña para acceder a los datos de usuario y empresa:")
print("")
registros={"Usuarios":3, "Empresas":1}
print("Cantidad de registros")
print("")
for k,v in registros.items():
    print(k,v)
print("")
print("Información de usuarios y empresas")
print("")
print("Usuarios")
print("")
datos={"Usuario1": "Luis Castro",
       "Usuario2": "Maria Lopez",
       "Usuario3": "Martha Ruiz", 
       "Empresa":"Alkosto",}
print(datos["Usuario1"])
print(datos["Usuario2"])
print(datos["Usuario3"])
print("")
print("Empresas")
print("")
print(datos["Empresa"])
print("")

#Segunda historia

print("Información de usuario y empresa")
print("")
print("Usuarios")
print("")
datos={"Usuario1": "Luis Castro",
       "Usuario2": "Maria Lopez",
       "Usuario3": "Martha Riuz", 
       "Empresa":"Alkosto",}
print(datos["Usuario1"])
print(datos["Usuario2"])
print(datos["Usuario3"])
print("")
print("Empresas")
print("")
print(datos["Empresa"])
print("")
queja=input("Escriba su queja, reclamo o sugerencia")
print("Gracias por su comentario")
print("")

#INVENTARIOS

print("Bienvenido a la pestaña de Inventarios")
contraseña=input("Digite su contraseña para entrar a inventarios:")
print("")

#Cantidades

print("En esta sección podrás encontrar las cantidades de los equipos")
print("")
def Computadores():
    print()
def Portatiles():
    print
def Celulares():
    print
def Relojes_inteligentes():
    print
def Tabletas():
    print
cantidades={"Computadores":10, "Portatiles" :10, "Celulares":10, "Relojes inteligentes":10, "Tabletas":10,}
for k,v in cantidades.items():
    print(k,v)
print("")
cantidades["Computadores"]=12
print("Cantidad modificada:")
print("")
for k,v in cantidades.items():
    print(k,v)
print("")

#Marcas

print("En esta sección encontrarás todas las marcas de los productos")
print("")
def Lenovo():
    print()
def Apple():
    print
def Samsung():
    print
def hp():
    print
def Huawei():
    print
def Motorola():
    print
def Xiaomi():
    print
def Asus():
    print
marcas={"Lenovo": Lenovo , "Apple": Apple, "Samsung": Samsung, "hp": hp, "Huawei": Huawei, "Motorola": Motorola , "Xiaomi" : Xiaomi , "Asus": Asus}
for k,v in marcas.items():
    print(k)
print("")

       
#Proveedores

print("En esta sección encontrarás los proveedores con su respectiva marca")
print("")
# 0,1,2,3,4,5,6,7
proveedores=["Angelica Marín - Lenovo", "Luis Castro - Apple", "Maria Luna - Samsung", "Dora Ruiz - hp", "Sonia Castro - Huawei", "Daniel Ruiz - Motorola", "Luisa Niño - Xiaomi", "Maria Lopez - Asus"]
print(proveedores[0])
print(proveedores[1])
print(proveedores[2])
print(proveedores[3])
print(proveedores[4])
print(proveedores[5])
print(proveedores[6])
print("")
print("Proveedores modificados")
print("")
print("")

#Referencias

print("Aquí puedes ver las referencias de los productos")
print("")
def Computadores():
    print()
def Portatiles():
    print
def Celulares():
    print
def Relojes_inteligentes():
    print
def Tabletas():
    print
referencias={"Computadores":10123, "Portatiles" :15610, "Celulares":135460, "Relojes inteligentes":1241650, "Tabletas":15410,}
for k,v in referencias.items():
    print(k,v)
print("")
referencias["Computadores"]=65555556
referencias["Portatiles"]=111111
print("referencias modificada:")
print("")
for k,v in referencias.items():
    print(k,v)
print("")
busca=input("Escriba el equipo que quiere buscar")
if busca == referencias:
    print(referencias)
else:
    print("Resultado:", referencias.get(busca, "No se encontro el equipo"))
busca=input("Escriba el equipo que quiere buscar")
busca == referencias
print("Resultado:", referencias.get(busca, "Se encontro el equipo"))
print("")