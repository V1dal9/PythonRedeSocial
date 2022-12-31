encoding: "utf-8"
from menuprincipal import*
from utilizadores.remover import*
from utilizadores.alterar import*
from utilizadores.inserir import*
from utilizadores.lista import*

from utilizadores.validacaodados import*

from tweets.inserir import*
from tweets.like import*
from tweets.lista import*
from tweets.remover import*
opcao = ""
def Menu():
    print("Opcoes".center(50, '-'))
    print('1 -> Lista de Utilizadores')
    print('2 -> Lista de tweets')
    print('3 -> Numero de likes dos tweets')
    print('4 -> Alterar lista de utilizadores')
    print('5 -> Remover utilizador')
    print('6 -> Inserir utilizador')
    print('7 -> Inserir Tweets')
    print('8 -> Remover tweet')
    print('0 -> Sair')

while opcao != '0':
    Menu()# apresenta o menu
    opcao =input('\nInsira a sua opcao: ')
    if opcao == '0':
        print("\nA rede social vai terminar...")
        ENTER = input('\nPrima <ENTER> para continuar.\n')
        break
    if opcao == '1':
        lista_utilizadores(nome)
        ENTER = input('\nPrima <ENTER> para continuar.\n')
    if opcao == '2':
        lista_tweets()
        ENTER = input('\nPrima <ENTER> para continuar.\n')
    if opcao == '3':
        like_tweets()
        ENTER = input('\nPrima <ENTER> para continuar.\n')
    if opcao == '4':
        alterar_utilizador()
        enter = input('\nPrima <ENTER> para continuar.\n')
    if opcao == '5':
        remover_utilizador()
        ENTER = input('\nPrima <ENTER> para continuar.\n')
    if opcao == '6':
        Inserir_utilizador()
        ENTER = input('\nPrima <ENTER> para continuar.\n')
    if opcao == '7':
        Inserir_tweets()
        ENTER = input('\nPrima <ENTER> para continuar.\n')
if opcao == '8':
        remover_tweet()
        ENTER = input('\nPrima <ENTER> para continuar.\n')
