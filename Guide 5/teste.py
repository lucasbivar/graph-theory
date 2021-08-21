from meu_grafo import MeuGrafo

konigsberg = MeuGrafo(["1", "2", "3", "4"])
konigsberg.adicionaAresta("a1", "1", "2")
konigsberg.adicionaAresta("a2", "1", "2")
konigsberg.adicionaAresta("a3", "1", "3")
konigsberg.adicionaAresta("a4", "1", "4")
konigsberg.adicionaAresta("a5", "1", "4")
konigsberg.adicionaAresta("a6", "2", "3")
konigsberg.adicionaAresta("a7", "3", "4")

print(konigsberg.caminho_euleriano())


grafo_e3 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G"])
grafo_e3.adicionaAresta("a1", "A", "B")
grafo_e3.adicionaAresta("a2", "A", "C")
grafo_e3.adicionaAresta("a3", "A", "F")
grafo_e3.adicionaAresta("a4", "A", "G")
grafo_e3.adicionaAresta("a5", "B", "G")
grafo_e3.adicionaAresta("a6", "B", "F")
grafo_e3.adicionaAresta("a7", "B", "C")
grafo_e3.adicionaAresta("a8", "C", "D")
grafo_e3.adicionaAresta("a9", "C", "E")
grafo_e3.adicionaAresta("a10", "C", "F")
grafo_e3.adicionaAresta("a11", "C", "G")
grafo_e3.adicionaAresta("a12", "D", "E")
grafo_e3.adicionaAresta("a13", "F", "G")

print(grafo_e3.caminho_euleriano())
