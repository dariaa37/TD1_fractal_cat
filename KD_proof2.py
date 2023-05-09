# Solo pruebas del Gato

gatoFractal = {
    "g1" : 0,
    "g2" : 0,
    "g3" : 0,
    "g4" : 0,
    "g5" : 0,
    "g6" : 0,
    "g7" : 0,
    "g8" : 0,
    "g9" : 0,
}

def generarMiniTableros():
    tablero = []
    for i in range(3):  
        filas = []
        for j in range(3):
            filas.append(f"{i}. {j}")
        # Cuando la fila se llena, se agrega a el gato
        tablero.append(filas)
    return tablero


for key in gatoFractal:
    gatoFractal[key] = generarMiniTableros()

for i in gatoFractal:
    print(gatoFractal[i])


