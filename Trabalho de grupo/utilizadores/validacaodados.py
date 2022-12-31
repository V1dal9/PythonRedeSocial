
def NumeroTelemóvel():
    # tipo in ["inteiro", "real"]
    while True:
        try:
            numero = int(input("Insira o número de telemóvel:\n"))
            if numero<900000000 and numero>999999999:
                print("Insira um número válido.")
            else:
                fich = open('Telemóvel.txt', 'a')
                fich.write(numero + ' ')
                print("Número adicionado á lista")
        except ValueError:
            print("Não digitou um número inteiro!")
            continue


