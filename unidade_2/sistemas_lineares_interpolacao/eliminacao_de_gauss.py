# Implementação do método de Eliminação de Gauss
import numpy as np
from prettytable import PrettyTable
import time


def eliminacaoDeGauss(A, b):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Determina a ordem da matriz contando o número de linhas
    n = A.shape[0]

    Ab = np.column_stack((A, b))

    # Contador para o número de iterações
    NumeroIteracoes = 0

    # Eliminação de Gauss
    for i in range(n):
        pivo = Ab[i, i]

        if pivo == 0:
            print('Erro: divisão por zero!')
            exit()

        for j in range(i+1, n):
            multiplicador = Ab[j, i] / pivo
            Ab[j, i:] = Ab[j, i:] - multiplicador * Ab[i, i:]

        # Incrementa o contador de iterações
        NumeroIteracoes += 1

    # Fase de Retrosubstituição
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]

    # Calcula o vetor de resíduos
    residuo = np.dot(A, x) - b

    # Calcula o resíduo por distância relativa
    residuoRelativo = np.linalg.norm(residuo) / np.linalg.norm(b)

    # Exibição da solução
    print('A solução do sistema é: ')
    table = PrettyTable()
    table.field_names = ['xi', 'x']
    for i in range(len(x)):
        table.add_row([f'x{i+1}', f'{x[i]:.5f}'])
    print(table)

    # Exibir o número de iterações
    print(f'Número de iterações: {NumeroIteracoes}')

    # Exibir o resíduo por distância relativa
    print(f'Resíduo: {residuoRelativo}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return x
