'''Escribir un programa que pida un numero al usuario y muestre las tablas de multipl
icar de ese numero'''

print("Hola, este programa te mostrará la tabla de multiplicar del numero que ingreses")
Numero = (input("Por favor ingresa un número-> "))
a=0
while True:
    try:
        Numero1 = int(Numero)
        break
    except:
        print("Te pedí un número")
for a in range(1,11):
    print(f"{Numero} * {a} = ",Numero1*a)

 