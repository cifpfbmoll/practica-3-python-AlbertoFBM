# PRÁCTICA 3 --> EJERCICIO 3
# ¿Qué función te informa del tipo de dato tiene almacenado una variable?
# Haz una prueba con los distintos tipos de datos que conoces.

print("--> La función type es la función que nos retorna el tipo de datos de una \
variable <--")
print("Por ejemplo: ")

a = int(input("Pon un elemento de tipo entero --> a= "))
b = float(input("Pon un elemento de tipo decimal --> b= "))
c = input("Pon un elemento de tipo cadena --> c= ")

print("a= ", type(a))
print("b= ", type(b))
print("c= ", type(c))