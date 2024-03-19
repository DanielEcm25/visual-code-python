class Persona: 
    def __init__(self,nombre,edad):
        self ._nombre=nombre
        self ._edad=edad 
    def Saludar(self):
        return f"Hola, soy {self._nombre} y mi edad es {self._edad} años"

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        Persona.__init__(self,nombre,edad)
        self.__carrera=carrera
    def carrera(self):
        return f"{super(). Saludar()}. Estudio la carrera de {self. __carrera}"
    
class EstudianteUniversidad(Estudiante):
    __ContadordeEstudiantes = 0
    def __init__(self,nombre,edad,carrera,lugar):
        Estudiante.__init__(self,nombre,edad,carrera)
        self.__lugar = lugar
        EstudianteUniversidad.__ContadordeEstudiantes += 1
    def getInformacionEstiudiante (self):
        return f"{super().carrera()} y vivo en {self.__lugar}"  
    @staticmethod
    def getContadordeEstudiantes():
        return f"Se han creado {EstudianteUniversidad.__ContadordeEstudiantes} estudiantes"
    
Diego = EstudianteUniversidad("Diego Sánchez",19,"Ing. de sistemas","Sutatausa")          
Daniel = EstudianteUniversidad("Daniel Contreras",18,"Ing. de sstemas","Ubaté")
Michael = EstudianteUniversidad("Michael Suárez",18,"Ing. de sistemas","Carmen de Carupa")
print(Diego.getInformacionEstiudiante())
print(Daniel.getInformacionEstiudiante())
print(Michael.getInformacionEstiudiante())
print(EstudianteUniversidad.getContadordeEstudiantes())