import heapq

# ---------------------------------------------------
# PRIM
# ---------------------------------------------------

def prim(matriz):

    n = len(matriz)

    visitado = [False] * n

    heap = [(0, 0, -1)]

    custo_total = 0

    agm = []

    while heap:

        peso, u, pai = heapq.heappop(heap)

        if visitado[u]:
            continue

        visitado[u] = True

        custo_total += peso

        if pai != -1:

            agm.append((pai, u, peso))

        for v in range(n):

            if not visitado[v] and matriz[u][v] != 0:

                heapq.heappush(
                    heap,
                    (matriz[u][v], v, u)
                )

    return agm, custo_total