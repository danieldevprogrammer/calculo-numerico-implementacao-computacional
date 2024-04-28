# Implementação do MMQ Polinomial de Grau 2
import numpy as np
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def mmqPolinomialGrau2(x, y):
    # Verifica se x e y são arrays numpy
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError('x e y devem ser arrays numpy')

    # Verifica se x e y têm o mesmo comprimento
    if len(x) != len(y):
        raise ValueError('x e y devem ter o mesmo comprimento')

    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Calcula x^2 e x^3 para cada elemento
    x_quad = x ** 2
    x_cubo = x ** 3

    # Calcula as somas para cada coluna da tabela
    n = len(x)
    soma_x = np.sum(x)
    soma_y = np.sum(y)
    soma_x_quad = np.sum(x_quad)
    soma_x_cubo = np.sum(x_cubo)
    soma_xy = np.sum(x * y)
    soma_x_quad_y = np.sum(x_quad * y)

    # Calcula os coeficientes do ajuste quadrático
    matriz_coeficientes = np.array([[n, soma_x, soma_x_quad],
                                    [soma_x, soma_x_quad, soma_x_cubo],
                                    [soma_x_quad, soma_x_cubo, soma_x_quad ** 2]])
    vetor_independente = np.array([soma_y, soma_xy, soma_x_quad_y])

    # Resolve o sistema de equações lineares
    def eliminacaoDeGauss(A, b):
        # Determina a ordem da matriz contando o número de linhas
        n = A.shape[0]

        Ab = np.column_stack((A, b))

        # Contador para o número de iterações
        NumeroIteracoes = 0

        # Eliminação de Gauss
        for i in range(n):
            # Pivô é o elemento da diagonal principal
            pivo = Ab[i, i]
            # Se o pivô for zero, então vai ocorrer uma divisão por zero, encerrando a execução
            if pivo == 0:
                print('Erro: divisão por zero!')
                exit()

            # Zera os elementos abaixo do pivô na coluna i
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
        print('\nA solução do sistema por Eliminação de Gauss é: ')
        table = PrettyTable()
        table.field_names = ['xi', 'x']
        for i in range(len(x)):
            table.add_row([f'x{i+1}', f'{x[i]:.5f}'])
        print(table)

        # Exibir o número de iterações
        print(f'Número de iterações: {NumeroIteracoes}')

        # Exibir o resíduo por distância relativa
        print(f'Resíduo: {residuoRelativo}\n')

        return x

    coeficientes = eliminacaoDeGauss(matriz_coeficientes, vetor_independente)

    # Coeficientes do ajuste quadrático
    a, b, c = coeficientes

    # Calcula os valores ajustados de y
    y_quadratico = a * x_quad + b * x + c

    # Calcula o R²
    sqreg = np.sum((y_quadratico - y) ** 2)
    sqtot = np.sum((y - np.mean(y)) ** 2)
    R2 = 1 - sqreg / sqtot

    # Criação da tabela
    table = PrettyTable()
    table.field_names = ['x', 'y', 'x^2', 'x^3', 'g(x)', 'SQReg', 'SQTot']
    for i in range(n):
        table.add_row(['{:.4f}'.format(x[i]), '{:.4f}'.format(y[i]), '{:.4f}'.format(x_quad[i]),
                       '{:.4f}'.format(x_cubo[i]), '{:.4f}'.format(
                           y_quadratico[i]),
                       '{:.4f}'.format((y_quadratico[i] - y[i]) ** 2),
                       '{:.4f}'.format((y[i] - np.mean(y)) ** 2)])
    table.add_row(['----', '----', '----', '----', '----', '----', '----'])
    table.add_row(['{:.4f}'.format(soma_x), '{:.4f}'.format(soma_y), '{:.4f}'.format(soma_x_quad),
                   '{:.4f}'.format(soma_x_cubo), '{:.4f}'.format(
                       a * soma_x_quad + b * soma_x + c),
                   '{:.4f}'.format(sqreg), '{:.4f}'.format(sqtot)])
    print(table)

    print(f'\nCoeficientes do ajuste quadrático:')
    print(f'a: {a:.4f}, b: {b:.4f}, c: {c:.4f}')
    print(f'Equação do ajuste: y = {a:.4f} * x^2 + {b:.4f} * x + {c:.4f}')
    print(f'R² = {R2:.4f}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    # Plotar o gráfico do ajuste quadrático
    plt.scatter(x, y, label='Dados Originais')
    plt.plot(x, y_quadratico, color='red', label='Ajuste Quadrático')
    plt.title('MMQ - Quadrático')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return
