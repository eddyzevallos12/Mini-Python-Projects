import random

options = ("piedra", "papel", "tijera")
computer_wins = 0
user_wins = 0

rounds=1

while True:
    
  print("*"*10)
  print("ROUND: ", rounds)
  print("*"*10)
  
  usuario= input("Elije: piedra, papel o tijera?: ")
  usuario = usuario.lower()
  
  if not usuario in options:
    print("Esa opcion no es valida")
    continue
  
  computer= random.choice(options)
  
  print("User option: ", usuario)
  print("Computer option: ", computer)
  
  if usuario == computer:
    print("Empate!")
  elif usuario == "piedra":
    if computer == "tijera":
      print("Piedra gana tijera")
      print("User win!!")
      user_wins += 1
    else:
      print("Papel gana a piedra")
      print("Computer win!!!")
      computer_wins += 1
  elif usuario == "papel":
    if computer == "piedra":
      print("Papel gana a piedra")
      print("User win!")
      user_wins += 1
    else:
      print("Tijera gana a papel")
      print("Computer win!")
      computer_wins += 1
  elif (usuario == "tijera"):
    if computer == "papel":
      print("Tijera gana a papel")
      print("user win!")
      user_wins += 1
    else:
      print("Piedra gana a tijera")
      print("Computer win!")
      computer_wins += 1

  print("User wins: ", user_wins)
  print("Computer wins: ", computer_wins)
  
  if computer_wins == 2:
    print("Computer es el GANADOR")
    break
  if user_wins == 2:
    print("User es el GANADOR")
    break


  rounds += 1