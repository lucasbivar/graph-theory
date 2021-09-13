import unittest
from bibgrafo.grafo_exceptions import *
from meu_grafo_matriz_adjacencia_dir import MeuGrafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g_a0 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_a0.adicionaAresta('a1', 'J', 'C')
        self.g_a0.adicionaAresta('a2', 'C', 'E')
        self.g_a0.adicionaAresta('a3', 'C', 'E')
        self.g_a0.adicionaAresta('a4', 'P', 'C')
        self.g_a0.adicionaAresta('a5', 'P', 'C')
        self.g_a0.adicionaAresta('a6', 'T', 'C')
        self.g_a0.adicionaAresta('a7', 'M', 'C')
        self.g_a0.adicionaAresta('a8', 'M', 'T')
        self.g_a0.adicionaAresta('a9', 'T', 'Z')

        self.g_a1 = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_a1.adicionaAresta('a1','J','C')
        self.g_a1.adicionaAresta('a2', 'J', 'E')
        self.g_a1.adicionaAresta('a3', 'J', 'P')
        self.g_a1.adicionaAresta('a4', 'E', 'C')
        self.g_a1.adicionaAresta('a5', 'P', 'C')
        self.g_a1.adicionaAresta('a6', 'P', 'E')

        self.g_a2 = MeuGrafo(['Nina', 'Maria'])
        self.g_a2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_a3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_a4 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_a4.adicionaAresta('a1', 'A', 'A')
        self.g_a4.adicionaAresta('a2', 'A', 'B')
        self.g_a4.adicionaAresta('a3', 'A', 'A')

        self.g_a5 = MeuGrafo(['Luisa','Pedro', 'Rebeca', 'Valentina', 'Enzo', 'Augusto',
         'Leticia', 'Amanda', 'Lucas', 'Isabel'])
        self.g_a5.adicionaAresta('a1', 'Pedro', 'Valentina')
        self.g_a5.adicionaAresta('a2', 'Enzo', 'Valentina')
        self.g_a5.adicionaAresta('a3', 'Pedro', 'Enzo')
        self.g_a5.adicionaAresta('a4', 'Rebeca', 'Augusto')
        self.g_a5.adicionaAresta('a5', 'Augusto', 'Leticia')
        self.g_a5.adicionaAresta('a6', 'Leticia', 'Rebeca')
        self.g_a5.adicionaAresta('a7', 'Amanda', 'Lucas')
        self.g_a5.adicionaAresta('a8', 'Amanda', 'Isabel')
        self.g_a5.adicionaAresta('a9', 'Lucas', 'Isabel')

        #Grafo rede social com arestas paralelas
        self.g_a6 = MeuGrafo(['Joao', 'Henrique', 'Maria', 'Isabella', 'Vinicius'])
        self.g_a6.adicionaAresta('amizade1', 'Joao', 'Vinicius')
        self.g_a6.adicionaAresta('amizade2', 'Vinicius', 'Joao')
        self.g_a6.adicionaAresta('amizade3', 'Isabella', 'Joao')
        self.g_a6.adicionaAresta('amizade4', 'Maria', 'Isabella')
        self.g_a6.adicionaAresta('amizade5', 'Henrique', 'Joao')
        self.g_a6.adicionaAresta('amizade6', 'Vinicius', 'Maria')
        self.g_a6.adicionaAresta('amizade7', 'Isabella', 'Henrique')
        self.g_a6.adicionaAresta('amizade8', 'Isabella', 'Henrique')
       
        self.g_a7 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_a7.adicionaAresta("1", "A", "B")
        self.g_a7.adicionaAresta("2", "A", "G")
        self.g_a7.adicionaAresta("3", "A", "J")
        self.g_a7.adicionaAresta("4", "K", "G")
        self.g_a7.adicionaAresta("5", "K", "J")
        self.g_a7.adicionaAresta("6", "J", "G")
        self.g_a7.adicionaAresta("7", "J", "I")
        self.g_a7.adicionaAresta("8", "I", "G")
        self.g_a7.adicionaAresta("9", "G", "H")
        self.g_a7.adicionaAresta("10", "H", "F")
        self.g_a7.adicionaAresta("11", "F", "B")
        self.g_a7.adicionaAresta("12", "B", "G")
        self.g_a7.adicionaAresta("13", "B", "C")
        self.g_a7.adicionaAresta("14", "C", "D")
        self.g_a7.adicionaAresta("15", "D", "E")
        self.g_a7.adicionaAresta("16", "D", "B")
        self.g_a7.adicionaAresta("17", "E", "B")

        self.g_a8 = MeuGrafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.g_a8.adicionaAresta('a1', '1', '2')
        self.g_a8.adicionaAresta('a2', '2', '4')
        self.g_a8.adicionaAresta('a3', '3', '2')
        self.g_a8.adicionaAresta('a4', '2', '3')
        self.g_a8.adicionaAresta('a5', '2', '4')
        self.g_a8.adicionaAresta('a6', '2', '6')
        self.g_a8.adicionaAresta('a7', '2', '5')
        self.g_a8.adicionaAresta('a8', '5', '6')
        self.g_a8.adicionaAresta('a9', '8', '6')
        self.g_a8.adicionaAresta('a10', '7', '6')
        self.g_a8.adicionaAresta('a11', '8', '7')
        self.g_a8.adicionaAresta('a12', '8', '9')

        self.g_a9 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G"])
        self.g_a9.adicionaAresta("a1", "A", "B")
        self.g_a9.adicionaAresta("a2", "A", "C")
        self.g_a9.adicionaAresta("a3", "A", "F")
        self.g_a9.adicionaAresta("a4", "A", "G")
        self.g_a9.adicionaAresta("a5", "B", "G")
        self.g_a9.adicionaAresta("a6", "B", "F")
        self.g_a9.adicionaAresta("a7", "B", "C")
        self.g_a9.adicionaAresta("a8", "C", "D")
        self.g_a9.adicionaAresta("a9", "C", "E")
        self.g_a9.adicionaAresta("a10", "C", "F")
        self.g_a9.adicionaAresta("a11", "C", "G")
        self.g_a9.adicionaAresta("a12", "D", "E")
        self.g_a9.adicionaAresta("a13", "F", "G")


        self.g_d0 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G"])
        self.g_d0.adicionaAresta("a1", "A", "B", 1)
        self.g_d0.adicionaAresta("a2", "B", "C", 1)
        self.g_d0.adicionaAresta("a3", "B", "F", 3)
        self.g_d0.adicionaAresta("a4", "C", "D", 1)
        self.g_d0.adicionaAresta("a5", "C", "E", 2)
        self.g_d0.adicionaAresta("a6", "D", "E", 3)
        self.g_d0.adicionaAresta("a7", "E", "G", 2)
        self.g_d0.adicionaAresta("a8", "F", "G", 1)


        self.g_d1 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G"])
        self.g_d1.adicionaAresta("a1", "A", "B", 2)
        self.g_d1.adicionaAresta("a2", "A", "D", 3)
        self.g_d1.adicionaAresta("a3", "A", "C", 1)
        self.g_d1.adicionaAresta("a4", "B", "D", 1)
        self.g_d1.adicionaAresta("a5", "C", "D", 4)
        self.g_d1.adicionaAresta("a6", "C", "F", 5)
        self.g_d1.adicionaAresta("a7", "F", "G", 7)
        self.g_d1.adicionaAresta("a8", "E", "G", 10)
        self.g_d1.adicionaAresta("a9", "D", "E", 2)
        self.g_d1.adicionaAresta("a9", "D", "F", 2)


        self.g_d2 = MeuGrafo(["Joao", "Vini", "Isabela", "Maria", "Pedro", "Henrique", "Hugo", "Fernanda"])
        self.g_d2.adicionaAresta("l1", "Joao", "Isabela", 2)
        self.g_d2.adicionaAresta("l2", "Vini", "Isabela", 1)
        self.g_d2.adicionaAresta("l3", "Vini", "Fernanda", 3)
        self.g_d2.adicionaAresta("l4", "Fernanda", "Hugo", 2)
        self.g_d2.adicionaAresta("l5", "Isabela", "Pedro", 1)
        self.g_d2.adicionaAresta("l6", "Isabela", "Henrique", 4)
        self.g_d2.adicionaAresta("l7", "Isabela", "Maria", 6)
        self.g_d2.adicionaAresta("l8", "Pedro", "Henrique", 10)
        self.g_d2.adicionaAresta("l9", "Maria", "Henrique", 2)
        self.g_d2.adicionaAresta("l10", "Pedro", "Hugo", 6)
        self.g_d2.adicionaAresta("l11", "Henrique", "Hugo", 8)
        self.g_d2.adicionaAresta("l12", "Maria", "Fernanda", 8)


        self.g_d3 = MeuGrafo(["A", "B", "C", "D", "E", "F", "G", "H"])
        self.g_d3.adicionaAresta("k1", "A", "B", 20)
        self.g_d3.adicionaAresta("k2", "A", "D", 80)
        self.g_d3.adicionaAresta("k3", "A", "G", 90)
        self.g_d3.adicionaAresta("k4", "B", "F", 10)
        self.g_d3.adicionaAresta("k5", "C", "F", 50)
        self.g_d3.adicionaAresta("k6", "C", "H", 20)
        self.g_d3.adicionaAresta("k7", "D", "G", 20)
        self.g_d3.adicionaAresta("k8", "E", "B", 50)
        self.g_d3.adicionaAresta("k9", "E", "G", 30)
        self.g_d3.adicionaAresta("k10", "F", "C", 10)
        self.g_d3.adicionaAresta("k11", "F", "D", 40)
        self.g_d3.adicionaAresta("k12", "G", "A", 20)
        self.g_d3.adicionaAresta("k13", "G", "A", 20)
        self.g_d3.adicionaAresta("k14", "D", "C", 10)
        self.g_d3.adicionaAresta("k15", "C", "D", 10)


    def test_warshall(self):
        self.assertEqual(self.g_a0.warshall(), [[0, 1, 1, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], 
            [0, 1, 1, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
        
        self.assertEqual(self.g_a1.warshall(), [[0, 1, 1, 1], [0, 0, 0, 0], 
            [0, 1, 0, 0], [0, 1, 1, 0]])

        self.assertEqual(self.g_a2.warshall(), [[0, 1], [0, 0]])

        self.assertEqual(self.g_a3.warshall(), [[0]])

        self.assertEqual(self.g_a4.warshall(), [[1, 1, 0, 0], [0, 0, 0, 0], 
            [0, 0, 0, 0], [0, 0, 0, 0]])

        self.assertEqual(self.g_a5.warshall(), [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        self.assertEqual(self.g_a6.warshall(), [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])

        self.assertEqual(self.g_a7.warshall(), [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])

        self.assertEqual(self.g_a8.warshall(), [[0, 1, 1, 1, 1, 1, 0, 0, 0], 
            [0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        
        self.assertEqual(self.g_a9.warshall(), [[0, 1, 1, 1, 1, 1, 1], 
        [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])


    def test_dijkstra(self):
        self.assertEqual(self.g_d0.dijkstra_drone("A", "G", 6, 20, []), ['A', 'B', 'F', 'G'])
        
        self.assertEqual(self.g_d0.dijkstra_drone("A", "G", 3, 15, ["C"]), ['A', 'B', 'C', 'E', 'G'])
        
        self.assertEqual(self.g_d1.dijkstra_drone("A", "G", 3, 10, ["E", "G"]), False)
        
        self.assertEqual(self.g_d1.dijkstra_drone("A", "E", 2, 5, ["B"]), ['A', 'B', 'D', 'E'])
        
        self.assertEqual(self.g_d2.dijkstra_drone("Vini", "Hugo", 4, 23, ["Fernanda", "Maria"]), 
            ['Vini', 'Fernanda', 'Hugo'])
        
        self.assertEqual(self.g_d2.dijkstra_drone("Joao", "Fernanda", 2, 50, ["Isabela", "Maria"]), 
            ['Joao', 'Isabela', 'Maria', 'Fernanda'])
        
        self.assertEqual(self.g_d2.dijkstra_drone("Isabela", "Hugo", 1, 5, 
            ["Pedro", "Maria", "Henrique"]), False)

        self.assertEqual(self.g_d2.dijkstra_drone("Vini", "Henrique", 2, 13, ["Pedro"]), 
            ['Vini', 'Isabela', 'Pedro', 'Henrique'])

        self.assertEqual(self.g_d2.dijkstra_drone("Isabela", "Hugo", 1, 8, 
            ["Pedro", "Maria", "Henrique"]), ['Isabela', 'Pedro', 'Hugo'])

        self.assertEqual(self.g_d3.dijkstra_drone("A", "H", 150, 200, []), 
            ['A', 'B', 'F', 'C', 'H'])
        
        self.assertEqual(self.g_d3.dijkstra_drone("B", "E", 50, 80, ["H", "A", "G", "D"]), False)

        self.assertEqual(self.g_d3.dijkstra_drone("B", "D", 10, 45, ["F", "E", "D"]), 
            ['B', 'F', 'C', 'D'])

        self.assertEqual(self.g_d3.dijkstra_drone("G", "E", 100, 200, ["G", "A", "D"]), False)

        self.assertEqual(self.g_d3.dijkstra_drone("E", "H", 120, 300, ["F", "A", "E", "D"]), 
            ['E', 'B', 'F', 'C', 'H'])

        self.assertEqual(self.g_d3.dijkstra_drone("C", "B", 5, 222, ["A", "H", "G", "D"]), False)