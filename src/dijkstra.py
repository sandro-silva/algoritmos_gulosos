import heapq

# ---------------------------------------------------
# DIJKSTRA
# ---------------------------------------------------

def dijkstra(matriz, origem):

    n = len(matriz)

    distancias = [float('inf')] * n

    anterior = [-1] * n

    distancias[origem] = 0

    heap = [(0, origem)]

    while heap:

        dist_atual, u = heapq.heappop(heap)

        if dist_atual > distancias[u]:
            continue

        for v in range(n):

            peso = matriz[u][v]

            if peso != 0:

                nova_distancia = (
                    distancias[u] + peso
                )

                if nova_distancia < distancias[v]:

                    distancias[v] = nova_distancia

                    anterior[v] = u

                    heapq.heappush(
                        heap,
                        (nova_distancia, v)
                    )

    return distancias, anterior


# ---------------------------------------------------
# RECONSTRUIR CAMINHO
# ---------------------------------------------------

def reconstruir_caminho(anterior, destino):

    caminho = []

    atual = destino

    while atual != -1:

        caminho.append(atual)

        atual = anterior[atual]

    caminho.reverse()

    return caminho