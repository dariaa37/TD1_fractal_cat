from tkinter import *

# Ventana principal
# window = Tk()
# window.title("Gato Fractal")
# window.geometry("300x300")

# gatoFractal = {
#     "g1" : 0,    "g2" : 0,    "g3" : 0,
#     "g4" : 0,    "g5" : 0,    "g6" : 0,
#     "g7" : 0,    "g8" : 0,    "g9" : 0,
# }

# # # Tablero
# def jugada(boton):
#     pass

# # Crear botones usando un bucle for
# def generarMiniTableros():
#     tablero = []
#     for i in range(3):  
#         filas = []
#         for j in range(3):
#             filas.append(f"{i}. {j}")
#             boton = Button(window, text=" ", font=('Helvetica', '20'), width=5, height=2, command=lambda x=i, y=j: jugada(tablero[x][y]))
#         boton.grid(row=i, column=j, padx=2, pady=2)
#         # Cuando la fila se llena, se agrega a el gato
#         tablero.append(filas)
#     return tablero

# for key in gatoFractal:
#     gatoFractal[key] = generarMiniTableros()

# window.mainloop()


# Ventana principal
window = Tk()
window.title("Gato Fractal")
window.geometry("300x300")

gatoFractal = {
    "g1": 0, "g2": 0, "g3": 0,
    "g4": 0, "g5": 0, "g6": 0,
    "g7": 0, "g8": 0, "g9": 0,
}

# Tablero
def jugada(boton):
    pass

# Crear botones usando un bucle for
def generarMinitablero(fila, columna):
    tablero = []
    for i in range(3):
        filas = []
        for j in range(3):
            filas.append(f"{i}.{j}")
            boton = Button(window, text=" ", font=('Helvetica', '20'), width=5, height=2,
                           command=lambda x=i, y=j: jugada(tablero[x][y]))
            boton.grid(row=i+fila*3, column=j+columna*3, padx=2, pady=2)
            # Cuando la fila se llena, se agrega a el gato
            filas.append(boton)
        tablero.append(filas)
    return tablero

# Ventana principal
window = Tk()
window.title("Gato Fractal")
window.geometry("300x300")

gatoFractal = {
    "g1": 0, "g2": 0, "g3": 0,
    "g4": 0, "g5": 0, "g6": 0,
    "g7": 0, "g8": 0, "g9": 0,
}

# Tablero
def jugada(boton):
    pass

# Crear botones usando un bucle for
def generarMinitablero(fila, columna):
    tablero = []
    for i in range(3):
        filas = []
        for j in range(3):
            filas.append(f"{i}.{j}")
            boton = Button(window, text=" ", font=('Helvetica', '20'), width=5, height=2,
                           command=lambda x=i, y=j: jugada(tablero[x][y]))
            boton.grid(row=i+fila*3, column=j+columna*3, padx=2, pady=2)
            # Cuando la fila se llena, se agrega a el gato
            filas.append(boton)
        tablero.append(filas)
    return tablero

for key in gatoFractal:
    gatoFractal[key] = generarMinitablero(int(key[1])-1, int(key[2])-1)

window.mainloop()
window.mainloop()
