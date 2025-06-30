#Inventario de venta de cosméticos Castillo
import os
import pwinput

#Se utilizará una lista vacía para guardar el inventario
inventario=[]

#Función para cargar el archivo usuarios.txt
def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open ("usuarios.txt", "r") as archivo: # Se abre el archivo en modo de lectura
            for linea in archivo:
                usuario, clave = linea.strip().split(",") # strip para eliminar espacios en blanco y split para separar líneas con coma
                usuarios[usuario] = clave
    return usuarios

#Se define función para autenticación
def inicio():
    print ("--------------INICIO DE SESIÓN--------------")
    usuarios = cargar_usuarios()
    intentos = 0
    maximo_intentos=3

    while intentos < maximo_intentos:
        usuario = input("Usuario: ")
        clave_ingresada = pwinput.pwinput("Contraseña: ", mask="*")
        if usuario in usuarios and usuarios[usuario] == clave_ingresada:
            print ("Acceso permitido\n")
            return True
        else:
            intentos +=1
            print (f"Usuario o contraseña incorrectos. Intento {intentos}/{maximo_intentos}\n")
            
    print ("Superó el número de intentos permitidos!")
    return False

#Se define función para cargar los datos de los productos en inventario
def cargarInventario():
    try:
        with open("inventario.txt","r", encoding="utf-8") as archivo:
            for linea in archivo:
                producto=linea.strip().split(",")
                inventario.append(producto)
    except FileNotFoundError:
        pass 

#Se define función para guardar el inventario en un archivo de texto
def guardarInventario():
    with open("inventario.txt","w", encoding="utf-8") as archivo:
        for producto in inventario:
            archivo.write(",".join(producto) + "\n")
#Se define función para agregar los productos
def agregarProducto():
    nombre=input("Ingrese el nombre del producto: ").upper() # upper para cambiar a mayúsculas todas las letras
    for producto in inventario:
        if producto[0].strip().upper() == nombre.strip().upper():
            print ("El producto ya existe en el inventario!")
            return

    cantidad=int(input("Ingrese la cantidad disponible: "))
    precio=float(input("Ingrese el precio por unidad en córdobas: "))

    producto=[nombre,str(cantidad),str(precio)] # str para cambiar el valor de entero a cadena
    inventario.append(producto)
    
    with open("inventario.txt","a",encoding="utf-8") as archivo:
        archivo.write(",".join(producto) + "\n")

    print ("Producto agregado con éxito al inventario!")

#Se define función para mostrar el inventario
def mostrarInventario():
    print ("\n Inventario actual:")
    if len(inventario)==0:
        print ("No hay productos para mostrar "
               "en el inventario!\n")
    else: 
        for i in range(len(inventario)):
            producto=inventario[i]
            print (f"{i+1}. {producto[0]} - cantidad: {producto[1]} - precio: C${producto[2]}")
        print ()

#Se define función para actualizar producto

def actualizarProducto():
    if len(inventario)==0:
        print ("No hay productos para actualizar en el inventario!")
    else:
        nombre=input("Ingrese el nombre del producto que desea actualizar: ").upper()
        encontrado=False

        for i in range(len(inventario)):
            if inventario[i][0].upper() == nombre:
                encontrado=True
                print (f"¿Qué dato del producto {inventario[i][0]}?")
                print ("1. Nombre")
                print ("2. Cantidad")
                print ("3. Precio")
                opcion=input("Seleccione una opción: ")

                if opcion=="1":
                    nuevoNombre=input("Ingrese el nuevo nombre para el producto: ")
                    inventario[i][0]=nuevoNombre.upper()
                    print ("Nombre del producto actualizado exitosamente!")
                elif opcion=="2":
                    nuevaCantidad=int(input("Ingrese la nueva cantidad en existencia del producto: "))
                    inventario[i][1]=str(nuevaCantidad)
                    print("Cantidad en existencia del producto actualizada exitosamente!")
                elif opcion=="3":
                    nuevoPrecio=float(input("Ingrese el nuevo precio del producto: "))
                    inventario[i][2]=str(nuevoPrecio)
                    print("Precio del producto actualizado exitosamente!")
                else:
                    print ("Opción inválida!")
                guardarInventario()
                break
        if not encontrado:
            print ("El producto no existe en el inventario!")

#Se define la función para eliminar productos
def eliminarProducto():
    if len(inventario)==0:
        print ("No hay productos para eliminar en el inventario!")
    else:
        nombre=input("Ingrese el nombre del producto que desea eliminar del inventario: ").upper()
        encontrado=False

        for i in range(len(inventario)):
            if inventario[i][0].upper()==nombre:
                eliminado=inventario.pop(i) # pop() elimina el elemento en la posición indicada
                guardarInventario()
                print(f"El producto {eliminado} fue eliminado del inventario exitosamente!")
                encontrado=True
                break
        if not encontrado:
            print ("El producto que desea eliminar no existe en el inventario!")