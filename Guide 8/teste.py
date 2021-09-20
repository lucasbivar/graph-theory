from meu_grafo import MeuGrafo

g = MeuGrafo(["A", "B", "C", "D", "E", "F", "G", "H"])
g.adicionaAresta("k1", "A", "B", 20)
g.adicionaAresta("k2", "A", "D", 80)
g.adicionaAresta("k3", "A", "G", 90)
g.adicionaAresta("k4", "B", "F", 10)
g.adicionaAresta("k5", "C", "F", 50)
g.adicionaAresta("k6", "C", "H", 20)
g.adicionaAresta("k7", "D", "G", 20)
g.adicionaAresta("k8", "E", "B", 50)
g.adicionaAresta("k9", "E", "G", 30)
g.adicionaAresta("k10", "F", "C", 10)
g.adicionaAresta("k11", "F", "D", 40)
g.adicionaAresta("k12", "G", "A", 20)
g.adicionaAresta("k13", "G", "A", 20)
g.adicionaAresta("k14", "D", "C", 10)
g.adicionaAresta("k15", "C", "D", 10)


kruskal_mst = g.mst_kruskal()

print(kruskal_mst)
print(len(kruskal_mst.N))
print(len(kruskal_mst.A))

soma = 0
for a in kruskal_mst.A:
  soma += kruskal_mst.A[a].getPeso()

print("Kruskal MST Cost", soma)


prim_mst = g.mst_prim()

print(prim_mst)
print(len(prim_mst.N))
print(len(prim_mst.A))

soma = 0
for a in prim_mst.A:
  soma += prim_mst.A[a].getPeso()

print("Prim MST Cost", soma)