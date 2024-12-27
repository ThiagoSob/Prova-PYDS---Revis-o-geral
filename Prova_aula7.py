# Você tem um conjunto de dados fictícios que representa informações sobre a produção anual de diferentes culturas
# em várias fazendas ao longo de vários anos.
# Seu objetivo é realizar uma análise simples desses dados utilizando funções agregadoras.

# Tarefas:
# Encontre o ano com a produção total máxima e o ano com a produção total mínima:

    # Você deve somar a produção total de todas as fazendas para cada ano e determinar qual foi o ano com a maior e a menor produção.
# Identifique a cultura com a maior e a menor produção total ao longo dos anos:

    # Some a produção de cada cultura em todas as fazendas e anos, e identifique qual cultura teve a maior produção e qual teve a menor produção.
# Encontre a fazenda com a produção máxima e a fazenda com a produção mínima em um determinado ano:

    # Selecione um ano e, dentro desse ano, identifique a fazenda que obteve a maior produção e a que obteve a menor produção.

# Dados Fictícios:
# Para simplificar, vamos construir dados fictícios representando a produção anual de três culturas (milho, soja e trigo) em três fazendas
# (Fazenda A, Fazenda B, Fazenda C) ao longo de três anos (2021, 2022, 2023).


##BANCO DE DADOS:
banco_de_dados = {
    'Fazenda A':{
        'Milho':{'2021':147, '2022':223, '2023':104},
        'Soja':{'2021':57, '2022':95, '2023':103},
        'Trigo':{'2021':302, '2022':401, '2023':560}
        },
    'Fazenda B':{
            'Milho':{'2021':590, '2022':605, '2023':601},
            'Soja':{'2021':107, '2022':195, '2023':174},
            'Trigo':{'2021':157, '2022':135, '2023':174}
            },
    'Fazenda C':{
        'Milho':{'2021':54, '2022':35, '2023':78},
        'Soja':{'2021':603, '2022':774, '2023':875},
        'Trigo':{'2021':208, '2022':145, '2023':202}
        }
}




#Tarefa 1

def producao_maxima_minima(banco_de_dados):
    total_por_ano = {}

    for fazenda, culturas in banco_de_dados.items():
        for cultura, anos in culturas.items():
            for ano, producao in anos.items():
                if ano not in total_por_ano:
                    total_por_ano[ano] = 0
                total_por_ano[ano] += producao

    maximo = max(total_por_ano.items(), key=lambda item: item[1])[0]
    minimo = min(total_por_ano.items(), key=lambda item: item[1])[0]
    valor_maximo = max(total_por_ano.items(), key=lambda item: item[1])[1]
    valor_minimo = min(total_por_ano.items(), key=lambda item: item[1])[1]

    return f' -Ano com Produção Máxima: {maximo}\n    -> Seu valor é: {valor_maximo} Ton\n -Ano com Produção Mínima: {minimo}\n    -> Seu valor é: {valor_minimo} Ton'
print('====='*10)
print('\n\n')
print('Produção Total por Ano:\n')
print(producao_maxima_minima(banco_de_dados))
print('\n\n')
print('====='*10)

#Tarefa 2

def cultura_producao_maximo_minimo(banco_de_dados):
    total_por_cultura = {}

    for fazenda, culturas in banco_de_dados.items():
        for cultura, anos in culturas.items():
            if cultura not in total_por_cultura:
                total_por_cultura[cultura] = 0 
            for ano, producao in anos.items():
                total_por_cultura[cultura] += producao
    
    maximo = max(total_por_cultura.items() , key=lambda item: item[1])[0]
    minimo = min(total_por_cultura.items() , key=lambda item: item[1])[0]
    valor_maximo = max(total_por_cultura.items(), key=lambda item: item[1])[1]
    valor_minimo = min(total_por_cultura.items(), key=lambda item: item[1])[1]
    
    return f' -Produção Máxima: {maximo}\n    -> Seu valor é: {valor_maximo} Ton\n -Produção Mínima: {minimo}\n    -> Seu valor é:{valor_minimo} Ton'

print('\n\n')
print('Produção Total por Cultura:\n')
print(cultura_producao_maximo_minimo(banco_de_dados))
print('\n\n')
print('====='*10)


#Tarefa 3

def fazenda_producao_maximo_minimo(ano_escolhido):
    
    total_por_fazenda_ano = {}

    for fazenda, culturas in banco_de_dados.items():
        total_por_fazenda_ano[fazenda] ={}
        for cultura, anos in culturas.items():
            for ano, producao in anos.items():
                if ano == ano_escolhido:
                    if ano not in total_por_fazenda_ano[fazenda]:
                        total_por_fazenda_ano[fazenda][ano] = 0
                    total_por_fazenda_ano[fazenda][ano] += producao
    
    fazenda_maxima = max(total_por_fazenda_ano.items(), key=lambda item: item[1].get(ano_escolhido, 0))[0]
    fazenda_minima = min(total_por_fazenda_ano.items(), key=lambda item: item[1].get(ano_escolhido, 0))[0]

    return f' -Fazenda com Produção Máxima: {fazenda_maxima}\n -Fazenda com Procução Mínima: {fazenda_minima}'

print('\n\n')
print('Produção das Fazendas por Ano:')
while True:
    print('\n')
    print('>>Observação: Caso deseje sair basta digitar 0 no lugar do ano<<\n\n')
    ano_escolhido = int(input('Qual o Ano que deseja saber a produção: '))
    if ano_escolhido == 0:
        break
    elif ano_escolhido != 2021 and ano_escolhido != 2022 and ano_escolhido != 2023:
        print('\n\n')
        print('====='*10)
        print('\n\n')
        print('Não possuimos informações deste ano no nosso Banco de Dados ou Ano Inválido.\n\nTente Novamente!')
        print('\n\n')
        print('====='*10)
        print('\n')
    else:
        print('\n\n')
        print('====='*10)
        print('\n\n')
        print(f'Produção das Fazendas no ano de {ano_escolhido}:\n')
        print(fazenda_producao_maximo_minimo(ano_escolhido))
        print('\n\n')
        print('====='*10)

print('\n\n')
print('====='*10)
print('\n\n')
print('FIM...')
print('\n\n')
print('====='*10)