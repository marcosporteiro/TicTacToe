def jugada(tablero, seleccion, turno):
  if seleccion == "Q" or seleccion == "q":
    
    if tablero[0][0] == " ":
      tablero[0][0] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
      
  elif seleccion == "W" or seleccion == "w":
    
    if tablero[0][1] == " ":
      tablero[0][1] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
      
  elif seleccion == "E" or seleccion == "e":
        
    if tablero[0][2] == " ":
      tablero[0][2] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
      
  elif seleccion == "A" or seleccion == "a":

    if tablero[1][0] == " ":
      tablero[1][0] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
    
  elif seleccion == "S" or seleccion == "s":
    
    if tablero[1][1] == " ":
      tablero[1][1] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
    
  elif seleccion == "D" or seleccion == "d":
    
    if tablero[1][2] == " ":
      tablero[1][2] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
      
  elif seleccion == "Z" or seleccion == "z":

    if tablero[2][0] == " ":
      tablero[2][0] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
    
  elif seleccion == "X" or seleccion == "x":

    if tablero[2][1] == " ":
      tablero[2][1] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
    
  elif seleccion == "C" or seleccion == "c":
    
    if tablero[2][2] == " ":
      tablero[2][2] = turno
    else:
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
      
  else :
      seleccion = input("Jugada invalida, seleccione denuevo: ")
      jugada(tablero, seleccion, turno)
