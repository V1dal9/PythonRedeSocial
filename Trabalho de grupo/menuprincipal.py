encoding: "utf-8"

from utilizadores import*
opcao = ""
def Menu():
    print("Opcoes".center(50, '-'))
    print('1 -> Utilizadores')
    print('2 -> Tweets')

while opcao != '0':
    Menu()# apresenta o menu
    opcao =input('\nInsira a sua opcao: ')
    if opcao == '0':
        print("\nA rede social vai terminar...")
        ENTER = input('\nPrima <ENTER> para continuar.\n')
        break
    if opcao == '1':
        Utilizadores
        ENTER = input('\nPrima <ENTER> para continuar.\n')
    if opcao == '2':
        Tweets()
        ENTER = input('\nPrima <ENTER> para continuar.\n')