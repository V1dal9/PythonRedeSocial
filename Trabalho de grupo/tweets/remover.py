encoding:"utf-8"
#8
def remover_tweet():
    print("\n")
    fich = open('tweets_remover.txt', 'r')
    lista = fich.readlines()
    pos = int(input('Qual a posição do tweet que quer remover? '))
    if pos > len(lista):
        print('Não existe esse tweet, só pode ser entre 1 a {}'.format(len(lista)))
    else:
        lista.pop(pos-1)
        fich1= open('tweets.txt', 'w')
        fich1.write("")
        fich1.close()
        fich2= open('tweets.txt', 'a')
        for i in range(len(lista)):
            fich2.write(lista[i])
        fich2.close()
