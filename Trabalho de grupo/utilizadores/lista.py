encoding: "utf-8"
#1
import os
def lista_utilizadores(nome_ficheiro):
    f = open("utilizadores.txt", "rt")
    cab = f.readline()
    listaN = f.readlines()
    f.close()
    f = open(nome_ficheiro, 'wt')
    print('<style>table,th,td{border:1px solid blue; border-collapse:collapse;}</style>', file=f)
    print('<script>alert(124);</script>', file=f)
    print('<body>', file=f)
    print('<table>', file=f)
    print("<img hrf=logotipo.jpg with=100px ", file=f)
    print("<tr><th>%s</th><th>%s</th><th>%s</th></tr>" % ('Nome', 'Telefone', 'Email'), file=f)
    for linha in listaN:
        linha = linha.rstrip('\n')
        v = linha.split(';')
        Nome, Email, Telefone = linha.split(';')
        print(Nome, Telefone, Email)
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Nome, Telefone, Email), file=f)
    print('</table>', file=f)
    print('</body>', file=f)
    f.close()
nome = 'lista1.html'
lista_utilizadores(nome)
os.system(nome)
