print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Bem-vindo à Ilha do Tesouro.\nSua missão é encontrar o tesouro") 

escolha1 = input('''
Você está em uma encruzilhada. Onde você quer ir? 
Digite "esquerda" ou "direita"\n''').lower() 

if escolha1 == "esquerda":
  escolha2 = input('''
  Você está em um lago. Existe uma ilha no meio do lago. Você quer "nadar" ou "esperar"?
  \n''').lower()
  if escolha2 == "esperar":
    escolha3 = input('''
    Você chega à ilha ileso. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. 
    Qual cor você escolhe?
    ''').lower()
    if escolha3 == "vermelha":
      print("Você entrou na sala e pegou fogo! Game Over.")
    elif escolha3 == "amarela":
      print("Você entrou na sala e encontrou o tesouro! Parabéns! Você venceu!!!")
    elif escolha3 == "azul":
      print("Você entrou na sala e foi comido por bestas! Game over.")
    else:
      print("Não existe porta para essa cor. Game Over.")
  else:
    print("Você foi atacado por um tubarão. Game Over.")
else:
  print("Você caiu em um buraco. Game Over.")
