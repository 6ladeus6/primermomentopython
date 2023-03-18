
opcion = 1
ciclistas = []
contId = 1
while opcion != 0:
    print("1: Ingrese el ciclista: ")
    print("2: Mostrar la tabla de posiciones: ")
    print("3: Editar tiempo de ciclista: ")
    print("4: Eliminar una ciclista por ID: ")
    print("0: Salir: ")
    opcion = int(input("Escoja una opción: "))
    if(opcion == 1):
        ciclista = {}
        ciclista["codigo"] = contId
        ciclista["nombre"] = input("Nombre ciclista: ")
        ciclista["edad"] = float(input("Edad: "))
        ciclista["pais"] = input("Pais: ")
        ciclista["equipo"] = input("Equipo: ")
        ciclista["tiempo"] = int(input("Tiempo: "))

        ciclistas.append(ciclista)
        print("Ciclista registrado...")
        contId = contId + 1
    elif(opcion == 2):
        for ciclista in ciclistas:
            print(ciclista)
    elif(opcion == 3):
        buscarciclista = int(input("Digite el codigo para buscar el ciclista: "))
        for ciclista in ciclistas:
            if(buscarciclista == ciclista["codigo"]):
                print("El tiempo actual del ciclista es: ",ciclista["tiempo"])
                ciclista["tiempo"] = float(input("Digite el nuevo tiempo: "))
                print("El nuevo tiempo del ciclista " , ciclista["nombre"]  ," Con codigo ", ciclista["codigo"] ,"es: " , ciclista["tiempo"])
            else: print("El ciclista no registra!...")
    elif(opcion == 4):
        buscarciclista = int(input("Digite el codigo para buscar el ciclista: "))
        for ciclista in ciclistas:
            if(buscarciclista == ciclista["codigo"]):
                   ciclista["codigo"] = ""
                   ciclista["nombre"] =""
                   ciclista["edad"] =""
                   ciclista["pais"] =""
                   ciclista["equipo"] =""
                   ciclista["tiempo"] =""
            else: print("El ciclista no registra!...")
    elif(opcion == 0):
        pass
    else: print("La opcion ingresada no es valida")
    

