# PRÁCTICA 3 --> EJERCICIO 5
# Pida un número que como máximo tenga tres cifras (por ejemplo serían 
# válidos 1, 99 i 213 pero no 1001). Si el usuario introduce un número
# de más de tres cifras debe un informar con un mensaje de error como
# este “ERROR: El número 1005 tiene más de tres cifras”.

numero = int(input("Ponga un número de MÁXIMO 3 cifras: "))
if (numero < 1000):
    print("Bien hecho, menos mal que no has puesto más de 3 cifras...")
else:
    print(f"INSENSATO!! EL NÚMERO {numero} TIENE MÁS DE 3 CIFRAS!!")