import os
import logica as l

def imprimir_tablero(tablero, turno, puntosx, puntoso, estado_partida, jugadas, modo_juego):
  os.system('clear')
  print("------------------- TRES EN RAYA -------------------")
  print()
  print("Tablero         Instrucciones        Puntaje")
  print()
  print("                |¯¯¯|¯¯¯|¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
  print(f' {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}      | Q | W | E | Jugador X | Jugador O |')
  print('-----------     |-----------|-----------------------|')
  print(f' {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}      | A | S | D |     {puntosx}     |     {puntoso}     |')
  print('-----------     |-----------|_______________________|')
  print(f' {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}      | Z | X | C |')
  print("                |___|___|___|")
  print()
  
  l.logica(puntosx, puntoso, turno, estado_partida, jugadas, modo_juego)
  
