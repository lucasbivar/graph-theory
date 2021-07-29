from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import MeuGrafo

m1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
m1.adicionaAresta("1", "A", "B")
m1.adicionaAresta("2", "A", "G")
m1.adicionaAresta("3", "A", "J")
m1.adicionaAresta("4", "K", "G")
m1.adicionaAresta("5", "K", "J")
m1.adicionaAresta("6", "J", "G")
m1.adicionaAresta("7", "J", "I")
m1.adicionaAresta("8", "I", "G")
m1.adicionaAresta("9", "G", "H")
m1.adicionaAresta("10", "H", "F")
m1.adicionaAresta("11", "F", "B")
m1.adicionaAresta("12", "B", "G")
m1.adicionaAresta("13", "B", "C")
m1.adicionaAresta("14", "C", "D")
m1.adicionaAresta("15", "D", "E")
m1.adicionaAresta("16", "D", "B")
m1.adicionaAresta("17", "E", "B")

m2 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
m2.adicionaAresta('a1', '4', '1')
m2.adicionaAresta('a2', '4', '2')
m2.adicionaAresta('a3', '4', '3')
m2.adicionaAresta('a4', '4', '5')
m2.adicionaAresta('a5', '5', '6')
m2.adicionaAresta('a6', '5', '3')


m3 = MeuGrafo(['A', 'B', 'C'])
m3.adicionaAresta('a1', 'A', 'B')
m3.adicionaAresta('a2', 'A', 'C')
m3.adicionaAresta('a3', 'B', 'C')

g_p = MeuGrafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
g_p.adicionaAresta('a1', '1', '2')
g_p.adicionaAresta('a2', '2', '4')
g_p.adicionaAresta('a3', '3', '2')
g_p.adicionaAresta('a4', '2', '3')
g_p.adicionaAresta('a5', '2', '4')
g_p.adicionaAresta('a6', '2', '6')
g_p.adicionaAresta('a7', '2', '5')
g_p.adicionaAresta('a8', '5', '6')
g_p.adicionaAresta('a9', '8', '6')
g_p.adicionaAresta('a10', '7', '6')
g_p.adicionaAresta('a11', '8', '7')
g_p.adicionaAresta('a12', '8', '9')

g_d3 = MeuGrafo(['Luisa', 'Pedro', 'Rebeca', 'Valentina', 'Enzo', 'Augusto',
'Leticia', 'Amanda', 'Lucas', 'Isabel'])
g_d3.adicionaAresta('a1', 'Pedro', 'Valentina')
g_d3.adicionaAresta('a2', 'Enzo', 'Valentina')
g_d3.adicionaAresta('a3', 'Pedro', 'Enzo')
g_d3.adicionaAresta('a4', 'Rebeca', 'Augusto')
g_d3.adicionaAresta('a5', 'Augusto', 'Leticia')
g_d3.adicionaAresta('a6', 'Leticia', 'Rebeca')
g_d3.adicionaAresta('a7', 'Amanda', 'Lucas')
g_d3.adicionaAresta('a8', 'Amanda', 'Isabel')
g_d3.adicionaAresta('a9', 'Lucas', 'Isabel')

# print(m1.ha_ciclo())
# print(m2.ha_ciclo())
# print(m3.ha_ciclo())
# print(g_p.ha_ciclo())

print("Grafo G_P_editado")
for i in range(-4, 10):
  print(i, ':', g_p.caminho(i))

print()

print("Grafo M1")
for i in range(-4, 15):
  print(i, ':', m1.caminho(i))

print()

print("Grafo D3")
for i in range(-4, 15):
  print(i, ':', g_d3.caminho(i))


g_d2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
g_d2.adicionaAresta('a1', 'A', 'B')
g_d2.adicionaAresta('a2', 'A', 'C')
g_d2.adicionaAresta('a3', 'B', 'C')
g_d2.adicionaAresta('a4', 'C', 'D')
g_d2.adicionaAresta('a5', 'E', 'F')
print(g_d2.ha_ciclo())