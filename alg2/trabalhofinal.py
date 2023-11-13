A_lancamento = []
linha_lancamento = []
obra = []


with open("alg2/filmes.csv", "r") as filmes, open("alg2/ano.csv", mode='w', encoding='utf-8') as linhas:
    for linha in filmes:
        coluna = linha.split(";")
        if (coluna[0] != "Ano de Lançamento"):
            A_lancamento.append(coluna[0])
        
with open("alg2/filmes.csv", 'r') as filmes, open('alg2/titulo.csv', 'w') as titulo:
    for linha in filmes:
        coluna = linha.split(";")
        if coluna[1] != "Título da obra":
            obra.append(coluna[1])

with open('alg2/ano.csv', 'r') as ano, open('alg2/titulo.csv', 'r') as titulo, open("alg2/TandO.csv", 'w') as TandO:
    for i in range(len(A_lancamento)):
        TandO.write(f"{A_lancamento[i]}, {obra[i]} \n")

#Funções que quero realizar:
#Conferir quais filmes foram lançados em x anos (Ok)
#Conferir quais as obras de x genero e seu ano de lançamento
#Conferir quais filmes foram lançados por x distribuidora
#Pesquisar por x filmes onde aparecerá:
    # Ano de lançamento
    # Distribuidora
    # Nacionalidade
    # Salas de lançamento
    # Máximo de salas ocupadas
    # Renda acumulada
    # Genero
# Quantia de obras no arquivo
