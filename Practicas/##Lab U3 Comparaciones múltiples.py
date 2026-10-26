##Lab U3 Comparaciones múltiples
## Braulio Sebastian Mercado Rodriguez 22245258

##Ejercicio :Clasificación por edad:
edad= int(input("Porfavor ingrese su edad"))
if edad>18:
    print("Es un adulto")
elif edad>13:
    print("Es Adolecente")
else:
    print("Es menor")

##:Validar acceso (usuario y contraseña)

Usuario= input("Porfavor Ingrese su Usuario: ")
contraseña =  input("Ingrese su contraseña: ")
if Usuario== "Juri" and contraseña == "BlackSickSpider":
    print("Contraseña correcta")
##No usar el pinche & no sirve: Mejor usar el and
elif Usuario== "Juri" and contraseña != "BlackSickSpider":
    print("Contraseña Incorrecta Perro metiche")
else:
    print("Usuario No encontrado pibe")