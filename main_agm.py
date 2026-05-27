import os

from src.grafo import ler_grafo
from src.kruskal import kruskal
from src.prim import prim

# ---------------------------------------------------
# INSTÂNCIAS
# ---------------------------------------------------

instancias = [
    "dij10",
    "dij20",
    "dij40",
    "dij50"
]

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# ---------------------------------------------------
# EXECUÇÃO
# ---------------------------------------------------

print("\n===== ÁRVORE GERADORA MÍNIMA =====\n")

for nome in instancias:

    arquivo = os.path.join(
        BASE_DIR,
        "data",
        f"{nome}.txt"
    )

    grafo = ler_grafo(arquivo)

    # -----------------------------
    # KRUSKAL
    # -----------------------------

    _, custo_kruskal = kruskal(grafo)

    # -----------------------------
    # PRIM
    # -----------------------------

    _, custo_prim = prim(grafo)

    print(f"Instância: {nome}")

    print(f"Kruskal : {custo_kruskal}")

    print(f"Prim     : {custo_prim}")

    print()