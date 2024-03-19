'''Pedir al usuario que ingrese 2 números, después, se debe mostrar el rango de
esos 2 números, pero, solo imprimiendo los números que sean impares.
'''

print("Hola, este programa te mostrará los números primos comprendidos entre dos números que ingreses")
num1 = int(input("Por favor ingresa el primer número-> "))
num2 = int(input("Por favor ingresa el segundo número-> "))
a = 0
for i in range(num1,num2+1):
    if i % 2 != 0:
        print(i)
