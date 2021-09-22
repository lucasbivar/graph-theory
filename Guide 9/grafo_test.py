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


        # Grafo Matriz Curricular
        self.eng_comp = MeuGrafo(["11", "12", "13", "14", "15","16", "17",
                      "21", "22", "23","24", "25", "26", "27",
                      "31", "32", "33", "34", "35", "36",
                      "41", "42", "43", "44", "45",
                      "51", "52", "53", "54", "55",
                      "61", "62", "63", "64", "65",
                      "71", "72", "73", "74", "75",
                      "81", "82", "83", "84", "85",
                      "91", "92", "93", "94",
                      "101", "102", "103"])

        self.eng_comp.adicionaAresta("d1", "11", "21")
        self.eng_comp.adicionaAresta("d2", "14", "24")
        self.eng_comp.adicionaAresta("d3", "14", "25")
        self.eng_comp.adicionaAresta("d4", "14", "34")
        self.eng_comp.adicionaAresta("d5", "14", "35")
        self.eng_comp.adicionaAresta("d6", "15", "24")
        self.eng_comp.adicionaAresta("d7", "15", "25")
        self.eng_comp.adicionaAresta("d8", "15", "34")
        self.eng_comp.adicionaAresta("d9", "15", "35")
        self.eng_comp.adicionaAresta("d10", "16", "26")
        self.eng_comp.adicionaAresta("d11", "21", "31")
        self.eng_comp.adicionaAresta("d12", "21", "41")
        self.eng_comp.adicionaAresta("d13", "24", "33")
        self.eng_comp.adicionaAresta("d14", "24", "43")
        self.eng_comp.adicionaAresta("d15", "24", "44")
        self.eng_comp.adicionaAresta("d16", "24", "53")
        self.eng_comp.adicionaAresta("d17", "24", "54")
        self.eng_comp.adicionaAresta("d18", "24", "72")
        self.eng_comp.adicionaAresta("d19", "26", "36")
        self.eng_comp.adicionaAresta("d20", "31", "51")
        self.eng_comp.adicionaAresta("d21", "31", "52")
        self.eng_comp.adicionaAresta("d22", "31", "64")
        self.eng_comp.adicionaAresta("d23", "34", "63")
        self.eng_comp.adicionaAresta("d24", "35", "63")
        self.eng_comp.adicionaAresta("d25", "34", "81")
        self.eng_comp.adicionaAresta("d26", "35", "81")
        self.eng_comp.adicionaAresta("d27", "36", "44")
        self.eng_comp.adicionaAresta("d28", "36", "45")
        self.eng_comp.adicionaAresta("d29", "36", "55")
        self.eng_comp.adicionaAresta("d30", "43", "62")
        self.eng_comp.adicionaAresta("d31", "44", "55")
        self.eng_comp.adicionaAresta("d32", "44", "93")
        self.eng_comp.adicionaAresta("d33", "45", "93")
        self.eng_comp.adicionaAresta("d34", "51", "61")
        self.eng_comp.adicionaAresta("d35", "52", "75")
        self.eng_comp.adicionaAresta("d36", "54", "81")
        self.eng_comp.adicionaAresta("d37", "55", "65")
        self.eng_comp.adicionaAresta("d38", "61", "84")
        self.eng_comp.adicionaAresta("d39", "61", "94")
        self.eng_comp.adicionaAresta("d40", "63", "73")
        self.eng_comp.adicionaAresta("d41", "64", "75")
        self.eng_comp.adicionaAresta("d42", "64", "84")
        self.eng_comp.adicionaAresta("d43", "73", "82")
        self.eng_comp.adicionaAresta("d44", "74", "83")
        self.eng_comp.adicionaAresta("d45", "75", "85")
        self.eng_comp.adicionaAresta("d46", "75", "94")
        self.eng_comp.adicionaAresta("d47", "83", "92")
        self.eng_comp.adicionaAresta("d48", "92", "103")



        self.matematica = MeuGrafo(["11", "12", "13", "14", "15","16", "17",
              "21", "22", "23","24", "25", "26", "27",
              "31", "32", "33", "34", "35", "36",
              "41", "42", "43", "44", "45", "46",
              "51", "52", "53", "54", "55", "56","57",
              "61", "62", "63", "64", "65", "66","67",
              "71", "72", "73", "74", "75", "77",
              "81", "82", "83", "84", "85", "87"])

        self.matematica.adicionaAresta("d1", "11", "21")
        self.matematica.adicionaAresta("d2", "11", "22")
        self.matematica.adicionaAresta("d3", "13", "22")
        self.matematica.adicionaAresta("d4", "16", "26")
        self.matematica.adicionaAresta("d5", "21", "31")
        self.matematica.adicionaAresta("d6", "22", "32")
        self.matematica.adicionaAresta("d7", "12", "33")
        self.matematica.adicionaAresta("d8", "12", "34")
        self.matematica.adicionaAresta("d9", "21", "41")
        self.matematica.adicionaAresta("d10", "23", "41")
        self.matematica.adicionaAresta("d11", "23", "42")
        self.matematica.adicionaAresta("d12", "32", "42")
        self.matematica.adicionaAresta("d13", "36", "43")
        self.matematica.adicionaAresta("d14", "34", "44")
        self.matematica.adicionaAresta("d15", "27", "45")
        self.matematica.adicionaAresta("d16", "33", "51")
        self.matematica.adicionaAresta("d17", "12", "52")
        self.matematica.adicionaAresta("d18", "32", "53")
        self.matematica.adicionaAresta("d19", "44", "54")
        self.matematica.adicionaAresta("d20", "44", "55")
        self.matematica.adicionaAresta("d21", "44", "57")
        self.matematica.adicionaAresta("d22", "51", "61")
        self.matematica.adicionaAresta("d23", "52", "62")
        self.matematica.adicionaAresta("d24", "32", "63")
        self.matematica.adicionaAresta("d25", "54", "64")
        self.matematica.adicionaAresta("d26", "46", "65")
        self.matematica.adicionaAresta("d27", "57", "67")
        self.matematica.adicionaAresta("d28", "42", "71")
        self.matematica.adicionaAresta("d29", "22", "72")
        self.matematica.adicionaAresta("d30", "41", "73")
        self.matematica.adicionaAresta("d31", "42", "73")
        self.matematica.adicionaAresta("d32", "64", "74")
        self.matematica.adicionaAresta("d33", "65", "75")
        self.matematica.adicionaAresta("d34", "67", "77")
        self.matematica.adicionaAresta("d35", "62", "81")
        self.matematica.adicionaAresta("d36", "75", "82")
        self.matematica.adicionaAresta("d37", "32", "83")
        self.matematica.adicionaAresta("d38", "74", "84")
        self.matematica.adicionaAresta("d39", "77", "87")

        self.construcao_edificios = MeuGrafo([
            '11', '12', '13', '14', '15', '16', '17', '18',
            '21', '22', '23', '24', '25', '26', '27',
            '31', '32', '33', '34', '35', '36', '37', '38',
            '41', '42', '43', '44', '45', '46', '47',
            '51', '52', '53', '54', '55', '56', '57', '58',
            '61', '62', '63', '64', '65', '66', '67', '68',
            '71', '72', '73'])

        self.construcao_edificios.adicionaAresta('d1', '15', '21')
        self.construcao_edificios.adicionaAresta('d2', '14', '23')
        self.construcao_edificios.adicionaAresta('d3', '11', '24')
        self.construcao_edificios.adicionaAresta('d4', '17', '24')
        self.construcao_edificios.adicionaAresta('d5', '15', '25')
        self.construcao_edificios.adicionaAresta('d6', '17', '26')
        self.construcao_edificios.adicionaAresta('d7', '17', '27')
        self.construcao_edificios.adicionaAresta('d8', '15', '32')
        self.construcao_edificios.adicionaAresta('d9', '21', '32')
        self.construcao_edificios.adicionaAresta('d10', '21', '33')
        self.construcao_edificios.adicionaAresta('d11', '25', '33')
        self.construcao_edificios.adicionaAresta('d12', '15', '34')
        self.construcao_edificios.adicionaAresta('d13', '11', '35')
        self.construcao_edificios.adicionaAresta('d14', '27', '35')
        self.construcao_edificios.adicionaAresta('d15', '26', '36')
        self.construcao_edificios.adicionaAresta('d16', '23', '37')
        self.construcao_edificios.adicionaAresta('d17', '24', '38')
        self.construcao_edificios.adicionaAresta('d18', '17', '41')
        self.construcao_edificios.adicionaAresta('d29', '21', '41')
        self.construcao_edificios.adicionaAresta('d20', '17', '42')
        self.construcao_edificios.adicionaAresta('d21', '21', '42')
        self.construcao_edificios.adicionaAresta('d22', '23', '43')
        self.construcao_edificios.adicionaAresta('d23', '24', '44')
        self.construcao_edificios.adicionaAresta('d24', '36', '45')
        self.construcao_edificios.adicionaAresta('d25', '37', '45')
        self.construcao_edificios.adicionaAresta('d26', '17', '46')
        self.construcao_edificios.adicionaAresta('d27', '32', '46')
        self.construcao_edificios.adicionaAresta('d28', '11', '47')
        self.construcao_edificios.adicionaAresta('d29', '37', '47')
        self.construcao_edificios.adicionaAresta('d30', '37', '51')
        self.construcao_edificios.adicionaAresta('d31', '43', '51')
        self.construcao_edificios.adicionaAresta('d32', '45', '51')
        self.construcao_edificios.adicionaAresta('d33', '46', '51')
        self.construcao_edificios.adicionaAresta('d34', '41', '52')
        self.construcao_edificios.adicionaAresta('d35', '42', '52')
        self.construcao_edificios.adicionaAresta('d36', '45', '52')
        self.construcao_edificios.adicionaAresta('d37', '46', '52')
        self.construcao_edificios.adicionaAresta('d38', '17', '53')
        self.construcao_edificios.adicionaAresta('d39', '32', '53')
        self.construcao_edificios.adicionaAresta('d40', '47', '54')
        self.construcao_edificios.adicionaAresta('d41', '17', '55')
        self.construcao_edificios.adicionaAresta('d42', '32', '55')
        self.construcao_edificios.adicionaAresta('d43', '46', '56')
        self.construcao_edificios.adicionaAresta('d44', '43', '57')
        self.construcao_edificios.adicionaAresta('d45', '31', '62')
        self.construcao_edificios.adicionaAresta('d46', '44', '62')
        self.construcao_edificios.adicionaAresta('d47', '22', '64')
        self.construcao_edificios.adicionaAresta('d48', '27', '64')
        self.construcao_edificios.adicionaAresta('d49', '33', '64')
        self.construcao_edificios.adicionaAresta('d50', '36', '64')
        self.construcao_edificios.adicionaAresta('d51', '47', '65')
        self.construcao_edificios.adicionaAresta('d52', '22', '66')
        self.construcao_edificios.adicionaAresta('d53', '31', '67')


        self.telematica = MeuGrafo([
            '11','12','13','14','15','16','17',
            '21','22','23','24','25','26','27',
            '31','32','33','34','35','36','37',
            '41','42','43','44','45','46','47',
            '51','52','53','54','55','56',
            '61','62','63','64','65'
            ])

        self.telematica.adicionaAresta('d1', '11', '21')
        self.telematica.adicionaAresta('d2', '12', '22')
        self.telematica.adicionaAresta('d3', '16', '22')
        self.telematica.adicionaAresta('d4', '12', '23')
        self.telematica.adicionaAresta('d5', '16', '23')
        self.telematica.adicionaAresta('d6', '13', '24')
        self.telematica.adicionaAresta('d7', '16', '26')
        self.telematica.adicionaAresta('d8', '21', '31')
        self.telematica.adicionaAresta('d9', '26', '32')
        self.telematica.adicionaAresta('d10', '22', '33')
        self.telematica.adicionaAresta('d11', '23', '33')
        self.telematica.adicionaAresta('d12', '26', '33')
        self.telematica.adicionaAresta('d13', '14', '34')
        self.telematica.adicionaAresta('d14', '25', '35')
        self.telematica.adicionaAresta('d15', '21', '36')
        self.telematica.adicionaAresta('d16', '24', '36')
        self.telematica.adicionaAresta('d17', '31', '41')
        self.telematica.adicionaAresta('d18', '31', '42')
        self.telematica.adicionaAresta('d19', '32', '43')
        self.telematica.adicionaAresta('d20', '32', '44')
        self.telematica.adicionaAresta('d21', '33', '44')
        self.telematica.adicionaAresta('d22', '33', '45')
        self.telematica.adicionaAresta('d23', '21', '46')
        self.telematica.adicionaAresta('d24', '34', '46')
        self.telematica.adicionaAresta('d25', '41', '51')
        self.telematica.adicionaAresta('d26', '41', '52')
        self.telematica.adicionaAresta('d27', '44', '53')
        self.telematica.adicionaAresta('d28', '44', '54')
        self.telematica.adicionaAresta('d29', '37', '55')
        self.telematica.adicionaAresta('d30', '41', '55')
        self.telematica.adicionaAresta('d31', '44', '55')
        self.telematica.adicionaAresta('d32', '42', '61')
        self.telematica.adicionaAresta('d33', '51', '61')
        self.telematica.adicionaAresta('d34', '53', '62')


        self.fisica = MeuGrafo([
            '11', '12', '13', '14', '15', '16', '17',
            '21', '22', '23', '24', '25', '26', '27',
            '31', '32', '33', '34', '35', '36', '37',
            '41', '42', '43', '44', '45', '46',
            '51', '52', '53', '54', '55', '56', '57',
            '61', '62', '63', '64', '65', '66', '68',
            '71', '72', '73', '74', '76',
            '81', '82', '83', '84', '85', '86'])

        self.fisica.adicionaAresta('d1', '11', '21')
        self.fisica.adicionaAresta('d2', '12', '21')
        self.fisica.adicionaAresta('d3', '11', '22')
        self.fisica.adicionaAresta('d4', '12', '22')
        self.fisica.adicionaAresta('d5', '12', '23')
        self.fisica.adicionaAresta('d6', '12', '24')
        self.fisica.adicionaAresta('d7', '14', '24')
        self.fisica.adicionaAresta('d8', '15', '25')
        self.fisica.adicionaAresta('d9', '21', '31')
        self.fisica.adicionaAresta('d10', '23', '31')
        self.fisica.adicionaAresta('d10', '21', '31')
        self.fisica.adicionaAresta('d11', '22', '32')
        self.fisica.adicionaAresta('d12', '23', '33')
        self.fisica.adicionaAresta('d13', '31', '41')
        self.fisica.adicionaAresta('d14', '31', '42')
        self.fisica.adicionaAresta('d15', '32', '42')
        self.fisica.adicionaAresta('d16', '33', '45')
        self.fisica.adicionaAresta('d17', '31', '46')
        self.fisica.adicionaAresta('d18', '41', '51')
        self.fisica.adicionaAresta('d19', '45', '51')
        self.fisica.adicionaAresta('d20', '41', '52')
        self.fisica.adicionaAresta('d21', '42', '52')
        self.fisica.adicionaAresta('d22', '45', '53')
        self.fisica.adicionaAresta('d23', '31', '54')
        self.fisica.adicionaAresta('d24', '43', '55')
        self.fisica.adicionaAresta('d25', '21', '57')
        self.fisica.adicionaAresta('d26', '43', '57')
        self.fisica.adicionaAresta('d27', '51', '61')
        self.fisica.adicionaAresta('d28', '51', '62')
        self.fisica.adicionaAresta('d29', '52', '62')
        self.fisica.adicionaAresta('d30', '21', '63')
        self.fisica.adicionaAresta('d31', '53', '63')
        self.fisica.adicionaAresta('d32', '51', '64')
        self.fisica.adicionaAresta('d33', '56', '66')
        self.fisica.adicionaAresta('d34', '31', '68')
        self.fisica.adicionaAresta('d35', '57', '68')
        self.fisica.adicionaAresta('d36', '61', '71')
        self.fisica.adicionaAresta('d37', '41', '72')
        self.fisica.adicionaAresta('d38', '45', '72')
        self.fisica.adicionaAresta('d39', '66', '73')
        self.fisica.adicionaAresta('d40', '31', '74')
        self.fisica.adicionaAresta('d41', '43', '74')
        self.fisica.adicionaAresta('d51', '41', '76')
        self.fisica.adicionaAresta('d52', '68', '76')
        self.fisica.adicionaAresta('d42', '65', '81')
        self.fisica.adicionaAresta('d43', '74', '82')
        self.fisica.adicionaAresta('d44', '73', '83')
        self.fisica.adicionaAresta('d45', '54', '84')
        self.fisica.adicionaAresta('d46', '71', '84')
        self.fisica.adicionaAresta('d47', '16', '85')
        self.fisica.adicionaAresta('d48', '25', '85')
        self.fisica.adicionaAresta('d49', '51', '86')
        self.fisica.adicionaAresta('d50', '76', '86')

        self.letras = MeuGrafo([
            '11', '12', '13', '14', '15', '16', '17',
            '21', '22', '23', '24', '25', '26', '27',
            '31', '32', '33', '34', '35', '36', '37',
            '41', '42', '43', '44', '45', '46', '47',
            '51', '52', '53', '54', '55', '56', '57',
            '61', '62', '63', '64', '65', '66', '67', '68',
            '71', '72', '73', '74', '75', '76', '77', '78',
            '81', '82', '83', '84', '85', '86', '87', '88'])

        self.letras.adicionaAresta('d1', '11', '21')
        self.letras.adicionaAresta('d2', '11', '22')
        self.letras.adicionaAresta('d3', '12', '23')
        self.letras.adicionaAresta('d4', '12', '25')
        self.letras.adicionaAresta('d5', '17', '26')
        self.letras.adicionaAresta('d6', '21', '31')
        self.letras.adicionaAresta('d7', '21', '32')
        self.letras.adicionaAresta('d8', '21', '33')
        self.letras.adicionaAresta('d9', '24', '34')
        self.letras.adicionaAresta('d10', '25', '35')
        self.letras.adicionaAresta('d11', '31', '41')
        self.letras.adicionaAresta('d12', '33', '42')
        self.letras.adicionaAresta('d13', '25', '43')
        self.letras.adicionaAresta('d14', '25', '44')
        self.letras.adicionaAresta('d15', '36', '44')
        self.letras.adicionaAresta('d16', '23', '46')
        self.letras.adicionaAresta('d17', '35', '46')
        self.letras.adicionaAresta('d18', '37', '47')
        self.letras.adicionaAresta('d19', '31', '51')
        self.letras.adicionaAresta('d20', '35', '52')
        self.letras.adicionaAresta('d21', '13', '53')
        self.letras.adicionaAresta('d22', '45', '54')
        self.letras.adicionaAresta('d23', '35', '55')
        self.letras.adicionaAresta('d24', '22', '56')
        self.letras.adicionaAresta('d25', '43', '57')
        self.letras.adicionaAresta('d26', '31', '61')
        self.letras.adicionaAresta('d27', '31', '62')
        self.letras.adicionaAresta('d28', '35', '63')
        self.letras.adicionaAresta('d29', '54', '64')
        self.letras.adicionaAresta('d30', '37', '67')
        self.letras.adicionaAresta('d31', '54', '68')
        self.letras.adicionaAresta('d32', '31', '71')
        self.letras.adicionaAresta('d33', '31', '72')
        self.letras.adicionaAresta('d34', '31', '73')
        self.letras.adicionaAresta('d35', '64', '74')
        self.letras.adicionaAresta('d36', '35', '75')
        self.letras.adicionaAresta('d37', '45', '76')
        self.letras.adicionaAresta('d38', '27', '77')
        self.letras.adicionaAresta('d39', '53', '77')
        self.letras.adicionaAresta('d40', '64', '78')
        self.letras.adicionaAresta('d41', '68', '78')
        self.letras.adicionaAresta('d42', '17', '83')
        self.letras.adicionaAresta('d43', '74', '84')
        self.letras.adicionaAresta('d44', '77', '87')
        self.letras.adicionaAresta('d45', '74', '88')
        self.letras.adicionaAresta('d46', '78', '88')

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
    

    def test_ordenacao_topologica(self):
        self.assertEqual(self.eng_comp.ordenacao_topologica(), ['11', '12', '13', '14', 
        '15', '16', '17', '22', '23', '27', '32', '42', '71', '74', '91', '101', '102', 
        '21', '24', '25', '26', '34', '35', '83', '31', '33', '36', '41', '43', '53', 
        '54', '63', '72', '92', '44', '45', '51', '52', '62', '64', '73', '81', '103', 
        '55', '61', '75', '82', '93', '65', '84', '85', '94'])

        self.assertEqual(self.matematica.ordenacao_topologica(), ['11', '12', '13', 
        '14', '15', '16', '17', '23', '24', '25', '27', '35', '36', '46', '56', '66', 
        '85', '21', '22', '26', '33', '34', '43', '45', '52', '65', '31', '32', '41', 
        '44', '51', '62', '72', '75', '42', '53', '54', '55', '57', '61', '63', '81', 
        '82', '83', '64', '67', '71', '73', '74', '77', '84', '87'])

        self.assertEqual(self.construcao_edificios.ordenacao_topologica(), ['11', '12', 
        '13', '14', '15', '16', '17', '18', '22', '31', '58', '61', '63', '68', '71', '72', 
        '73', '21', '23', '24', '25', '26', '27', '34', '66', '67', '32', '33', '35', '36',
        '37', '38', '41', '42', '43', '44', '45', '46', '47', '53', '55', '57', '62', '64', 
        '51', '52', '54', '56', '65'])

        self.assertEqual(self.telematica.ordenacao_topologica(), ['11', '12', '13', '14', 
        '15', '16', '17', '25', '27', '37', '47', '56', '63', '64', '65', '21', '22', '23', 
        '24', '26', '34', '35', '31', '32', '33', '36', '46', '41', '42', '43', '44', '45', 
        '51', '52', '53', '54', '55', '61', '62'])

        self.assertEqual(self.fisica.ordenacao_topologica(), ['11', '12', '13', '14', '15',
        '16', '17', '26', '27', '34', '35', '36', '37', '43', '44', '56', '65', '21', '22', 
        '23', '24', '25', '55', '66', '81', '31', '32', '33', '57', '73', '85', '41', '42', 
        '45', '46', '54', '68', '74', '83', '51', '52', '53', '72', '76', '82', '61', '62', 
        '63', '64', '86', '71', '84'])

        self.assertEqual(self.letras.ordenacao_topologica(), ['11', '12', '13', '14', '15', 
        '16', '17', '24', '27', '36', '37', '45', '65', '66', '81', '82', '85', '86', '21',
        '22', '23', '25', '26', '34', '47', '53', '54', '67', '76', '83', '31', '32', '33', 
        '35', '43', '44', '56', '64', '68', '77', '41', '42', '46', '51', '52', '55', '57', 
        '61', '62', '63', '71', '72', '73', '74', '75', '78', '87', '84', '88'])

