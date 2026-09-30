nombre= "Burnice White"
edad = 25
Ciudad = "La Periferia"
print(nombre,edad,Ciudad)
##Comentario: Con personajes reconocibles es mas facil establecer mis variables##

#Ejercicio: Actualizar un contador##
contador= 0
contador = contador + 1
print(contador)
contador = contador + 1
print(contador)
contador = contador + 1
print(contador)
contador = contador + 1
print(contador)

##comentarios de la actividad: Contador mas contador debe ir acompada de un print##

##EJERCICIO: Constante de conversion##
Pulgada = 5
CONSTANTE= 2.54 
print("La medida en centimetros es", Pulgada*CONSTANTE)
##coMENTARIOS: DEJA EL NUMERO CERRADO O SE PUDRE todo##.

##AREA DE UN RECTANGULO##
base = 15
altura = 30
Area = base*altura
print(Area)
##Comentario: Area ya te da todo##

Iva = 0.16
Precio = float(input("Ingrese el puto precio:"))
Precio_Final = Precio+(Precio*Iva)
print(Precio_Final)
##Comentario: PON EL PINCHE FLOAT PORQUE SI NO, NO JALA##

A = 6
B = 7
Temp= A
Temp= B

print(A,B)
print(B,A)
##Comentarios: Aver si no esta tan facil o si la cajetie)

##Identificar tipos con type)##

V1= 69
V2 = 43.33
V3 = "Lalatina"
V4 = True
int(V1)
float(V2)
str(V3)
bool(V4)
print 
(type(V1))
print(type(V2))  
print(type(V3))
print(type(V4))
###Comentario: Print type es para identificar el tipo de variable que es, si es int, float,lutr o bool.
##//ACTIVIDAD: Convertir tipos##
texto = "25"
numero_convertido = int(texto)

print("Texto original:", texto, "->", type(texto))
print("Convertido a entero:", numero_convertido, "->", type(numero_convertido))

# 2. Conversión de entero a texto con str()
numero = 100
texto_convertido = str(numero)

print("Número original:", numero, "->", type(numero))
print("Convertido a texto:", texto_convertido, "->", type(texto_convertido))

V = 3
C = 2
Z = V + C
print(Z)
V = 8
C = 3
class mayor:
	"""Determina si el primer valor es mayor que el segundo."""

	@staticmethod
	def comparar(valor_a, valor_b):
		return valor_a > valor_b


mayor_es_v = mayor.comparar(V, C)
print(mayor_es_v)
##NO le entendi pero que la tecnologia haga lo suyo##