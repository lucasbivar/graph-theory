from meu_grafo import MeuGrafo

grafoRoteiro2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])

grafoRoteiro2.adicionaAresta('1', 'A', 'B')
grafoRoteiro2.adicionaAresta('2', 'A', 'G')
grafoRoteiro2.adicionaAresta('3', 'A', 'J')
grafoRoteiro2.adicionaAresta('4', 'K', 'G')
grafoRoteiro2.adicionaAresta('5', 'K', 'J')
grafoRoteiro2.adicionaAresta('6', 'J', 'G')
grafoRoteiro2.adicionaAresta('7', 'J', 'I')
grafoRoteiro2.adicionaAresta('8', 'I', 'G')
grafoRoteiro2.adicionaAresta('9', 'G', 'H')
grafoRoteiro2.adicionaAresta('10', 'H', 'F')
grafoRoteiro2.adicionaAresta('11', 'F', 'B')
grafoRoteiro2.adicionaAresta('12', 'G', 'B')
grafoRoteiro2.adicionaAresta('13', 'B', 'C')
grafoRoteiro2.adicionaAresta('14', 'C', 'D')
grafoRoteiro2.adicionaAresta('15', 'D', 'E')
grafoRoteiro2.adicionaAresta('16', 'B', 'D')
grafoRoteiro2.adicionaAresta('17', 'B', 'E')

print(grafoRoteiro2)

print(grafoRoteiro2.dfs('K'))
print(grafoRoteiro2.bfs('K'))
