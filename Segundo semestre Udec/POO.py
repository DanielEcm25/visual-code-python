#Clases y métodos 
#encapsulamiento es ocultar el funcionamiento interno 
class Bebida:
    def __init__(self,name):
        self.__name = name 
    def ObtenerNombreBebida(self):
        return self.__name
class Cerveza(Bebida):
    _contador = 0
    def __init__(self, name, alcohol, marca):
        super().__init__(name)
        self.__alcohol = alcohol
        self.__marca = marca
        Cerveza._contador +=1 
    def ObtenerNombreBebida(self):
        return f"Soy una cerveza {super().ObtenerNombreBebida()} de la marca {self.__marca} con grado de alcohol {self.__alcohol}"
    @staticmethod
    def ObtenerContadorCervezas():
        return f"se han creado {Cerveza._contador} cervezas"
cerveza = Cerveza("Poker",4.0,"Bavaria")
cerveza1 = Cerveza("Aguila",4.0,"Babaria")
cerveza2 = Cerveza("Corona",4.5,"Mexicana")
#poliformismo se ejecuta en orden 
print(cerveza.ObtenerNombreBebida())
print(Cerveza.ObtenerContadorCervezas())
