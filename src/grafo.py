# ---------------------------------------------------
# LEITURA DO GRAFO
# ---------------------------------------------------

def ler_grafo(nome_arquivo):

    with open(nome_arquivo, 'r', encoding='utf-8') as f:

        linhas = [linha.strip()
                  for linha in f
                  if linha.strip()]

    n = int(linhas[0])

    matriz = [[0] * n for _ in range(n)]

    linha_atual = 1

    for i in range(n - 1):

        valores = list(
            map(int, linhas[linha_atual].split())
        )

        linha_atual += 1

        for j, peso in enumerate(valores):

            col = i + j + 1

            matriz[i][col] = peso
            matriz[col][i] = peso

    return matriz