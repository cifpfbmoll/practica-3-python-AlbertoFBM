# PRÁCTICA 3 --> EJERCICIO 7
# Pida al usuario tres número que serán el día, mes y año.
# Comprueba que la fecha introducida es válida.

print("Ponga una fecha: ejemplo: 12/3/2020")

dia = int(input("ponga el dia: "))
mes = int(input("ponga el mes: "))
año = int(input("ponga el año: "))

if (dia>31) or (dia<=0) or (mes<=0) or (mes>12) or (año<=0):
    print(dia,"/",mes,"/", año,"--> La fecha es incorrecta!!")
elif (mes==2) and (dia>29):
    print("Dia incorrecto! Febrero no tiene dia", dia)
elif (mes==4) and (dia>30):
    print("Dia incorrecto! Abril no tiene dia", dia)
elif (mes==6) and (dia>29):
    print("Dia incorrecto! Junio no tiene dia", dia)
elif (mes==9) and (dia>30):
    print("Dia incorrecto! Septiembre no tiene dia", dia)
elif (mes==11) and (dia>30):
    print("Dia incorrecto! Noviembre no tiene dia", dia)
else: 
    print(dia,"/", mes,"/", año,"--> La fecha es correcta!!")