import iniciar_juego as ij

def logica(puntosx, puntoso, turno, estado_partida, jugadas, modo_juego):
  if estado_partida:
    print("Turno: "+turno)
  else:
    if jugadas == 9:
      print("Hubo un empate")
    else: 
      print(f"¡¡¡ Ganó el jugador {turno} !!!")
      
    entrada = input("Presione cualquier tecla para continuar o F para terminar: ")
    if entrada == "F" or entrada == "f":
      print()
      if puntoso < puntosx:
        print(f"Ganó el jugador X con {puntosx} puntos")
      elif puntoso > puntosx:
        print(f"Ganó el jugador O con {puntoso} puntos")
      else: print("Hubo un empate ")
    else:
      if turno == "X":
        turno = "O"
      else: turno = "X"
      tablero = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]
      ij.iniciar_juego(tablero,turno, puntosx, puntoso, True, modo_juego)
  