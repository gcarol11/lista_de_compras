lista_compras = []


while True:
    
    print("\nMenú de opciones:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1/2/3/4): ")
    
    if opcion == '1':
        
        articulo = input("Ingrese el nombre del artículo a agregar: ")
        lista_compras.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")
    
    elif opcion == '2':
       
        if lista_compras:
            print("Lista de compras actual:")
            for i, item in enumerate(lista_compras):
                print(f"{i}. {item}")
            
            try:
                indice = int(input("Ingrese el índice del artículo a eliminar: "))
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"Artículo '{eliminado}' eliminado de la lista.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print("La lista está vacía.")
    
    elif opcion == '3':
    
        if lista_compras:
            print("Lista de compras:")
            for i, item in enumerate(lista_compras):
                print(f"{i}. {item}")
        else:
            print("La lista está vacía.")
    
    elif opcion == '4':
        
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
