'''Con el siguiente diccionario, debes crear un programa que pregunte al usuario por
un número; el programa debe imprimir el jugador al que hace referencia ese
número'''

Jugadores = {1:"Casillas",15:"Ramos",
             3:"Pique",5:"Puyol",
             11:"Capdevila",14:"Xabi Alonso",
             16:"Busquets",8:"Xavi Hernández",
             18:"Pedrito",6:"Iniesta",
             7:"Villa"
             }
print("Hola, este programa te mostrará el nombre de un jugador de la selección de España según su dorsal")
while True:
    Numero = int(input("Por favor ingresa el número del jugador-> "))
    if Numero in Jugadores:
        print(f"El jugador con el dorsal {Numero} es: ",Jugadores[Numero])
        break
    else: 
        print(f"El jugador {Numero} no se encuentra")