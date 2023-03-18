
#opcion = 1
#cuentas = []
#while opcion != 10:
 #cuenta = {}
 #cuenta["cuentaUno"] = int(input("CuentaUno" ))
 #cuenta["cuentaDos"] = int(input("CuentaDos" ))
 #cuenta["cuentaTres"] = int(input("CuentaTres" ))
 

 #.append(cuenta)


#opcion +=1

#print(cuentas.sort(reverse=True))
cuentas = []

for i in range(3):
    cuenta = {}
    cuenta["cuenta"] = int(input("Cuenta: " ))
    cuentas.append(cuenta)


ordenados = sorted(cuenta["cuenta"], reverse=True)

print(ordenados)

