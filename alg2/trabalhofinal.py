import csv
ano_e = []
arrFilmes = []
arrFilmes_a = []
arrFilmes_g = []
arrFilmes_i = []
arrFilmes_e = []

with open("alg2/filmes.csv", "r") as filmes:
    for filme in filmes:
        arrFilmes.append(filme.split(';'))

def contarlinha():
    with open("alg2/filme_ano.csv", 'r') as filme_anos:
        for ano in filme_anos:
            arrFilmes_a.append(ano.split(";"))

    with open("alg2/genero.csv", 'r') as filme_genero:
        for genero in filme_genero:
            arrFilmes_g.append(genero.split(";"))

    with open("alg2/empresa.csv", 'r') as filme_empresa:
        for empresa in filme_empresa:
            arrFilmes_e.append(empresa.split(";"))

    with open("alg2/inf.csv", 'r') as filme_info:
        for info in filme_info:
            arrFilmes_i.append(info.split(";"))

def filme_ano(ano):
    with open("alg2/filmes.csv", "r") as filme, open("alg2/filme_ano.csv", "a") as filme_ano:
        writer = csv.DictWriter(filme_ano, fieldnames=['Ano de exibição', 'Título da Obra'], delimiter = ';')
        if inf.tell() == 0:
            writer.writeheader()
        for linha in filme:
            coluna = linha.split(";")
            if coluna[0] == str(ano):
                filme_ano.write(coluna[0] + ";" + coluna[1] + "\n")

def genero(pesq):
    with open("alg2/filmes.csv", "r") as filmes, open("alg2/genero.csv", "w", encoding='utf-8') as genero:
        writer = csv.DictWriter(genero, fieldnames=['Ano de exibição', 'Título da Obra', 'Gênero'], delimiter = ';')
        if inf.tell() == 0:
            writer.writeheader()
        for linha in filmes:
            coluna = linha.split(";")
            if coluna[3].lower() == pesq.lower():
                genero.write(coluna[0]+";"+coluna[1]+";"+coluna[3]+"\n")

def empresa(pesq):
    with open("alg2/filmes.csv", "r") as filmes, open("alg2/empresa.csv", "w", encoding='utf-8') as empresa:
        writer = csv.DictWriter(empresa, fieldnames=['Ano de exibição', 'Título da Obra', 'Gênero', 'Empresa Distribuidora'], delimiter = ';')
        if inf.tell() == 0:
            writer.writeheader()
        for linha in filmes:
            coluna = linha.split(";")
            if coluna[7].lower() == pesq.lower():
                empresa.write(coluna[0]+";"+coluna[1]+";"+coluna[3]+ ";" + coluna[7] +"\n")

def inf(nome_filme):
    info = []
    with open("alg2/filmes.csv", "r") as filmes, open("alg2/inf.csv", "a") as inf:
        writer = csv.DictWriter(inf, fieldnames=['Ano de exibição', 'Título da Obra', 'CPB/ROE', 'Gênero', 'Nacionalidade', 'Data de Lançamento', 'Empresa Distribuidora', 'Renda acumulada'], delimiter = ';')
        if inf.tell() == 0:
            writer.writeheader()
        for linha in csv.reader(filmes, delimiter = ';'):
            coluna = linha
            if coluna[2] == nome_filme:
                inf.write(f"{coluna[0]}; {coluna[1]}; {coluna[2]}; {coluna[3]}; {coluna[5]}; {coluna[6]}; {coluna[7]}; {coluna[12]} \n")
                cont_inf += 1
            if coluna[1].lower() == nome_filme.lower():
                inf.write(f"{coluna[0]}; {coluna[1]}; {coluna[2]}; {coluna[3]}; {coluna[5]}; {coluna[6]}; {coluna[7]}; {coluna[12]} \n")

def relatorio():
    contarlinha()
    count_filmes = len(arrFilmes)
    cabecalho = arrFilmes[0]
    print (f"\nNo arquivo principal filmes.csv há um total de {count_filmes} linhas")
    print(f'\nNo arquivo filme_ano.csv há um total de {len(arrFilmes_a)} linhas')
    print(f"\nNo arquivo genero.csv há um total de {len(arrFilmes_g)} linhas")
    print(f"\nNo arquivo empresa.csv há um total de {len(arrFilmes_e)} linhas")
    print(f"\nNo arquivo inf.csv há um total de {len(arrFilmes_i)} linhas")
 
    print(f"\nOs nomes das colunas no arquivo principal são: ")
    for i in range(len(cabecalho)):
        if(cabecalho[i].strip() != ''):
            print(cabecalho[i])

def main():
    print("Seja bem-vindo!")
    print("Insira o número desejado para: ")
    print("0. para sair")
    print("1. Pesquisar os filmes lançados em um ano específico.")
    print("2. Quais as obras de um gênero específico.")
    print("3. Pesquisar as informações sobre um filme.")
    print("4. Pesquisar um filme através de seu CBP / ROE.")
    print("5. Pesquisar os filmes exibidos por uma empresa distribuidora específica.")
    print("6. Exibir relatório.")

    num = int(input("Insira o número: "))

    if num == 0:
        exit()
    elif num == 1:
        print("Se deseja voltar ao menu digite 0.")
        while True:
            ano = int(input("Insira qual ano deseja pesquisar os filmes exibidos: "))
            if ano == 0:
                main()
            else:
                filme_ano(ano)
            continuar = input("Você deseja obter informação de mais algum filme? (S/N) ").lower() == "n"
            while continuar:
                main()

    elif num == 2:
        print("Se deseja voltar ao menu digite 0.")
        while True:
            pesq = input("Insira o gênero ao qual deseja ver os filmes exibidos: ")
            if pesq == "0":
                main()
            else:
                genero(pesq)
            continuar = input("Você deseja obter informação de mais algum filme? (S/N) ").lower() == "n"
            while continuar:
                main()
    elif num == 3:
        print("Se deseja voltar ao menu digite 0.")
        while True:
            nome_filme = input("Insira o nome do filme: ")
            if nome_filme == 0:
                main()
            else:
                inf(nome_filme)
            continuar = input("Você deseja obter informação de mais algum filme? (S/N) ").lower() == "n"
            while continuar:
                main()
    elif num == 4:
        print("Se deseja voltar ao menu digite 0.")
        while True:
            nome_cpb = input("Insira o CPB/ROE do filme: ")
            if nome_cpb == 0:
                main()
            else:
                inf(nome_cpb)
            continuar = input("Você deseja obter informação de mais algum filme? (S/N) ").lower() == "n"
            while continuar:
                main()
    elif num == 5:
        print("Se deseja voltar ao menu digite 0.")
        while True:
            nome_emp = input("Insira a empresa distrubuidora do filme: ")
            if nome_emp == 0:
                main()
            else:
                empresa(nome_emp)
            continuar = input("Você deseja obter informação de mais algum filme? (S/N) ").lower() == "n"
            while continuar:
                main()
    elif num == 6:
        relatorio()
        
if __name__ == "__main__":
    main()

#Funções que quero realizar:

# Função 1:  Quais os filmes lançados em (20XX) anos OK
    # Nome função: filme_ano()
# Função 2:  Quais as obras lançadas de X gênero e seu ano de exibição OK
# Função 3:  Pesquisar informações sobre um filme específico.  OK
    # Deverá conter:
        # Seu ano de exibição
        # CPB / ROE
        # Nacionalidade
        # Empresa distribuidora
        # Renda acumulada
        # Data de lançamento
# Função 4:  Pesquisar o filme através de seu CBP/ROE e exibir suas informações
# Função 5:  Pesquisar quais filmes possuem X país(es) produtor(es). 
# Função 6:  Quais os filmes exibidos por X distribuidora