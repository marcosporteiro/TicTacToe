import random
import os
from iniciar_juego import *


def menu():

  modo_juego = "M"
  tablero = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
  
  if random.randint(0, 1) == 0: 
    turno= "X"
  else:
    turno = "O"
  
  puntosx = 0
  puntoso = 0
  
  os.system('clear')
  print("------------------- TRES EN RAYA -------------------")
  print()
  print("1) Jugador contra IA.")
  print("2) Multijugador.")
  print("3) Salir.")
  print()
  entrada = input("Seleccione una opcion: ")
  if entrada == "1" and entrada:
    modo_juego = "S"
    iniciar_juego(tablero, turno, puntosx, puntoso, True, modo_juego)
  elif entrada == "2":
    modo_juego = "M"
    iniciar_juego(tablero, turno, puntosx, puntoso, True, modo_juego)
    
  