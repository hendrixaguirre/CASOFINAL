Proceso CosméticosCastillo
	// Se definen las variables
	Definir inventario como cadena
	dimension inventario[100,3] // Matriz para almacenar el inventario 
	definir totalProductos Como Entero
	definir opcioon como entero
	definir nombre como cadena 
	definir cantidad Como Entero
	definir precio Como Real
	
	totalProductos=0
	// Se establece el ciclo para que se repita continuamente
	Repetir 
		Escribir "/-------- MENÚ COSMÉTICOS CASTILLO --------\"
		Escribir "1. Agregar producto"
		Escribir "2. Actualizar producto"
		Escribir "3. Eliminar producto"
		Escribir "4. Mostrar inventario"
		Escribir "5. Salir"
		Escribir "* Elija una opción (1/2/3/4/5): "
		Leer opcioon // Se lee la opción que elige el usuario
		
		Segun opcioon hacer
			1:
				Escribir "Ingrese el nombre del producto:"
				Leer nombre
				Escribir "Ingrese la cantidad:"
				Leer cantidad
				Escribir "Ingrese el precio:"
				Leer precio 
				
				Inventario[totalProductos + 1,1]=nombre
				inventario[totalProductos + 1,2]=ConvertirATexto(cantidad) // Se convierte la cantidad a texto
				inventario[totalProductos + 1,3]=ConvertirATexto(precio) // Se convierte el precio a texto
				
				totalProductos=totalProductos+1 
				Escribir "Producto agregado con éxito!"
			2:
				si totalProductos=0 Entonces
					Escribir "No hay productos para actualizar en el inventario"
				sino 
					Escribir "Ingrese el nombre del producto que desea actualizar:"
					leer nombre
					Definir encontrado Como Logico
					encontrado=Falso
					
					nombre=Mayusculas(nombre) // Se pasan todos los caracteres a mayuscula
					i=1
					Mientras i<=totalProductos Y encontrado=Falso Hacer
						si Mayusculas(inventario[i,1])= nombre Entonces
							encontrado = Verdadero
							Escribir "¿Qué dato desea actualizar del producto ", inventario[i,1], "?"
							Escribir "1. Nombre"
							Escribir "2. Cantidad"
							Escribir "3. Precio"
							Leer opciion
							
							Segun opciion hacer
								1:
									Escribir "Ingrese el nuevo nombre para el producto: "
									Leer nombre
									inventario[i,1]=nombre // Se cambia el nombre que había en la columna 1
									Escribir "Nombre actualizado exitosamente!"
								2:
									Escribir "Ingrese la nueva cantidad en existencia: "
									Leer cantidad 
									inventario[i,2]=ConvertirATexto(cantidad) // Se convierte la cantidad a texto
									Escribir "Cantidad en existencia actualizada exitosamente!"
								3:
									Escribir "Ingrese el nuevo precio del producto: "
									Leer precio 
									inventario[i,3]=ConvertirATexto(precio) // Se convierte el precio a texto
									Escribir "Precio del producto actualizado exitosamente!"
								De Otro Modo:
									Escribir "Opción inválida!"
							FinSegun
						FinSi
						i=i+1
					FinMientras
					
					si encontrado=Falso Entonces
						Escribir "El producto no existe en inventario!"
					FinSi
				FinSi
			3:
				si totalProductos=0 Entonces
					Escribir "No hay productos para eliminar del inventario!"
				SiNo
					Escribir "Ingrese el nombre del producto que desea eliminar del inventario: "
					Leer nombre
					Definir encontrado Como Logico
					encontrado=Falso
					nombre=Mayusculas(nombre)
					
					i=1
					Mientras i<=totalProductos Y encontrado=Falso Hacer
						si Mayusculas(inventario[i,1])=nombre Entonces
							encontrado=Verdadero
							//Se desplazan las líneas hacia arriba, para no dejar espacios vacíos
							para j=i hasta totalProductos - 1
								inventario[j,1] = inventario[j+1,1]
								inventario[j,2] = inventario[j+1,2]
								inventario[j,3] = inventario[j+1,3]
							FinPara
							inventario[totalProductos,1]= ""
							inventario[totalProductos,2]= ""
							inventario[totalProductos,3]= ""
							totalProductos = totalProductos - 1
							Escribir "Producto eliminado del inventario exitosamente!"
						FinSi
						i = i + 1
					FinMientras
					si encontrado=Falso Entonces
						Escribir "El producto a eliminar no fue encontrado en el inventario!"
					FinSi
				FinSi
			4: 
				si totalProductos=0 Entonces
					Escribir "No hay productos en el inventario!"
				sino 
					Escribir "Inventario actual:"
					para i=1 Hasta totalProductos
						Escribir i, ".", inventario[i,1], " / cantidad: ", inventario[i,2], " / precio: C$", inventario[i,3]
					FinPara
				FinSi
			5:
				Escribir "Gracias por hacer uso del sistema. Hasta luego!"
				salir=Verdadero
			De Otro Modo:
				Escribir "Opción inválida, intente de nuevo!"
		FinSegun
	Hasta Que salir=Verdadero	
		
FinProceso
