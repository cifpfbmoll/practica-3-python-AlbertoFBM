# PRÁCTICA 3 --> EJERCICIO 6
# Pida al usuario el precio de un producto y el nombre del producto
# y muestre el mensaje con el precio del IVA (21%). Por ejemplo:
# “Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en
# 121 euros en total”.

print("--->>> Calculadora de IVA <<<---")
print("Ponga el precio y el producto que quiera comprar y el IVA \
correspondiente.")
print("EL IVA puede ser del 21%, del 10% o del 4%.")

producto = input("Producto: ")
precio = float(input("Precio: "))
iva = float(input("% IVA: "))

if (iva == 21):
    precio_final_21 = precio + (precio * 0.21)
    print("Su", producto,"con el 21% de IVA vale", precio_final_21,"€")
elif (iva == 10):
    precio_final_10 = precio + (precio * 0.10)
    print("Su", producto,"con el 10% de IVA vale", precio_final_10,"€")
else: 
    precio_final_4 = precio + (precio * 0.04)
    print("Su", producto,"con el 4% de IVA vale", precio_final_4,"€")