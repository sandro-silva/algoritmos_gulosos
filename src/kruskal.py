# ---------------------------------------------------
# UNION FIND
# ---------------------------------------------------

class UnionFind:

    def __init__(self, n):

        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):

        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])

        return self.pai[x]

    def union(self, x, y):

        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:

            self.pai[rx] = ry

        elif self.rank[rx] > self.rank[ry]:

            self.pai[ry] = rx

        else:

            self.pai[ry] = rx
            self.rank[rx] += 1

        return True


# ---------------------------------------------------
# KRUSKAL
# ---------------------------------------------------

def kruskal(matriz):

    n = len(matriz)

    arestas = []

    for i in range(n):

        for j in range(i + 1, n):

            arestas.append(
                (matriz[i][j], i, j)
            )

    arestas.sort()

    uf = UnionFind(n)

    custo_total = 0

    agm = []

    for peso, u, v in arestas:

        if uf.union(u, v):

            agm.append((u, v, peso))

            custo_total += peso

    return agm, custo_total