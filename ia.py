import random

def ia(tablero):
  i=0
  j=0
  estado_tablero = []
  for i in range(3):
    for j in range(3):
      if tablero[i][j] == " ":
        estado_tablero.append([i,j])
  
  seleccion = random.choice(estado_tablero)
  i = seleccion[0]
  j = seleccion[1]
  tablero[i][j] = "O"
  