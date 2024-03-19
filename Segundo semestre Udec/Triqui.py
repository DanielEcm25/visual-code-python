#Juego de triqui usando las librerías de tkinter y random
#Hecho por Daniel Esteban Contreras Motoa
#Segundo Semestre Programación I
from tkinter import *
import random
pantalla = Tk()
pantalla.title("Triqui al estilo Pro-Gramer")
jugadores = ["X","O"]
jugador_usuario = random.choice(jugadores)
creditos = Label(text="Hecho por: Daniel Esteban Contreras Motoa :3",font=('consolas',20),foreground="red3")
creditos.pack(side="bottom")
casillas = [[0,0,0],
           [0,0,0],
           [0,0,0]]
subtitulo = Label(text = "Turno de "+jugador_usuario,font=('consolas',35),foreground="Royalblue2")
subtitulo.pack(side="top")

def definir_color_inicial(jugador,conjunto):
    if jugador == conjunto[0]:
        subtitulo.config(text="Turno de "+jugador,foreground="royal blue")
    else:
        subtitulo.config(text="Turno de "+jugador,foreground="red2")
def siguiente_turno(fila,columna):
    global jugador_usuario
    if casillas[fila][columna]['text'] == ''and comprobar_ganador() is False:
        if jugador_usuario == jugadores[0]:
            casillas[fila][columna]['text'] = jugador_usuario
            if comprobar_ganador() is False:
                jugador_usuario  = jugadores[1]
                subtitulo.config(text=("Turno de "+jugadores[1]),foreground="red2")
                casillas[fila][columna].config(foreground="blue2")
            elif comprobar_ganador() is True:
                subtitulo.config(text=("Las "+jugador_usuario[0]+' ganan!'),foreground="blue2")
                casillas[fila][columna].config(foreground="blue2")
            elif comprobar_ganador() == "Empate":
                subtitulo.config(text=("Es un empate!"),foreground="goldenrod")
                casillas[fila][columna].config(foreground="blue2")
        else:
            casillas[fila][columna]['text'] = jugador_usuario
            if comprobar_ganador() is False:
                jugador_usuario = jugadores[0]
                subtitulo.config(text=("Turno de "+jugadores[0]),foreground="royal blue")
                casillas[fila][columna].config(foreground="red2")
            elif comprobar_ganador() is True:
                subtitulo.config(text=("Las "+jugadores[1]+' ganan!'),foreground="red2")
                casillas[fila][columna].config(foreground="red2")
            elif comprobar_ganador() == "Empate":
                subtitulo.config(text=("Es un empate!"),foreground="goldenrod")
                casillas[fila][columna].config(foreground="red2")
def comprobar_ganador():
    for fila in range(3):
        if casillas[fila][0]['text'] == casillas[fila][1]["text"]== casillas[fila][2]['text'] !="":
            casillas[fila][0].config(bg="spring green")
            casillas[fila][1].config(bg="spring green")
            casillas[fila][2].config(bg="spring green")
            return True
    for columna in range(3):
        if casillas[0][columna]['text'] == casillas[1][columna]["text"]== casillas[2][columna]['text'] !="":
            casillas[0][columna].config(bg="spring green")
            casillas[1][columna].config(bg="spring green")
            casillas[2][columna].config(bg="spring green")
            return True
    if casillas[0][0]['text'] == casillas[1][1]['text'] == casillas[2][2]['text'] != "":
        casillas[0][0].config(bg="spring green")
        casillas[1][1].config(bg="spring green")
        casillas[2][2].config(bg="spring green")
        return True
    elif casillas[0][2]['text'] == casillas[1][1]['text'] == casillas[2][0]['text'] != "":
        casillas[0][2].config(bg="spring green")
        casillas[1][1].config(bg="spring green")
        casillas[2][0].config(bg="spring green")
        return True
    elif espacios_vacios() is False:
        for fila in range(3):
            for columna in range(3):
                casillas[fila][columna].config(bg="yellow")
        return "Empate"
    else:
        return False
def espacios_vacios():
    espacios = 9
    for fila in range(3):
        for columna in range(3):
            if casillas[fila][columna]['text'] != '':
                espacios-=1
    if espacios == 0:
        return False
    else:
        return True
def nuevo_juego():
    global jugador_usuario
    jugador_usuario = random.choice(jugadores)      
    for fila in range(3):
        for columna in range(3):
            casillas[fila][columna].config(text="",bg="snow")
    definir_color_inicial(jugador_usuario,jugadores)  
reiniciar_juego = Button(text='Reiniciar juego',font=('consolas',10), command=nuevo_juego,foreground="green4",activeforeground="red")
reiniciar_juego.pack(side="top")
frame = Frame(pantalla)
frame.pack()
definir_color_inicial(jugador_usuario,jugadores)
for fila in range(3):
    for columna in range(3):
        casillas[fila][columna] = Button(frame, text='',font=('consolas',45),width=5,height=2, activeforeground="linen", bg="snow",
                                      command=lambda row=fila,column=columna: siguiente_turno(row,column)) 
        casillas[fila][columna].grid(row=fila,column=columna)
pantalla.mainloop()