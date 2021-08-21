from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        verticesNaoAdjacentes = list()
        for i in range(len(self.N)):
            for j in range(i+1, len(self.N)):
                novaAresta = f'{self.N[i]}-{self.N[j]}'
                if len(self.M[i][j]) == 0:
                    verticesNaoAdjacentes.append(novaAresta)
 
        return verticesNaoAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        qtdVertices = len(self.N)

        for i in range(qtdVertices):
          if len(self.M[i][i]) > 0:
            return True
        
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existeVertice(V):
            raise VerticeInvalidoException(f"O vértice {V} não existe no grafo.")

        indiceVertice = self.N.index(V)
        grau = 0

        for j in range(indiceVertice, len(self.N)):
            if j == indiceVertice:
                grau += 2*len(self.M[indiceVertice][j])
            else:
                grau += len(self.M[indiceVertice][j])
        
        for i in range(indiceVertice):
            grau += len(self.M[i][indiceVertice])

        return grau


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for i in range(len(self.N)):
            for j in range(i, len(self.N)):
                if len(self.M[i][j]) > 1:
                    return True
        
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existeVertice(V):
            raise VerticeInvalidoException(f"O vértice {V} não existe no grafo.")

        indiceVertice = self.N.index(V)
        arestas = set()

        for j in range(indiceVertice, len(self.N)):
            parAtual = self.M[indiceVertice][j]
            for aresta in parAtual:
                arestas.add(aresta)
        
        for i in range(indiceVertice):
            parAtual = self.M[i][indiceVertice]
            for aresta in parAtual:
                arestas.add(aresta)

        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False
        
        grauEsperado = len(self.N)-1
        for v in self.N:
            if self.grau(v) != grauEsperado:
                return False

        return True

