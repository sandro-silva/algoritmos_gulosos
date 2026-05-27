import os

from src.grafo import ler_grafo

from src.dijkstra import (
    dijkstra,
    reconstruir_caminho
)

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

print("\n===== CAMINHO MÍNIMO =====\n")

for nome in instancias:

    arquivo = os.path.join(
        BASE_DIR,
        "data",
        f"{nome}.txt"
    )

    grafo = ler_grafo(arquivo)

    origem = 0

    destino = len(grafo) - 1

    distancias, anterior = dijkstra(
        grafo,
        origem
    )

    caminho = reconstruir_caminho(
        anterior,
        destino
    )

    print(f"Instância: {nome}")

    print(
        f"Menor distância: "
        f"{distancias[destino]}"
    )

    print(
        "Caminho:",
        " -> ".join(map(str, caminho))
    )

    print()