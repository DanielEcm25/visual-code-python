'''En el siguiente diccionario se encuentran capitales de los paises en el mundo, deb
es realizar un programa que pida un pais al usuario, y muestre la capital de ese pa
is, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje dici
endo que ese pais no se encuentra.'''

Capitales = {"Guatemala": "Ciudad de Guatemala",
             "El Salvador":"San Salvador",
             "Honduras":"Honduras",
             "Nicaragua":"Managua",
             "Costa Rica":"San José",
             "Panamá":"Panamá",
             "Argentina":"Buenos Aires",
             "Colombia":"Bogotá",
             "Venezuela":"Caracas",
             "España":"Madrid"}
print("Hola, este programa te dirá la capital del país que ingreses")
while True:
    Pais = input("Por favor ingresa el nombre del país-> ").title()
    if Pais in Capitales:
        print(f"La capital de {Pais} es:", Capitales[Pais])
        break
    else: 
        print(f"El país ingresado ({Pais}) no se encuentra")