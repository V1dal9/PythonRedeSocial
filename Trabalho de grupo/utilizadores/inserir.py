encoding:"utf-8"
#import datetime
#data de inserao=datetime.datetime.now().strftime('%y-%m-%d  %H:%M:%S')
#6
def Inserir_utilizador():
    print("\n")
    fich = open('utilizadores.txt', 'a')   # fich para abrir ficheiro e carregar lista
    nome = input('Insira o nome?\n')
    while True:
        numero = input('Insira o numero?\n')


    Idade = str(input('Idade?\n'))
    sexo = input('sexo (Masculino/Feminino) ?\n ')
    while True:
        email = str(input('emai?\n '))
        pp = ['a-z', '.', '1-9']

        #for i in range()

    numero = int(input('Telemóvel?\n'))
    fich = open('utilizdor_inserir.txt', 'w')
    fich.write(nome + ' ')
    fich.write(Idade + " ")
    fich.write(sexo + " ")
    fich.write(email + " " + '\n')
    fich.write(numero + " " + '\n')
    print("Adicionado á lista.")
    fich.close()