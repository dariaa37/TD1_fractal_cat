# Taller de Desarrollo: Fractal Cat
# Equipo 4
# Date:     08/04/2023

# x = orange
# o = DeepSkyBkue2

from tkinter import *
import random

def gatito1():      # Buscar donde se llamara esta función, se espera que esta función rellene gato[0][0]
    global jugador
    global num

    for i in range(3):
        if gatitos[0][i] == gatitos[0][i+3] == gatitos[0][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[0][i] == gatitos[0][i+1] == gatitos[0][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[0][0] == gatitos[0][4] == gatitos[0][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[0][2] == gatitos[0][4] == gatitos[0][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def gatito2():
    global jugador
    global num

    for i in range(3):
        if gatitos[1][i] == gatitos[1][i+3] == gatitos[1][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[1][i] == gatitos[1][i+1] == gatitos[1][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[1][0] == gatitos[1][4] == gatitos[1][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[1][2] == gatitos[1][4] == gatitos[1][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def gatito3():
    global jugador
    global num

    for i in range(3):
        if gatitos[2][i] == gatitos[2][i+3] == gatitos[2][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[2][i] == gatitos[2][i+1] == gatitos[2][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[2][0] == gatitos[2][4] == gatitos[2][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[2][2] == gatitos[2][4] == gatitos[2][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""
####
def gatito4():
    global jugador
    global num

    for i in range(3):
        if gatitos[3][i] == gatitos[3][i+3] == gatitos[3][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[3][i] == gatitos[3][i+1] == gatitos[3][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[3][0] == gatitos[3][4] == gatitos[3][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[3][2] == gatitos[3][4] == gatitos[3][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def gatito5():
    global jugador
    global num

    for i in range(3):
        if gatitos[4][i] == gatitos[4][i+3] == gatitos[4][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[4][i] == gatitos[4][i+1] == gatitos[4][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[4][0] == gatitos[4][4] == gatitos[4][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[4][2] == gatitos[4][4] == gatitos[4][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def gatito6():
    global jugador
    global num

    for i in range(3):
        if gatitos[5][i] == gatitos[5][i+3] == gatitos[5][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[5][i] == gatitos[5][i+1] == gatitos[5][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[5][0] == gatitos[5][4] == gatitos[5][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[5][2] == gatitos[5][4] == gatitos[5][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def gatito7():
    global jugador
    global num

    for i in range(3):
        if gatitos[6][i] == gatitos[6][i+3] == gatitos[6][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[6][i] == gatitos[6][i+1] == gatitos[6][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[6][0] == gatitos[6][4] == gatitos[6][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[6][2] == gatitos[6][4] == gatitos[6][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def gatito8():
    global jugador
    global num

    for i in range(3):
        if gatitos[7][i] == gatitos[7][i+3] == gatitos[7][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[7][i] == gatitos[7][i+1] == gatitos[7][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[7][0] == gatitos[7][4] == gatitos[7][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[7][2] == gatitos[7][4] == gatitos[7][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def gatito9():
    global jugador
    global num

    for i in range(3):
        if gatitos[8][i] == gatitos[8][i+3] == gatitos[8][i+6] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    for i in num:
        if gatitos[8][i] == gatitos[8][i+1] == gatitos[8][i+2] !=  "":
            if jugador == "x":
                return jugadores[0]
            else:
                return jugadores[1]
        
    if gatitos[8][0] == gatitos[8][4] == gatitos[8][8] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    elif gatitos[8][2] == gatitos[8][4] == gatitos[8][6] != "":
        if jugador == "x":
            return jugadores[0]
        else:
            return jugadores[1]
    
    else:
        return ""

def jugadorGatitos(fila,columna):
    global jugador

    gatitos[fila][columna] = jugador


    # for i in gatitos:
    #     print(i)
    # print()

def tiro(fila, columna, ganador):
    global jugador

    if ganador == False:

        botones[fila][columna]['text'] = jugador 
        botones[fila][columna].config(state="disabled")  # Cambia las propiedades de los botones una vez presionados

        if jugador == jugadores[0]:
            botones[fila][columna].config(relief="raised")

        else:
            botones[fila][columna].config(relief="sunken")

        if jugador == jugadores[0]:     # Cambia al siguiente la variable jugador al siguiente jugador
            jugador = jugadores[1]
            etiqueta.config(text=("Turno de " + jugadores[1]), fg="DeepSkyBlue2")

        else:
            jugador = jugadores[0]
            etiqueta.config(text=("Turno de " + jugadores[0]), fg="orange")

    elif ganador == 'Empate':
        etiqueta.config(text='Empate!')

        for fil in range(9):
            for column in range(9):
                botones[fil][column].config(bg="red")

    else:
        if ganador == jugadores[1]:
            botones[fila][columna]['text'] = jugador 
            botones[fila][columna].config(state="disabled")

            if jugador == jugadores[0]:
                botones[fila][columna].config(relief="raised")
                for i in range(9):
                    for j in range(9):
                        botones[i][j].config(bg="orange")

            else:
                botones[fila][columna].config(relief="sunken")
                for i in range(9):
                    for j in range(9):
                        botones[i][j].config(bg="DeepSkyBlue2")

            etiqueta.config(text=(jugadores[1] + " gana"))
        else:
            botones[fila][columna]['text'] = jugador 
            botones[fila][columna].config(state="disabled")

            if jugador == jugadores[0]:
                botones[fila][columna].config(relief="raised")
                for i in range(9):
                    for j in range(9):
                        botones[i][j].config(bg="orange")

            else:
                botones[fila][columna].config(relief="sunken")
                for i in range(9):
                    for j in range(9):
                        botones[i][j].config(bg="DeepSkyBlue2")
            
            etiqueta.config(text=(jugadores[0] + " gana"))

def espaciosVacios():
    espacios = 81

    for fila in range(9):
        for columna in range(9):
            if gatitos[fila][columna] != "":
                espacios -= 1

    if espacios == 0:
        return False
    else:
        return True
    
def checarGanador():    # Evalua a la lista gato para ver si hay ganador
    global jugador

    for fila in range(3):
        if gato[fila][0] == gato[fila][1]== gato[fila][2] !=  "":
            
            return jugador
        
    for columna in range(3):
        if gato[0][columna] == gato[1][columna] == gato[2][columna] !=  "":
            
            return jugador
        
    if gato[0][0] == gato[1][1] == gato[2][2] != "":
        
        return jugador
    
    elif gato[0][2] == gato[1][1] == gato[2][0] != "":
        
        return jugador
    
    elif espaciosVacios() is False:
        
        return "Empate"
    
    else:
        return False

def nuevoJuego():
    global jugador
    global gatitos
    global gato

    jugador = random.choice(jugadores)

    gatitos = funciongatitos()

    gato = funciongato()

    etiqueta.config(text="Turno de " + jugador)

    for i in range(9):  # Calcular fila y columna del grupo
        row = i // 3
        col = i % 3
    
    # Calcular color del grupo
        if (row + col) % 2 == 0:
            color = color1
        else:
         color = color2
    
    # Crear botones del grupo
        for j in range(9):
        # Calcular fila y columna del boton
            r = j // 3
            c = j % 3
        
        # Calcular posicion en la ventana
            x = col*3 + c
            y = row*3 + r
        
        # Crear boton
            botones[i][j] = Button(frame, text="", font=('consolas', 12),width=4, height=2, bg=color,
                                   command= lambda fila=i, columna=j: funcionesCombinadas(fila, columna))
            botones[i][j].grid(row=y, column=x)

def funcionesCombinadas(fila,columna):
    global jugador

    jugadorGatitos(fila,columna)

    if gato[0][0] == "":
                
        gato[0][0] = gatito1()
        if gato[0][0] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[0][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[0][i].config(bg="DeepSkyBlue2")

    if gato[0][1] == "":
        
        gato[0][1] = gatito2()
        if gato[0][1] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[1][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[1][i].config(bg="DeepSkyBlue2")

    if gato[0][2] == "":
        
        gato[0][2] = gatito3()
        if gato[0][2] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[2][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[2][i].config(bg="DeepSkyBlue2")

    if gato[1][0] == "":
        gato[1][0] = gatito4()
        if gato[1][0] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[3][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[3][i].config(bg="DeepSkyBlue2")

    if gato[1][1] == "":
        gato[1][1] = gatito5()
        if gato[1][1] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[4][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[4][i].config(bg="DeepSkyBlue2")

    if gato[1][2] == "":
        gato[1][2] = gatito6()
        if gato[1][2] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[5][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[5][i].config(bg="DeepSkyBlue2")

    if gato[2][0] == "":
        gato[2][0] = gatito7()
        if gato[2][0] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[6][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[6][i].config(bg="DeepSkyBlue2")

    if gato[2][1] == "":
        gato[2][1] = gatito8()
        if gato[2][1] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[7][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[7][i].config(bg="DeepSkyBlue2")

    if gato[2][2] == "":
        gato[2][2] = gatito9()
        if gato[2][2] != "":
            if jugador == jugadores[0]:
                for i in range(9):
                    botones[8][i].config(bg="orange")
            else:
                for i in range(9):
                    botones[8][i].config(bg="DeepSkyBlue2")
    
    ganador = checarGanador()
    
    tiro(fila,columna, ganador)

def funciongatitos():
    gatitos2 = [["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""] ]
    
    return gatitos2

def funciongato():
    gato2 = [["","",""],     # Las casillas de este gato representa quien gano el gatito de la posicion correspondiente
        ["","",""],
        ["","",""]]
    
    return gato2

# Crear ventana
ventana = Tk()
ventana.title("botones Fractal")

jugadores = ["x", "o"]
jugador = random.choice(jugadores)

num = [0,3,6]

botones = [["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""], 
           ["","","","","","","","",""] ]

gatitos = funciongatitos()

gato = funciongato()

# Definir colores
color1 = "#E6E6E6"  # gris claro
color2 = "#CCCCCC"  # gris medio

#

etiqueta = Label(text="Turno de " + jugador, font=('consolas', 40))
if jugador == jugadores[0]:
    etiqueta.config(fg="orange")
else:
    etiqueta.config(fg="DeepSkyBlue2")

etiqueta.pack(side="top")

botonReinicio = Button(text="Reinicio", font=('consolas', 20), command=nuevoJuego)
botonReinicio.pack(side="top")

frame = Frame(ventana)
frame.pack()

# Crear grupos de botones
for i in range(9):
    # Calcular fila y columna del grupo
    row = i // 3
    col = i % 3
    
    # Calcular color del grupo
    if (row + col) % 2 == 0:
        color = color1
    else:
        color = color2
    
    # Crear botones del grupo
    for j in range(9):
        # Calcular fila y columna del boton
        r = j // 3
        c = j % 3
        
        # Calcular posicion en la ventana
        x = col*3 + c
        y = row*3 + r
        
        # Crear boton
        botones[i][j] = Button(frame, text="", fg="gray3",font=('consolas', 12),width=4, height=2, bg=color,
                               command= lambda fila=i, columna=j: funcionesCombinadas(fila, columna))
        botones[i][j].grid(row=y, column=x)



# Iniciar loop de la ventana
ventana.mainloop()