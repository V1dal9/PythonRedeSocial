encoding:"utf-8"
from tweets.inserir import*

def Inserir_tweets():
    print("\n")
    fich = open('tweets.txt', 'a')   # fich para abrir ficheiro e carregar lista
    nome=input('Insira o tweet?\n')
    fich = open('tweets.txt', 'w')
    fich.write(nome + ' ')
    print("Adicionado á lista.")
    fich.close()