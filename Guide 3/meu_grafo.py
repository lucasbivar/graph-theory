from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import deque

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        # O(n^2)
        arestasGrafo = set()
        for a in self.A:
            arestaAtual = self.A[a]
            verticesAresta = f'{arestaAtual.getV1()}-{arestaAtual.getV2()}'
            arestasGrafo.add(verticesAresta)

        verticesNaoAdjacentes = list()
        for i in range(len(self.N)):
            for j in range(i+1, len(self.N)):
                novaAresta = f'{self.N[i]}-{self.N[j]}'
                if novaAresta not in arestasGrafo and novaAresta[::-1] not in arestasGrafo:
                    verticesNaoAdjacentes.append(novaAresta)
 
        return verticesNaoAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        # O(n)
        for a in self.A:
            arestaAtual = self.A[a]
            if arestaAtual.getV1() == arestaAtual.getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # O(n)
        if(not self.existeVertice(V)):
            raise VerticeInvalidoException()

        grau = 0
        for a in self.A:
            arestaAtual = self.A[a]
            if arestaAtual.getV1() == V:
                grau += 1
            if arestaAtual.getV2() == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        # O(n)
        arestas = set()
        for a in self.A:

            arestaAtual = self.A[a]
            verticesAresta = (arestaAtual.getV1(), arestaAtual.getV2())

            if verticesAresta in arestas or verticesAresta[::-1] in arestas:
                return True
            
            arestas.add(verticesAresta)

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # O(n)
        if not self.existeVertice(V):
            raise VerticeInvalidoException()

        rotulos = []
        for a in self.A:
            arestaAtual = self.A[a]
            if arestaAtual.getV1() == V or arestaAtual.getV2() == V:
                rotulos.append(a)
        
        return rotulos

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        # O(n^2) -> função grau eh executada em O(n)
        if self.ha_laco() or self.ha_paralelas():
            return False

        grauEsperado = len(self.N)-1
        for v in self.N:
            if self.grau(v) != grauEsperado:
                return False

        return True


    def __gerarVerticesAdjacencentes(self):
        '''
        Gera dicionário com os vertices adjacentes de cada vértice do grafo 
        para otimizar a realização da DFS e da BFS.
        '''
        verticesAdjacentes = {}

        for aresta in self.A:
            arestaAtual = self.A[aresta]
            if arestaAtual.getV1() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV1()] = [(arestaAtual.getV2(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV1()].append((arestaAtual.getV2(), aresta))
            
            if arestaAtual.getV2() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV2()] = [(arestaAtual.getV1(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV2()].append((arestaAtual.getV1(), aresta))

        return verticesAdjacentes


    def __dfs_recursivo(self, V, arvoreDfs, verticesVisitados, verticesAdjacentes):
        '''
        Responsável por percorrer o grafo de modo recursivo
        :param V: O vértice atual
        :param dfs: Grafo que será construido pela DFS
        :param verticesVisitados: Conjunto responsável por armazenar os 
        vértices já visitados durante a busca
        :param verticesAdjacentes: Lista de Adjacência do grafo
        '''
        verticesVisitados.add(V)
      
        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:

            if verticeAdjacente not in verticesVisitados:
                if not arvoreDfs.existeVertice(verticeAdjacente):
                    arvoreDfs.adicionaVertice(verticeAdjacente)
                arvoreDfs.adicionaAresta(rotuloAresta, V, verticeAdjacente)

                self.__dfs_recursivo(verticeAdjacente, arvoreDfs, verticesVisitados, verticesAdjacentes)


    def dfs(self, V=''):
        '''
        Provê um grafo gerado pela DFS partindo do vértice passado como parâmetro.
        :param V: O vértice de partida
        :return: Um objeto do tipo MeuGrafo com o grafo gerado
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # O(n+m) -> n - Quantidade de vértices; m - Quantidade de arestas
        if not self.existeVertice(V):
            raise VerticeInvalidoException(f'O vértice {V} passado como parâmetro não existe.')

        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        arvoreDfs = MeuGrafo([V])
        verticesVisitados = set()

        if V not in verticesAdjacentes: return arvoreDfs

        self.__dfs_recursivo(V, arvoreDfs, verticesVisitados, verticesAdjacentes)
        
        return arvoreDfs
    


    def bfs(self, V=''):
        '''
        Provê um grafo gerado pela BFS partindo do vértice passado como parâmetro.
        :param V: O vértice de partida
        :return: Um objeto do tipo MeuGrafo com o grafo gerado
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # O(n+m) -> n - Quantidade de vértices; m- Quantidade de arestas
        if not self.existeVertice(V):
            raise VerticeInvalidoException(f'O vértice {V} passado como parâmetro não existe.')

        arvoreBfs = MeuGrafo([V])

        verticesVisitados = set([V])
        fila = deque([V])

        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        if V not in verticesAdjacentes: return arvoreBfs

        while len(fila) != 0:
            verticeAtual = fila.popleft()

            for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[verticeAtual]:
                if verticeAdjacente not in verticesVisitados:
                    if not arvoreBfs.existeVertice(verticeAdjacente):
                        arvoreBfs.adicionaVertice(verticeAdjacente)

                    arvoreBfs.adicionaAresta(rotuloAresta, verticeAtual, verticeAdjacente)
     
                    verticesVisitados.add(verticeAdjacente)
                    fila.append(verticeAdjacente)

        return arvoreBfs

    def conexo(self):
        '''
        Verifica se o grafo é conexo
        :return: Um valor booleano que indica se o grafo é ou não conexo
        '''
        qtdVertices = len(self.N)
        
        # chama a BFS para um vértice qualquer
        arvoreBFS = self.bfs(self.N[0])

        qtdVerticesCompConexa = len(arvoreBFS.N)

        # verifica se a quantidade de vértices da componente conexa gerada pela BFS
        # é igual a quantidade de vértices do grafo original
        return qtdVertices == qtdVerticesCompConexa