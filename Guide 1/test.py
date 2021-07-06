# from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import MeuGrafo

paraiba = MeuGrafo()

paraiba.adicionaVertice('J')
paraiba.adicionaVertice('C')
paraiba.adicionaVertice('E')
paraiba.adicionaVertice('P')
paraiba.adicionaVertice('M')
paraiba.adicionaVertice('T')
paraiba.adicionaVertice('Z')

paraiba.adicionaAresta('a1', 'J','C')
paraiba.adicionaAresta('a2', 'C','E')
paraiba.adicionaAresta('a3', 'C','E')
paraiba.adicionaAresta('a4', 'C','P')
paraiba.adicionaAresta('a5', 'C','P')
paraiba.adicionaAresta('a6', 'C','M')
paraiba.adicionaAresta('a7', 'C','T')
paraiba.adicionaAresta('a8', 'M','T')
paraiba.adicionaAresta('a9', 'T','Z')

print(paraiba)