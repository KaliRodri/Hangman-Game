import random
import os
def geraLista(palavra):
 lista = []
 for i in range(0,len(pergunta)):
  lista.append(" * ")
 return lista
 
def insereLetra(letra, palavra, secreta):
 for i in range(0,len(palavra)):
  if palavra[i] == letra:
   secreta[i] = letra
 return secreta
 
palavra = ["arara"]
pergunta = random.choice(palavra)





while True:
 print("*****BEM VINDO*****""\n")
 print("O que vai ser?""\n""1 - Nova Partida""\n""2 - Ver Pontuação""\n""3 - Sair")   
 choose = int(input())
 if choose == 1:
    print("Vamos começar!")
    os.system('cls')
    secreta = geraLista(palavra)
    print("\nPalavra secreta: ")
    print(secreta) 
    letra = input("Letra: ")
    if letra <= "a" and letra >= "Z":
     secreta = insereLetra(letra, palavra, secreta)
     print("\nPalavra secreta: ")
     print(secreta)
 
  
    
