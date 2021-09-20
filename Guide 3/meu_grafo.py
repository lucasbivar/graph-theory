from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import deque
from copy import deepcopy

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
    
    def __gerar_caminho_ciclo(self, verticeInicial, v, pai, ciclo):
        '''
        Gera de maneira recursiva a lista com o ciclo, com base no dicionário 
        de vértices contendo os seus respectivos pais.
        :param verticeInicial: Vértice de partida do ciclo
        :param v: Vertice atual na chamada recursiva
        :param pai: Dicionário que armazena o vértice que era anterior a um
        vertice x no fluxo da DFS e a aresta que liga os dois vértices
        '''
        if v not in pai: return

        ciclo.append(pai[v][1])
        ciclo.append(pai[v][0])

        if verticeInicial == pai[v][0]:
            return

        self.__gerar_caminho_ciclo(verticeInicial, pai[v][0], pai, ciclo)

    def __dfs_ciclo(self, V, arestaAnterior, verticeInicio, verticesAdjacentes, visitados, pai):
        '''
        Se for possivel, responsável por encontrar um ciclo saindo do 
        vértice de partida em um grafo para ele mesmo.
        :param V: Vértice atual da DFS 
        :param arestaAnterior: Rótulo da aresta pelo o qual veio o vértice V 
        no fluxo da DFS
        :param verticeInicio: Vértice de partida da DFS
        :param verticesAdjacentes: Dicionário com os vértices adjacentes 
        de cada vértice do grafo
        :param visitados: Vértices já visitados na DFS
        :param pai: Dicionário que armazena o vértice que era anterior a um
        vertice x no fluxo da DFS e a aresta que liga os dois vértices
        '''
        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            if verticeAdjacente == verticeInicio and rotuloAresta != arestaAnterior:
                pai[verticeAdjacente] = (V, rotuloAresta)
                return
                
            if verticeAdjacente not in visitados:
                pai[verticeAdjacente] = (V, rotuloAresta)
                visitados.add(verticeAdjacente)
                self.__dfs_ciclo(verticeAdjacente, rotuloAresta, verticeInicio, verticesAdjacentes, visitados, pai)


    def ha_ciclo(self):
        '''
        Caso exista, encontra um ciclo no grafo
        :return: Caso exista ciclo, retorna uma lista contendo um ciclo presente 
        no grafo, caso contrário, retorna o valor booleano False
        '''
        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        # tenta achar um ciclo partindo de cada vértice e voltando pra ele
        for v in self.N:
            pai = dict()
            visitados = set([v])
            if v not in verticesAdjacentes: continue

            self.__dfs_ciclo(v, None, v, verticesAdjacentes, visitados, pai)
          
            ciclo = [v]
            self.__gerar_caminho_ciclo(v, v, pai, ciclo)
            if len(ciclo) > 1 and ciclo[0] == ciclo[-1]: return ciclo

        return False

    def __dfs_melhor_proximo_caminho(self, V, distancias, verticesAdjacentes):
        '''
        Responsável por realizar a DFS no grafo e armazenar as distâncias de 
        cada vértice partindo do vértice inicial. As distâncias são armazenadas
        com objetivo de fazer com que a DFS adaptada que monta o caminho,
        encontre o melhor próximo vértice pra ir, ou seja, o vértice que vai 
        garantir uma maior profundidade
        :param V: Vértice atual da DFS
        :param distancias: Dicionário que inicia apenas com o vértice de partida
        e vai sendo preenchido com as distâncias dos vértices do grafo para o vértice 
        de partida ao longo da DFS
        :param verticesAdjacentes: Dicionário com os vértices adjacentes 
        de cada vértice do grafo
        '''
        if V not in verticesAdjacentes: return

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            if verticeAdjacente not in distancias:
                distancias[verticeAdjacente] = distancias[V] + 1
                self.__dfs_melhor_proximo_caminho(verticeAdjacente, distancias, verticesAdjacentes)
    
    def __dfs_caminho(self, V, visitados, caminho, verticesAdjacentes):
        '''
        Responsável por montar e encontrar o maior caminho partindo do 
        vértice V em um grafo.
        :param V: Vértice atual da DFS 
        :param visitados: Conjunto contendo os vértices já visitados pela DFS adaptada
        :param caminho: Lista para armazenar o caminho realizado pela DFS adaptada
        :param verticesAdjacentes: Dicionário com os vértices adjacentes 
        de cada vértice do grafo
        '''
        maiorCaminho = -1
        melhorVertice = None
        arestaMelhorVertice = None

        # novo grafo sem os vértices visitados
        novoGrafo = deepcopy(self)
        for v in visitados:
            if novoGrafo.existeVertice(v):
                novoGrafo.removeVertice(v)
        
        verticesAdjNovoGrafo = novoGrafo.__gerarVerticesAdjacencentes()

        # escolhe o melhor próximo vértice (que vai garantir um maior caminho)
        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            if verticeAdjacente not in visitados:
                distancias = {verticeAdjacente: 0}
                novoGrafo.__dfs_melhor_proximo_caminho(verticeAdjacente, distancias, verticesAdjNovoGrafo)
                
                distanciaMaxima = -1
                for key, value in distancias.items():
                    if value > distanciaMaxima: distanciaMaxima = value

                if distanciaMaxima > maiorCaminho:
                    maiorCaminho = distanciaMaxima
                    melhorVertice = verticeAdjacente
                    arestaMelhorVertice = rotuloAresta

        # adiciona o melhor vértice no caminho, e chama a DFS para ele
        if melhorVertice != None:
            visitados.add(melhorVertice)

            caminho.append(arestaMelhorVertice)
            caminho.append(melhorVertice)

            self.__dfs_caminho(melhorVertice, visitados, caminho, verticesAdjacentes)
               

    def caminho(self, n):
        '''
        Encontra um caminho de tamanho "n" no grafo.
        :param n: Tamanho do caminho desejado
        :return: Uma lista contendo o caminho de tamanho "n" caso exista, caso 
        contrário retorna o valor booleano False
        '''
        if n <= 0: return False

        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        # para cada vértice do grafo, encontra o maior caminho partindo dele,
        # enquanto não achar um que satisfaz o caminho de tamanho "n"
        for v in self.N:
            if v not in verticesAdjacentes: continue

            visitados = set([v])
            caminho = [v]
            self.__dfs_caminho(v, visitados, caminho, verticesAdjacentes)

            if n < len(visitados):
                return caminho[:2*n+1]

        return False

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