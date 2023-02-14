import imprimir_tablero as it
import jugada as j
import ia
import detectar_victoria as dv

def iniciar_juego(tablero,turno, puntosx, puntoso, estado_partida, modo_juego):
  jugadas = 0
  while estado_partida:
    
    it.imprimir_tablero(tablero, turno, puntosx, puntoso, estado_partida, jugadas, modo_juego)
    print()
    if jugadas <= 8:
      if modo_juego == "M" or (modo_juego == "S" and turno == "X"):
        seleccion = input("Seleccione un valor de la tabla instrucciones: ")
        j.jugada(tablero,seleccion, turno)
      else:
        ia.ia(tablero)
      
      jugadas +=1

      if dv.detectar_victoria(tablero, turno):
        estado_partida = False
        jugadas = 0
        if turno == "X":
          puntosx += 1
        else: puntoso += 1
      else:
        if turno == "X":
          turno = "O"
        else: turno = "X"
    else: 
      estado_partida = False
    
    it.imprimir_tablero(tablero, turno, puntosx, puntoso, estado_partida, jugadas, modo_juego)

    
  