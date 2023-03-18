
contMultiplosDos = 0
contMultiplosTres = 0

for i in range(3):
    numero = int(input("Ingrese un numero: "))
    if(numero % 2 == 0):
        contMultiplosDos += 1
    elif(numero % 3 == 0):
        contMultiplosTres += 1
    else: print("")


multiplosTresyDos = contMultiplosDos + contMultiplosTres
print ("Cantidad de numeros multiplos de DOS: ", contMultiplosDos)
print ("Cantidad de numeros multiplos de TRES: ", contMultiplosTres)
print ("Cantidad de numeros multiplos de DOS y TRES : ", multiplosTresyDos)