# Implementação do MMQ Potência
import numpy as np
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def mmqPotencia(x, y):
    # Verifica se x e y são arrays numpy
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError('x e y devem ser arrays numpy')

    # Verifica se x e y têm o mesmo comprimento
    if len(x) != len(y):
        raise ValueError('x e y devem ter o mesmo comprimento')

    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Calculo do log de x e log de y  para cada elemento para usarmos no cálculo e na criação da tabela:
    ln_x = np.log(x)
    ln_y = np.log(y)

    # Calcula as somas para cada coluna da tabela e esses valores vão servir como parâmetros para calcular os valores de a e de b
    n = len(x)
    soma_ln_x = np.sum(ln_x)
    soma_ln_y = np.sum(ln_y)
    soma_lnx_lny = np.sum(ln_x * ln_y)
    soma_ln_x_quad = np.sum(ln_x**2)  # ln_x_quad significa ln_x ao quadrado

    # Cálculo de a que é o coeficiente angular:
    a = (n * soma_lnx_lny - soma_ln_x * soma_ln_y) / \
        (n * soma_ln_x_quad - soma_ln_x**2)

    # Cálculo de b que é o coeficiente linear:
    b = np.exp((soma_ln_x * soma_lnx_lny - soma_ln_y * soma_ln_x_quad) /
               (soma_ln_x**2 - n * soma_ln_x_quad))

    # y é igual a g(x)
    y_pot = b * np.exp(a * ln_x)
    soma_y_pot = np.sum(y_pot)

    # Média de y
    y_media = (soma_ln_y/n)
    # sqreg é a Soma dos Quadrados da Regressão:
    sqreg = ((y_media - y_pot)**2)
    # sqtot é a Soma dos Quadrados Totais:
    sqtot = ((y_media - y)**2)
    soma_sqreg = np.sum(sqreg)
    soma_sqtot = np.sum(sqtot)

    # Cálculo do R²
    R2 = soma_sqreg / soma_sqtot

    # Criação da tabela
    table = PrettyTable()
    table.field_names = ['ln(x)', 'ln(y)', 'ln(y)ln(x)',
                         'ln(x)^2', 'g(x)', 'SQReg', 'SQTot']
    for i in range(n):
        table.add_row(['{:.4f}'.format(ln_x[i]), '{:.4f}'.format(ln_y[i]), '{:.4f}'.format(
            ln_x[i] * ln_y[i]), '{:.4f}'.format(ln_x[i]**2), '{:.4f}'.format(y_pot[i]), '{:.4f}'.format(sqreg[i]), '{:.4f}'.format(sqtot[i])])
    # Adiciona um rodapé com os valores das somas a tabela
    table.add_row(['----', '----', '----', '----', '----', '----', '----'])
    table.add_row(['{:.4f}'.format(soma_ln_x), '{:.4f}'.format(soma_ln_y), '{:.4f}'.format(soma_lnx_lny), '{:.4f}'.format(
        soma_ln_x_quad), '{:.4f}'.format(soma_y_pot), '{:.4f}'.format(soma_sqreg), '{:.4f}'.format(soma_sqtot)])
    # Fim da criação e imprimeção da tabela
    print(table)

    print(f'Coeficiente angular (a): {a:.4f}')
    print(f'Coeficiente linear (b): {b:.4f}')
    print(f'y = {b:.4f} * x^{a:.4f}')
    print(f'A média de y = {y_media:.4f}')
    print(f'R² = {R2:.4f}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    # Plotar o gráfico do ajuste linear
    plt.scatter(x, y, label='Dados Originais')
    plt.plot(x, y_pot, color='red', label='Ajuste Potência')
    plt.title('MMQ - Potência')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return
