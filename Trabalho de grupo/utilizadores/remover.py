encoding: "utf-8"
# 5
from configuracao import*
def remover_utilizador():
    print("\n")
    fich = open(nome_ficheiro_utilizadores, 'r')
    plinha = fich.readline()
    lista = fich.readlines()
    fich.close()
    print("%-20s %6s %2s %s" % ("Nome", "Idade", "", "Cidade"))
    for u in lista:
          u = u.rstrip("\n")
          nome, idade, cidade = u.split(";")
          print("%-20s %1s %-5s %1s %s" %(nome, "", idade, "", cidade))

    pos = int(input('Qual a posição do utilizador que quer remover? '))
    if pos > len(lista):
        print('Não existe esse utilizador, só pode ser entre 1 a {}'.format(len(lista)))
    else:
        lista.pop(pos-1)
        fich1 = open(nome_ficheiro_utilizadores, 'w')
        print(plinha, file=fich1)
        for i in range(len(lista)):
            fich1.write(lista[i])
        fich1.close()
    fich.close()
