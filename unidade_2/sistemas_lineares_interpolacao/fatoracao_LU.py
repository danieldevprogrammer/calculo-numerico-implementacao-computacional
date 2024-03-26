# Implementação do método de Fatoração LU
import numpy as np
from prettytable import PrettyTable
import time


def fatoracaoLU(A, b):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Inicializa a diagonal de L com 1
    for i in range(n):
        L[i, i] = 1.0

    for k in range(n):
        # Calculo da linha k da matriz U
        for j in range(k, n):
            U[k, j] = A[k, j] - sum(L[k, p] * U[p, j] for p in range(k))

        # Calculo da coluna k da matriz L
        for i in range(k+1, n):
            L[i, k] = (A[i, k] - sum(L[i, p] * U[p, k]
                       for p in range(k))) / U[k, k]

    # Resolvendo o sistema de equações:
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))

    # Resolvendo x por retrosubstituição:
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i+1, n))) / U[i, i]

    # Calcula o vetor de resíduos
    residuo = np.dot(A, x) - b

    # Calcula o resíduo por distância relativa
    residuoRelativo = np.linalg.norm(residuo) / np.linalg.norm(b)
    # Definindo das casas decimais da matriz para no máximo 4 casas:
    np.set_printoptions(precision=4)

    # Mostrar as Matrizes L e U para conferência e os resultados dos valores de x:
    print('\nMatriz L:')
    print(L)
    print('\nMatriz U:')
    print(U)

    print('\nValores Tabelados de x e y:')

    # Tabelar os valores de x e y:
    table = PrettyTable()
    table.field_names = ['xi', 'x', '|', 'yi', 'y']
    for i in range(len(x)):
        table.add_row([f'x{i+1}', f'{x[i]:.5f}',
                      '|', f'y{i+1}', f'{y[i]:.5f}'])
    print(table)

    # Número de iterações é igual ao número de elementos ou 1 (para matrizes vazias)
    NumeroIteracoes = max(n, 1)
    print(f'Número de iterações: {NumeroIteracoes}')

    # Exibir o resíduo por distância relativa
    print(f'Resíduo: {residuoRelativo}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return x, y, L, U, residuoRelativo
