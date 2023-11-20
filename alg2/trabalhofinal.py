import os
ano_e = []

def filme_ano(ano):
    with open("alg2/filmes.csv", "r") as filme, open("alg2/filme_ano.csv", "w") as filme_ano:
        filme_ano.write("Ano;Título da Obra \n")
        for linha in filme:
            coluna = linha.split(";")
            #print(coluna)
            if coluna[0] == str(ano):
                filme_ano.write(coluna[0]+";"+coluna[1]+"\n")
                #ano_e.append(coluna[0]+";"+coluna[1])

        # for i in ano_e:
        #     filme_ano.write(i + "\n")


def genero(pesq):
    with open("alg2/filmes.csv", "r") as filmes, open("alg2/genero.csv", "w", encoding='utf-8') as genero:
        genero.write("Ano de lançamento; Nome da obra; Gênero \n")
        for linha in filmes:
            coluna = linha.split(";")
            if coluna[3].lower() == pesq.lower():
                genero.write(coluna[0]+";"+coluna[1]+";"+coluna[3]+"\n")
                # print (coluna[3])

def inf(nome_filme):
    with open("alg2/filmes.csv", "r") as filmes:
        teste = (f'{(os.path.abspath(os.curdir))}/alg2/inf.csv')
        existeArq = (os.path.isfile(teste))

        with open("alg2/inf.csv", "a") as inf:
            print(not )
            if (not existeArq):
                inf.write("Ano de exibição; Título da Obra; CPB/ROE; Gênero; Nacionalidade; Data de Lançamento; Empresa Distribuidora; Renda acumulada \n ")
            for linha in filmes:
                coluna = linha.split(";")
                if coluna[1].lower() == nome_filme.lower():
                    inf.write(f"{coluna[0]}; {coluna[1]}; {coluna[2]}; {coluna[3]}; {coluna[5]}; {coluna[6]}; {coluna[7]}; {coluna[12]} \n")

def main():
    print("Seja bem-vindo!")
    print("Insira o número desejado para: ")
    print("0. para sair")
    print("1. Pesquisar os filmes lançados em um ano específico.")
    print("2. Quais as obras de um gênero específico.")
    print("3. Pesquisar as informações sobre um filme.")
    print("4. Pesquisar um filme através de seu CBP / ROE.")
    print("5. Pesquisar um filme através de seu(s) país(es) produtor(es).")
    print("6. Pesquisar os filmes exibidos por uma empresa distribuidora específica.")

    num = int(input("Insira o número: "))

    if num == 0:
        exit()
    elif num == 1:
        print("Se deseja voltar ao menu digite 0.")
        ano = int(input("Insira qual ano deseja pesquisar os filmes exibidos: "))
        if ano == 0:
            main()
        else:
            filme_ano(ano)
    elif num == 2:
        print("Se deseja voltar ao menu digite 0.")
        pesq = input("Insira o gênero ao qual deseja ver os filmes exibidos: ")
        if pesq == "0":
            main()
        else:
            genero(pesq)
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
    # elif num == 4:
        


        
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