from meu_grafo_matriz_adjacencia_dir import MeuGrafo

construcao_edificios = MeuGrafo([
            '11', '12', '13', '14', '15', '16', '17', '18',
            '21', '22', '23', '24', '25', '26', '27',
            '31', '32', '33', '34', '35', '36', '37', '38',
            '41', '42', '43', '44', '45', '46', '47',
            '51', '52', '53', '54', '55', '56', '57', '58',
            '61', '62', '63', '64', '65', '66', '67', '68',
            '71', '72', '73'])

construcao_edificios.adicionaAresta('d1', '15', '21')
construcao_edificios.adicionaAresta('d2', '14', '23')
construcao_edificios.adicionaAresta('d3', '11', '24')
construcao_edificios.adicionaAresta('d4', '17', '24')
construcao_edificios.adicionaAresta('d5', '15', '25')
construcao_edificios.adicionaAresta('d6', '17', '26')
construcao_edificios.adicionaAresta('d7', '17', '27')
construcao_edificios.adicionaAresta('d8', '15', '32')
construcao_edificios.adicionaAresta('d9', '21', '32')
construcao_edificios.adicionaAresta('d10', '21', '33')
construcao_edificios.adicionaAresta('d11', '25', '33')
construcao_edificios.adicionaAresta('d12', '15', '34')
construcao_edificios.adicionaAresta('d13', '11', '35')
construcao_edificios.adicionaAresta('d14', '27', '35')
construcao_edificios.adicionaAresta('d15', '26', '36')
construcao_edificios.adicionaAresta('d16', '23', '37')
construcao_edificios.adicionaAresta('d17', '24', '38')
construcao_edificios.adicionaAresta('d18', '17', '41')
construcao_edificios.adicionaAresta('d29', '21', '41')
construcao_edificios.adicionaAresta('d20', '17', '42')
construcao_edificios.adicionaAresta('d21', '21', '42')
construcao_edificios.adicionaAresta('d22', '23', '43')
construcao_edificios.adicionaAresta('d23', '24', '44')
construcao_edificios.adicionaAresta('d24', '36', '45')
construcao_edificios.adicionaAresta('d25', '37', '45')
construcao_edificios.adicionaAresta('d26', '17', '46')
construcao_edificios.adicionaAresta('d27', '32', '46')
construcao_edificios.adicionaAresta('d28', '11', '47')
construcao_edificios.adicionaAresta('d29', '37', '47')
construcao_edificios.adicionaAresta('d30', '37', '51')
construcao_edificios.adicionaAresta('d31', '43', '51')
construcao_edificios.adicionaAresta('d32', '45', '51')
construcao_edificios.adicionaAresta('d33', '46', '51')
construcao_edificios.adicionaAresta('d34', '41', '52')
construcao_edificios.adicionaAresta('d35', '42', '52')
construcao_edificios.adicionaAresta('d36', '45', '52')
construcao_edificios.adicionaAresta('d37', '46', '52')
construcao_edificios.adicionaAresta('d38', '17', '53')
construcao_edificios.adicionaAresta('d39', '32', '53')
construcao_edificios.adicionaAresta('d40', '47', '54')
construcao_edificios.adicionaAresta('d41', '17', '55')
construcao_edificios.adicionaAresta('d42', '32', '55')
construcao_edificios.adicionaAresta('d43', '46', '56')
construcao_edificios.adicionaAresta('d44', '43', '57')
construcao_edificios.adicionaAresta('d45', '31', '62')
construcao_edificios.adicionaAresta('d46', '44', '62')
construcao_edificios.adicionaAresta('d47', '22', '64')
construcao_edificios.adicionaAresta('d48', '27', '64')
construcao_edificios.adicionaAresta('d49', '33', '64')
construcao_edificios.adicionaAresta('d50', '36', '64')
construcao_edificios.adicionaAresta('d51', '47', '65')
construcao_edificios.adicionaAresta('d52', '22', '66')
construcao_edificios.adicionaAresta('d53', '31', '67')

print(len(construcao_edificios.N))
print(len(construcao_edificios.ordenacao_topologica()))
print(construcao_edificios.ordenacao_topologica())
