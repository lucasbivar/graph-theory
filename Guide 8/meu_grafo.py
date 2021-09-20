import math
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import deque
import heapq
from copy import deepcopy
from math import inf

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
            if len(ciclo) > 1: return ciclo

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
    

    def __vertices_conectados(self, verticeAtual, visitados, verticesAdjacentes):
        '''
        Encontra os vértices que estão na componente conexa do vértice de saída
        :param verticeAtual: Vértice atual (ou de saída) da DFS
        :param visitados: Conjunto responsável por armazenar os vértices já 
        visitados durante a busca
        :param verticesAdjacentes: Dicionário contendo os vértices adjacentes de
        cada vértice do grafo
        '''
        if verticeAtual not in verticesAdjacentes: return
        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[verticeAtual]:
            if verticeAdjacente not in visitados:
                visitados.add(verticeAdjacente)
                self.__vertices_conectados(verticeAdjacente, visitados, verticesAdjacentes)


    def __eh_ponte(self, rotuloAresta):
        '''
        Verifica se uma aresta é ponte
        :param rotuloAresta: Rótulo da aresta que deve ser verificada
        :return: Se for ponte, retorna True, caso contrário retorna False
        '''
        arestaAtual = self.A[rotuloAresta]
        v1 = arestaAtual.getV1()
        v2 = arestaAtual.getV2()

        self.removeAresta(rotuloAresta)
        visitados = set([v1])
        listaAdj = self.__gerarVerticesAdjacencentes()
        self.__vertices_conectados(v1, visitados, listaAdj)
        v_visitados_sem_aresta = len(visitados)

        self.adicionaAresta(rotuloAresta, v1, v2)
        visitados = set([v1])
        listaAdj = self.__gerarVerticesAdjacencentes()
        self.__vertices_conectados(v1, visitados, listaAdj)
        v_visitados_com_aresta = len(visitados)

        if v_visitados_com_aresta == v_visitados_sem_aresta:
            return False

        return True
            

    def __gerar_caminho_euleriano(self, verticeAtual, caminho):
        '''
        Gera o caminho euleriano do grafo.
        :param verticeAtual: Vértice atual (ou de saída) no algoritmo
        :param caminho: Lista para armazenar o caminho euleriano 
        '''
        caminho.append(verticeAtual)
        arestas = self.arestas_sobre_vertice(verticeAtual)

        if(len(arestas) == 0): return

        if(len(arestas) == 1):
            arestaAtual = self.A[arestas[0]]
            v1 = arestaAtual.getV1()
            v2 = arestaAtual.getV2()

            proximoVertice = v1 if verticeAtual == v2 else v2
            caminho.append(arestas[0])

            self.removeAresta(arestas[0])
            self.__gerar_caminho_euleriano(proximoVertice, caminho)
            return
        
        for aresta in arestas:
            if not self.__eh_ponte(aresta):
                arestaAtual = self.A[aresta]
                v1 = arestaAtual.getV1()
                v2 = arestaAtual.getV2()

                proximoVertice = v1 if verticeAtual == v2 else v2
                caminho.append(aresta)

                self.removeAresta(aresta)
                self.__gerar_caminho_euleriano(proximoVertice, caminho)
                return


    def caminho_euleriano(self):
        '''
        Encontra um caminho euleriano no grafo caso seja possível.
        :return: Caso exista um caminho euleriano, retorna uma lista contendo 
        o caminho de tamanho, caso contrário retorna o valor booleano False
        '''
        if not self.conexo():
            return False
        
        qtdGrauImpar = 0
        verticeSaida = None
        for v in self.N:
            grauV = self.grau(v)
            if grauV % 2 != 0:
                qtdGrauImpar += 1
                verticeSaida = v

            if qtdGrauImpar > 2:
                return False
        
        if qtdGrauImpar == 1:
            return False
        
        grafoCopia = deepcopy(self)
        caminho = []

        if verticeSaida != None:
            grafoCopia.__gerar_caminho_euleriano(verticeSaida, caminho)
        else:
            grafoCopia.__gerar_caminho_euleriano(grafoCopia.N[0], caminho)

        return caminho
    

    def __encontrarArestaMenorPeso(self):
        aresta = None
        menorPeso = inf
        for rotuloA in self.A:
            arestaAtual = self.A[rotuloA]
            if arestaAtual.getPeso() < menorPeso:
                menorPeso = arestaAtual.getPeso()
                aresta = rotuloA
        
        return aresta


    def mst_prim(self):
        """
        Algoritmo de Prim (Modificado) -> Encontra a Minimun Spanning Tree do Grafo.
        Referência: https://drive.google.com/file/d/1xdLgGBuF1P2_sSztH_bFUVxMFf1ZYz19/view
        :return: Caso exista uma MST, retorna um objeto MeuGrafo com a árvore, 
        caso contrário retorna o valor booleano False
        """
        if not self.conexo():
            return False

        arestaInicial = self.__encontrarArestaMenorPeso()
        if arestaInicial is None:
            return False

        arestaInicial = self.A[arestaInicial]
        v_inicial = arestaInicial.getV1()
        arvore_mst = MeuGrafo([v_inicial])
        vertices_mst = set([v_inicial])
  
        while len(vertices_mst) != len(self.N):
            menorPeso = inf
            arestaMenorPeso = None
            v_fora_mst = None

            for rotuloA in self.A:
                arestaAtual = self.A[rotuloA]
                v1 = arestaAtual.getV1()
                v2 = arestaAtual.getV2()
                v_na_mst, v_provavel_fora_mst = (v1, v2)  if v1 in vertices_mst else (v2, v1)

                if v_na_mst in vertices_mst and v_provavel_fora_mst not in vertices_mst:
                    if arestaAtual.getPeso() < menorPeso:
                        menorPeso = arestaAtual.getPeso()
                        arestaMenorPeso = rotuloA
                        v_fora_mst = v_provavel_fora_mst

            arestaMenorPeso = self.A[arestaMenorPeso]
            vertices_mst.add(v_fora_mst)
            arvore_mst.adicionaVertice(v_fora_mst)
            arvore_mst.adicionaAresta(arestaMenorPeso.getRotulo(), arestaMenorPeso.getV1(),
                arestaMenorPeso.getV2(), arestaMenorPeso.getPeso())

        return arvore_mst
    


    def mst_kruskal(self):
        """
        Algoritmo de Kruskal (Modificado) -> Encontra a Minimun Spanning Tree do Grafo.
        Referência: https://drive.google.com/file/d/1FFejlFlkMAV8KUSniGEMn4NR4v4rhsxj/view
        :return: Caso exista uma MST, retorna um objeto MeuGrafo com a árvore, 
        caso contrário retorna o valor booleano False
        """
        if not self.conexo():
            return False

        def find(x, pai):
            if pai[x] == x:
                return x

            pai[x] = find(pai[x], pai)
            return pai[x]

        def union(a, b, pai, peso):
            a = find(a, pai)
            b = find(b, pai)

            if a == b: return

            if peso[a] < peso[b]:
                pai[a] = b
            
            if peso[a] > peso[b]:
                pai[b] = a
            
            if peso[a] == peso[b]:
                pai[a] = b
                peso[b] += 1

        maiorPeso = self.A[max(self.A, key=lambda x: self.A[x].getPeso())].getPeso()
        menorPeso = self.A[min(self.A, key=lambda x: self.A[x].getPeso())].getPeso()

        quantidadeIntervalos = (maiorPeso-menorPeso)/((maiorPeso - menorPeso)/len(self.A))
        quantidadeIntervalos = math.floor(quantidadeIntervalos)

        E_buckets = [[] for i in range(quantidadeIntervalos+1)]
        E_buckets[0] = None

        for aresta in self.A:
            arestaAtual = self.A[aresta]
            c_e = arestaAtual.getPeso()

            j_e_posicao = (((c_e-menorPeso)/(maiorPeso-menorPeso))*(quantidadeIntervalos-1))+1
            j_e_posicao = math.floor(j_e_posicao)

            arestaFormatada = (arestaAtual.getPeso(), arestaAtual.getRotulo(), 
                        arestaAtual.getV1(), arestaAtual.getV2())

            E_buckets[j_e_posicao].append(arestaFormatada)
        

        arvore_mst = MeuGrafo()
        pai = {n: n for n in self.N}
        peso = {n: 0 for n in self.N}
        j = 1

        while len(arvore_mst.A) < len(self.N)-1:
            if len(E_buckets[j]) == 0:
                heapq.heapify(E_buckets[j])
                j += 1
            else:
                menorAtual = heapq.heappop(E_buckets[j])
                pesoAresta, rotuloAresta, v1, v2 = menorAtual

                if find(v1, pai) != find(v2, pai):
                    if not arvore_mst.existeVertice(v1): arvore_mst.adicionaVertice(v1)
                    if not arvore_mst.existeVertice(v2): arvore_mst.adicionaVertice(v2)
                    arvore_mst.adicionaAresta(rotuloAresta, v1, v2, pesoAresta)
                    union(v1, v2, pai, peso)

        return arvore_mst