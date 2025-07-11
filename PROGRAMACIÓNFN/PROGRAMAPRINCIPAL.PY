#Inventario de venta de cosméticos Castillo

import Funciones # Se importan todas las funciones ya antes definidas

#Se define función para llamar al menú
def menu():
    while True:
        print ("---- Menú ----")
        print ("1. Agregar producto")
        print ("2. Actualizar producto")
        print ("3. Eliminar producto")
        print ("4. Mostrar inventario")
        print ("5. Salir")

        opción=input("Seleccione una opción (1/2/3/4/5): ")
        if opción=="1":
            Funciones.agregarProducto() # Se llama a la función agregarProductos del módulo Funciones
        elif opción=="2":
            Funciones.actualizarProducto() # Se llama la función actualizarProducto del módulo Funciones
        elif opción=="3":
            Funciones.eliminarProducto() # Se llama a la función eliminarProducto del módulo Funciones
        elif opción=="4":
            Funciones.mostrarInventario() # Se llama a la función mostrarInventario del módulo Funciones
        elif opción=="5":
            print ("Gracias por hacer uso del sistema. Hasta luego!")
            break
        else: 
            print ("Opción inválida. Intente de nuevo!")

# Si se cumple la función inicio se llama a las funciones cargarInventario y menu
if Funciones.inicio():
    Funciones.cargarInventario()
    menu()