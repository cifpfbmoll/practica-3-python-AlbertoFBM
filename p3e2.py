# PRÁCTICA 3 --> EJERCICIO 2
# Pida al usuario el espacio recorrido por un coche y el tiempo
# que ha tardado en horas y que calcule a qué velocidad media
# había realizado el recorrido.

print("Calculadora de velocidad media.")
print("Ponga el espacio recorrido de su coche y el tiempo que ha tardado en \n\
horas.")
espacio_recorrido = float(input("Espacio recorrido: ejemplo(100km): "))
tiempo = float(input("Tiempo transcurrido en horas: "))

velocidad = float(espacio_recorrido / tiempo )
print("Usted iba a una velocidad media de", velocidad, "km/h.")
