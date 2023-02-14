def detectar_victoria(tablero, turno):
  estado_tablero = []
  victoria = False
  i=0
  j=0

  for i in range(3):
    for j in range(3):
      if tablero[i][j] == turno:
        estado_tablero.append("V")
      else:
        estado_tablero.append(" ")

  if estado_tablero[0] == "V":
    if estado_tablero[1] == "V":
      if estado_tablero[2] == "V":
        victoria = True
    elif estado_tablero[3] == "V":
      if estado_tablero[6]== "V":
        victoria = True
    elif estado_tablero[4]== "V":
      if  estado_tablero[8]=="V":
        victoria = True
  
  if estado_tablero[1] == "V":
    if estado_tablero[4]== "V":
      if estado_tablero[7]== "V":
        victoria = True

  if estado_tablero[2] == "V":
    if estado_tablero[5] == "V":
      if estado_tablero[8] == "V":
        victoria = True
    elif estado_tablero[4] == "V":
      if estado_tablero[6] == "V":
        victoria = True

  if estado_tablero[3] == "V":
    if estado_tablero[4] == "V":
      if estado_tablero[5] == "V":
        victoria = True

  if estado_tablero[6]== "V":
    if estado_tablero[7] == "V":
      if estado_tablero[8] == "V":
        victoria = True

  return victoria
