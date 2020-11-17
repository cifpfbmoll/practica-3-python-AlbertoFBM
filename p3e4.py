# PRÁCTICA 3 --> EJERCICIO 4
# Pide al usuario que introduzca 3 calificaciones, y 
# calcule la media de estas.

print("Calculadora de medias: (máximo 3 notas)")

cualificacion_1 = float(input("Ponga la primera nota: "))
cualificacion_2 = float(input("Ponga la segunda nota: "))
cualificacion_3 = float(input("Ponga la tercera nota: "))

media_de_notas = (cualificacion_1 + cualificacion_2 + cualificacion_3) / 3
print("Su media es de", media_de_notas)