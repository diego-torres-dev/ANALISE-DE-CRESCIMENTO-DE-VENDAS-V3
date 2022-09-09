# Lista de produtos
produtos = [
    'iphone',
    'galaxy',
    'ipad',
    'tv',
    'máquina de café',
    'kindle',
    'geladeira',
    'adega',
    'notebook dell',
    'notebook hp',
    'notebook asus',
    'microsoft surface',
    'webcam',
    'caixa de som',
    'microfone',
    'câmera canon'
]

# Lista com dados de vendas de 2019
vendas2019 = [
    558147,
    712350,
    573823,
    405252,
    718654,
    531580,
    973139,
    892292,
    422760,
    154753,
    887061,
    438508,
    237467,
    489705,
    328311,
    591120
]

# Lista com dados de vendas de 2020
vendas2020 = [
    951642,
    244295,
    26964,
    787604,
    867660,
    78830,
    710331,
    646016,
    694913,
    539704,
    324831,
    667179,
    295633,
    725316,
    644622,
    994303
]

# Cria uma lista de tuplas com os dados de vendas de 2019 e de 2020
vendas = list(zip(vendas2019, vendas2020))

# Cria um dicionário
dic_vendas = dict(zip(produtos, vendas))

# Cabeçalho
print("-" * 65)
print("|{:^20}|{:^12}|{:^12}|{:^16}|".format(
    "PRODUTO", "2019", "2020", "CRESCIMENTO"))
print("-" * 65)

# Percorre as entradas do dicionário
for produto, vendas in dic_vendas.items():
    # Desempacota a tupla desta iteração
    vendas2019, vendas2020 = vendas

    # Calcula o crescimento percentual das vendas
    crescimento = (vendas2020 / vendas2019) - 1

    # Verifica se as vendas de 2020 foram maiores que as de 2019
    if vendas2020 > vendas2019:
        crescimento = "{:.2%} 🠕".format(crescimento)
    else:
        crescimento = "{:.2%} 🠗".format(crescimento)

    # Exibição de resultados
    print("|{:<20}|{:>12}|{:>12}|{:^16}|".format(
        produto, vendas2019, vendas2020, crescimento))

# Rodapé
print("-" * 65)
