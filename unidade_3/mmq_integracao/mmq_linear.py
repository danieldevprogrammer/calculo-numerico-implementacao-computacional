# Implementação do MMQ Linear
import numpy as np
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def mmqLinear(x, y):
    # Verifica se x e y são arrays numpy
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError('x e y devem ser arrays numpy')

    # Verifica se x e y têm o mesmo comprimento
    if len(x) != len(y):
        raise ValueError('x e y devem ter o mesmo comprimento')

    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Calcula xy e x^2 para cada elemento para usarmos no cálculo e na criação da tabela:
    xy = x * y
    x_quad = x ** 2  # x_quad significa x ao quadrado

    # Calcula as somas para cada coluna da tabela e esses valores vão servir como parâmetros para calcular os valores de a e de b
    n = len(x)
    soma_x = np.sum(x)
    soma_y = np.sum(y)
    soma_xy = np.sum(xy)
    soma_x_quad = np.sum(x_quad)

    # Cálculo de a que é o coeficiente angular:
    a = (n * soma_xy - soma_x * soma_y) / \
        (n * soma_x_quad - soma_x ** 2)

    # Cálculo de b que é o coeficiente linear:
    b = (soma_xy * soma_x - soma_y * soma_x_quad) / \
        (soma_x ** 2 - n * soma_x_quad)

    # y é igual a g(x):
    y_linear = a * x + b
    soma_y_linear = np.sum(y_linear)

    # Média de y:
    y_media = (soma_y/n)
    # sqreg é a Soma dos Quadrados da Regressão:
    sqreg = ((y_media - y_linear)**2)
    # sqtot é a Soma dos Quadrados Totais:
    sqtot = ((y_media - y)**2)
    soma_sqreg = np.sum(sqreg)
    soma_sqtot = np.sum(sqtot)

    # Cálculo do R²
    R2 = soma_sqreg / soma_sqtot

    # Criação da tabela
    table = PrettyTable()
    table.field_names = ['x', 'y', 'xy', 'x^2', 'g(x)', 'SQReg', 'SQTot']
    for i in range(n):
        table.add_row(['{:.4f}'.format(x[i]), '{:.4f}'.format(y[i]), '{:.4f}'.format(xy[i]), '{:.4f}'.format(
            x_quad[i]), '{:.4f}'.format(y_linear[i]), '{:.4f}'.format(sqreg[i]), '{:.4f}'.format(sqtot[i])])
    # Adiciona um rodapé com os valores das somas a tabela
    table.add_row(['----', '----', '----', '----', '----', '----', '----'])
    table.add_row(['{:.4f}'.format(soma_x), '{:.4f}'.format(soma_y), '{:.4f}'.format(soma_xy), '{:.4f}'.format(
        soma_x_quad), '{:.4f}'.format(soma_y_linear), '{:.4f}'.format(soma_sqreg), '{:.4f}'.format(soma_sqtot)])
    # Fim da criação e imprimeção da tabela
    print(table)

    print(f'Coeficiente angular (a): {a:.4f}')
    print(f'Coeficiente linear (b): {b:.4f}')
    print(f'y = {a:.4f} * x + {b:.4f}')
    print(f'A média de y = {y_media:.4f}')
    print(f'R² = {R2:.4f}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    # Plotar o gráfico do ajuste linear
    plt.scatter(x, y, label='Dados Originais')
    plt.plot(x, y_linear, color='red', label='Ajuste Linear')
    plt.title('MMQ - Linear')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return
