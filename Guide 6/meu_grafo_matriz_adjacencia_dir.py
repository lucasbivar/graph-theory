from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def warshall(self):
        E = []

        for i in range(len(self.N)):
            linha = []
            for j in range(len(self.N)):
                if len(self.M[i][j]) >= 1:
                    linha.append(1)
                else:
                    linha.append(0)
                    
            E.append(linha)

        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if E[j][i] == 1:
                    for k in range(len(self.N)):
                        E[j][k] = E[j][k] if E[j][k] > E[i][k] else E[i][k]

        return E

