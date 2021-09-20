from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from math import inf

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

    def __matriz_sem_lacos_e_paralelas(self):
        copia_m_adj = deepcopy(self.M)

        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if i == j and len(copia_m_adj[i][j]) != 0:
                    copia_m_adj[i][j] = dict()

                if len(copia_m_adj[i][j]) > 1:
                    menorRotulo = None
                    menorAresta = None
                    menorPeso = inf
                    for rotuloAresta, aresta_obj in copia_m_adj[i][j].items():
                        if aresta_obj.getPeso() < menorPeso:
                            menorPeso = aresta_obj.getPeso()
                            menorRotulo = rotuloAresta
                            menorAresta = aresta_obj

                    copia_m_adj[i][j] = {menorRotulo: menorAresta}

        return copia_m_adj
    
    def dijkstra_drone(self, v_fonte, v_destino, carga, carga_maxima, pontos_recarga):
        if not self.existeVertice(v_fonte) or not self.existeVertice(v_destino):
            raise VerticeInvalidoException(
                "Os vértices passados não existem no grafo.")

        # removendo laços e paralelas
        copia_m_adj_dir = self.__matriz_sem_lacos_e_paralelas()

        # peso do menor caminho entre v_fonte e vertice r
        beta = {n: inf for n in self.N}
        phi = {n: 0 for n in self.N}  # permanente ou temporário
        pi = {n: 0 for n in self.N}  # predecessores
        gama = {n: None for n in self.N}  # cargas

        beta[v_fonte] = 0
        phi[v_fonte] = 1
        gama[v_fonte] = carga

        w = v_fonte
        while True:
            if w in pontos_recarga:
                gama[w] = carga_maxima
       
        
            for v in copia_m_adj_dir[self.N.index(w)]:
                for _, aresta in v.items():
                    v1 = aresta.getV1()
                    v2 = aresta.getV2()
                    r = v1 if w == v2 else v2
                    alpha_w_r = aresta.getPeso()
                  
                    if phi[r] == 0 and beta[r] > beta[w] + alpha_w_r and gama[w] >= alpha_w_r:
                        gama[r] = gama[w] - alpha_w_r
                        beta[r] = beta[w] + alpha_w_r
                        pi[r] = w
                    
                   

            beta_menor_valor = inf
            r_star = None
            for v in self.N:
                if phi[v] == 0 and beta[v] < beta_menor_valor:
                    beta_menor_valor = beta[v]
                    r_star = v
                

            if r_star == None:
                return False
            else:
                phi[r_star] = 1
                w = r_star

            if w == v_destino:
                break

        caminho = [v_destino]
        atual = v_destino
        while pi[atual] != 0:
            atual = pi[atual]
            caminho.append(atual)
        
        return caminho[::-1]
