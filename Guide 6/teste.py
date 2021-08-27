from meu_grafo_matriz_adjacencia_dir import MeuGrafo

g_a9 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G"])
g_a9.adicionaAresta("a1", "A", "B")
g_a9.adicionaAresta("a2", "A", "C")
g_a9.adicionaAresta("a3", "A", "F")
g_a9.adicionaAresta("a4", "A", "G")
g_a9.adicionaAresta("a5", "B", "G")
g_a9.adicionaAresta("a6", "B", "F")
g_a9.adicionaAresta("a7", "B", "C")
g_a9.adicionaAresta("a8", "C", "D")
g_a9.adicionaAresta("a9", "C", "E")
g_a9.adicionaAresta("a10", "C", "F")
g_a9.adicionaAresta("a11", "C", "G")
g_a9.adicionaAresta("a12", "D", "E")
g_a9.adicionaAresta("a13", "F", "G")
m = g_a9.warshall()

print(m)
# for l in m:
#   print(l)
