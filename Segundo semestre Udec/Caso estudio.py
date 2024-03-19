class Mensajes:
    def Titulo(self):
        return "\n\x1b[1;34mBienvenido al Billar Changosss\x1b[0;37m"
    def Agradecer(self):
        return "\x1b[1;32mMuchas gracias, esperamos vuelvas pronto\x1b[0;37m"
class Mesa:
    def __init__(self,tipo,cantidad_jugadores,tiempo):
         self.__tipo = tipo
         self.__cantidad = cantidad_jugadores
         self.__tiempo = tiempo
    def get_tipo(self):
        return self.__tipo
    def get_cantidad(self):
        return self.__cantidad
    def get_tiempo(self):
        return self.__tiempo
class Precio:
    def __init__(self):
        self.tipos = {"Pool":3000,
              "Libre":5000,
              "Tres bandas":6500}
    def devolver_valor(self,ronda):
        if ronda.get_tipo() in self.tipos: 
            return self.tipos[ronda.get_tipo()] 
    def calcular_precio(self,tipo,tiempo):
        valor_pagar = tipo*tiempo 
        return valor_pagar
    def precio_por_jugador(self,valor,jugadores):
        valor_individual = valor//jugadores
        return valor_individual
mensajes = Mensajes()
print(mensajes.Titulo()) 
while True:
    Tipo = input("""
            Elige el tipo de juego que deseas jugar: 
             1. Pool (P) 
             2. Libre (L)
             3. Tres bandas (T) -> """).capitalize()
    if Tipo == "P":
        Tipo = "Pool"
        break
    elif Tipo == "L":
        Tipo = "Libre"
        break
    elif Tipo == "T":
        Tipo = "Tres bandas"
        break
    print("\x1b[1;31mPor favor seleccione un carácter de la lista\x1b[0;37m")
print("\n")
while True:
    try:
        jugadores = int(input("Ahora ingresa la cantidad de amigos que van a jugar -> "))
        break
    except:
        print("\x1b[1;31mDebes ingresar un número entero, animal\x1b[0;37m")
while True:
    try:
        horas = float(input("Ingrese el tiempo en horas que van a jugar -> "))
        if horas >=1:
            pass
        else: 
            print("\x1b[1;31mEl valor debe ser superior a 1 hora\x1b[0;37m")
        break
    except:
        print("\x1b[1;31mDebe ingresar un valor numérico\x1b[0;37m")
Ronda1 = Mesa(Tipo,jugadores,horas)
precio = Precio()
print("\n")
print(f"La Cantidad de jugadores es de: {jugadores}")
print(f"El tipo de Mesa es: {Tipo}")
print(f"El tiempo jugado es de: {horas}h")
valor_partida=precio.calcular_precio(precio.devolver_valor(Ronda1),Ronda1.get_tiempo())
print(f"El Valor de la cuenta es de {valor_partida}$")
while True:
    Rta=input("¿Desea el precio por persona? (S),(N) ").capitalize()
    if Rta=="S":
        valor_individual = precio.precio_por_jugador(valor_partida,Ronda1.get_cantidad())
        print(f"El Valor de la cuenta por persona es de {valor_individual}$")
        break
    elif Rta == "N":
        print("Bueno.")
        break
    else:
        print("\x1b[1;31mPor favor seleccione una opción válida\x1b[0;37m")
print(mensajes.Agradecer())