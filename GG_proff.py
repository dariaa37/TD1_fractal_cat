#   x = naranja
#   o = celeste
#
#

from tkinter import *
import random

def siguienteTurno(fila, columna):
    global jugador

    if botones[fila][columna]['text'] == "":

        if jugador == jugadores[0]:
            botones[fila][columna]['text'] = jugador

            if checarGanador() is False:
                jugador = jugadores[1]
                etiqueta.config(text=("Turno de " + jugadores[1]))

            elif checarGanador() is True:
                etiqueta.config(text=(jugadores[0] + " gana"))

            elif checarGanador() == "Empate":
                etiqueta.config(text=("Empate!"))

        else:

            botones[fila][columna]['text'] = jugador

            if checarGanador() is False:
                jugador = jugadores[0]
                etiqueta.config(text=("Turno de " + jugadores[0]))

            elif checarGanador() is True:
                etiqueta.config(text=(jugadores[1] + " gana"))

            elif checarGanador() == "Empate":
                etiqueta.config(text=("Empate!"))

def checarGanador():
    gato1()
    return False

def gato1():
    g1 = 0
    while g1 == 0:
        for fila in range(3):
            if botones[fila][0]['text'] == botones[fila][1]['text'] == botones[fila][2]['text'] !=  "":
                botones[fila][0].config(bg="green")
                botones[fila][1].config(bg="green")
                botones[fila][2].config(bg="green")
                botones1[0][0] = jugador
                print(botones1)
                print(g1)
                g1=1
            
        for columna in range(3):
            if botones[0][columna]['text'] == botones[1][columna]['text'] == botones[2][columna]['text'] !=  "":
                botones[0][columna].config(bg="green")
                botones[1][columna].config(bg="green")
                botones[2][columna].config(bg="green")
                botones1[0][0] = jugador
                print(botones1)
                print(g1)
                g1=1
            
        if botones[0][0]['text'] == botones[1][1]['text'] == botones[2][2]['text'] != "":
            botones[0][0].config(bg="green")
            botones[1][1].config(bg="green")
            botones[2][2].config(bg="green")
            botones1[0][0] = jugador
            print(botones1)
            print(g1)
            g1=1
        
        elif botones[0][2]['text'] == botones[1][1]['text'] == botones[2][0]['text'] != "":
            botones[0][2].config(bg="green")
            botones[1][1].config(bg="green")
            botones[2][0].config(bg="green")
            botones1[0][0] = jugador
            print(botones1)
            g1=1
    


def gato2():
    pass

def gato3():
    pass

def gato4():
    pass

def gato5():
    pass

def gato6():
    pass

def gato7():
    pass

def gato8():
    pass

def gato9():
    pass

def espaciosVacios():
    espacios = 81

    for fila in range(3):
        for columna in range(3):
            if botones[fila][columna]['text'] != "":
                espacios -= 1

    if espacios == 0:
        return False
    else:
        return True

def nuevoJuego():
    global jugador

    jugador = random.choice(jugadores)

    etiqueta.config(text="Turno de " + jugador)

    for fila in range(9):
        for columna in range(9):
            botones[fila][columna].config(text="", bg="#F0F0F0")

ventana = Tk()
ventana.title("Tic-Tac-Toe")
jugadores = ["x", "o"]
jugador = random.choice(jugadores)
botones1 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

botones = [[0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0,0] ]

etiqueta = Label(text="Turno de " + jugador, font=('consolas', 40))
etiqueta.pack(side="top")

botonReinicio = Button(text="Reinicio", font=('consolas', 20), command=nuevoJuego)
botonReinicio.pack(side="top")

frame = Frame(ventana)
frame.pack()

for fila in range(9):
    for columna in range(9):
        botones[fila][columna] = Button(frame, text="", font=('consolas', 10), width=4, height=2,
                                        command= lambda fila=fila, columna = columna: siguienteTurno(fila, columna))
        botones[fila][columna].grid(row=fila, column=columna, padx=2, pady=2)


ventana.mainloop()