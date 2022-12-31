encoding:"utf-8"

#2
def lista_tweets():
    print('\n')
    i = 1
    print("Lista de Utilizadores:\n".center(50, '-'))
    fich = open('utilizadores.txt', 'r')
    listaN = fich.readlines()
    for linha in listaN:
        linha = linha.split()
        print("{}-{}".format(i, linha))
        i += 1