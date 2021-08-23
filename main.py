import os
import random
from typing import Counter
palavras = ["Carro", "Moto", "Jogo", "Motor", "Subterraneo", "Araucarias", "Trator", "Otorrino", "Laringologista"]
resposta = []


while True:
  print("*****BEM VINDO*****")
  print("O que vai ser?""\n""1 - Nova Partida""\n""2 - Ver Pontuação""\n""3 - Sair")
  choose = int(input())
  if choose == 1:
    print("Vamos começar!")
    os.system('cls')
    pergunta = random.choice(palavras)
    resposta = list (pergunta)
    cod = "_" * len(resposta)
    print(str(cod))
    
    
    
    
    
  elif choose == 2:
    print("*****PONTUAÇÃO*****")
  elif choose == 3:
    print("Tem certeza que quer sair?" "\n" "1 - sim 2 - Não")
    sair = int(input())
    if sair == 1:
      break 
  
    
