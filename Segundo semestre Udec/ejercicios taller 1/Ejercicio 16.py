'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).
'''

print("Hola, este programa te mostrará por pantalla cuantos años has cumplido")
edad = int(input("Por favor ingresa tu edad -> "))
a = 1
while a <=edad:
    print(f"Has cumplido {a} años") 
    a+=1