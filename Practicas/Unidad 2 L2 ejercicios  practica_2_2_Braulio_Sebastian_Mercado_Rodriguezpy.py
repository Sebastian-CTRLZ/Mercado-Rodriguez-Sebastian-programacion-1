##Ejercicio 1 primero##
numero = 7
par= numero % 2 ==0
print("El mumero(",par,")es par")
## debo especificar que el numero es par, si no no jala

##Ejercicio 2##
numero="5"
numero2="3"
sumatexto= numero + numero2
print(f"sin convertir: {numero} + {numero2} = {sumatexto}")
resultado_con_numero=int(numero)+int(numero2)
print(f"resultado de la suma es {resultado_con_numero}")
##:V

##Ejercicio 3##
nombre = "Braulio"
Edad = 19
Estatura = 1.70
es_estudiante = True
print("Reporte")
print("Nombre:", nombre, type(nombre))
print("Edad:", Edad, type(Edad))
print("Estatura:", Estatura, type(Estatura))
print("Es estudiante:", es_estudiante, type(es_estudiante))
##Extra##
mensaje = "hola soy " + nombre + " y tengo " + str(Edad) + " años y mido " + str(Estatura)
print(mensaje)
##

##Ejercicio 4##
v1 = 5
v2 = 5
print(f" {v1}+{v2} es {v1+v2}")
print(f" {v1}-{v2} es {v1-v2}")
print(f" {v1}*{v2} es {v1*v2}")
print(f" {v1}/{v2} es {v1/v2}")
## las operaciones de dos variables se tienen que usar print(f"etc)si no solo imprimira el texto dentro de los parentesis

##Ejercicio 5##
v1= 5
v2= 5
print("divison:",v1/v2)
print("residuos:",v1%v2)

##Soy vulnerable a tu lado más amable, soy carcelero de tu lado mas grosero
##Ejercicio 6##
##numeros distintos##
a = 20
b = 5
mayor = a > b
menor = a < b
igual = a == b
distinto = a != b
print(f"{a} > {b} es {mayor}")
print(f"{a} < {b} es {menor}")
print(f"{a} == {b} es {igual}")
print(f"{a} != {b} es {distinto}")

##numeros iguales##
a = 77
b = 77
mayor = a > b
menor = a < b
igual = a == b
distinto = a != b
print(f"{a} > {b} es {mayor}")
print(f"{a} < {b} es {menor}")
print(f"{a} == {b} es {igual}")
print(f"{a} != {b} es {distinto}")

##Asi si funciona con los corchetes, si no se muere la cosa

##Ejercicio 7##
edad = 18
Altura = 1.60
es_mayor_de_edad = edad >=18
es_alto = Altura <=1.170
es_mayor_de_edad_y_alto = es_mayor_de_edad and es_alto
es_mayor_de_edad_o_alto = es_mayor_de_edad or es_alto
es_mayor_de_edad_no = not es_mayor_de_edad

print(f"es mayor de edad: {es_mayor_de_edad}")
print(f"es alto: {es_alto}")
print(f"es mayor de edad y alto: {es_mayor_de_edad_y_alto}")
print(f"es mayor de edad o alto: {es_mayor_de_edad_o_alto}")
print(f"no es mayor de edad: {es_mayor_de_edad_no}")

##Las expresiones booleanas serian como edad y altura. ta complicado
##Ejercicio 8##
v1 = 6
v2 = 8
v3 = 8
promedio = (v1 + v2 + v3)/3
positivo = promedio >= 6 
print(f"calificaciones: {v1}, {v2}, {v3}")
print(f"promedio: {promedio}")
print(f"está aprobado: {positivo}")

v1 = 6
v2 = 5
v3 = 4
promedio = (v1 + v2 + v3)/3
positivo = promedio >= 6 
print(f"calificaciones: {v1}, {v2}, {v3}")
print(f"promedio: {promedio}")
print(f"está aprobado: {positivo}")
##Promedio, recuerda con promedio

##Ejercicio 9##

##combinacion 1##
edad = 19
nacionalidad = "China"
es_elegible= edad >=17 and nacionalidad == "China"
es_elegible_or = edad > 17 or nacionalidad == "China"
print(f"edad: {edad}")
print(f"nacionalidad: {nacionalidad}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##combinacion 2##

edad = 20
nacionalidad = "mexicana"
es_elegible= edad >=17 and nacionalidad == "mexicana"
es_elegible_or = edad > 17 or nacionalidad == "mexicana"
print(f"edad: {edad}")
print(f"nacionalidad: {nacionalidad}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##combinacion 3##

edad = 25
nacionalidad = "Peruana"
es_elegible= edad >=17 and nacionalidad == "Peruana"
es_elegible_or = edad > 17 or nacionalidad == "Peruana"
print(f"edad: {edad}")
print(f"nacionalidad: {nacionalidad}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##combinacion 4##

edad = 15
nacionalidad = "Chileno"
es_elegible= edad >=17 and nacionalidad == "Chileno"
es_elegible_or = edad > 17 or nacionalidad == "Chileno"
print(f"edad: {edad}")
print(f"nacionalidad: {nacionalidad}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##Soy vulnerable a la hora de hacer ejercicios, pero me gusta aprender y mejorar mis habilidades en programación.
import webbrowser

# que buna rola la verdad de dios
url = "https://music.youtube.com/watch?v=f0SG-aGlOxE&si=Gbmz0XkOJZS24bPZ"

# Abre la URL en el navegador predeterminado con el .webbrowser
webbrowser.open(url)