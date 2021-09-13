from meu_grafo_matriz_adjacencia_dir import MeuGrafo

g_d3 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G", "H"])
g_d3.adicionaAresta("k1", "A", "B", 20)
g_d3.adicionaAresta("k2", "A", "D", 80)
g_d3.adicionaAresta("k3", "A", "G", 90)
g_d3.adicionaAresta("k4", "B", "F", 10)
g_d3.adicionaAresta("k5", "C", "F", 50)
g_d3.adicionaAresta("k6", "C", "H", 20)
g_d3.adicionaAresta("k7", "D", "G", 20)
g_d3.adicionaAresta("k8", "E", "B", 50)
g_d3.adicionaAresta("k9", "E", "G", 30)
g_d3.adicionaAresta("k10", "F", "C", 10)
g_d3.adicionaAresta("k11", "F", "D", 40)
g_d3.adicionaAresta("k12", "G", "A", 20)
g_d3.adicionaAresta("k13", "G", "A", 20)
g_d3.adicionaAresta("k14", "D", "C", 10)
g_d3.adicionaAresta("k15", "C", "D", 10)

print(g_d3.dijkstra_drone("C", "B", 5, 222, ["A", "H", "G", "D"]))


