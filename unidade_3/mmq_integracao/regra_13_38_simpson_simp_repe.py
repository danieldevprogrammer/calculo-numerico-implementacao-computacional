# Implementação do método da Regra de Simpson para integração numérica.
import numpy as np
import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt


def regrasSimpson(x, y, h, valor_real_integral, nomeDaFuncao):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Definindo função para o método de 1/3 de Simpson
    def simpson_1_3(h, y):
        n = len(y) - 1
        soma = y[0] + y[n]
        soma += 4 * np.sum(y[1:n:2])
        soma += 2 * np.sum(y[2:n-1:2])
        return (h / 3) * soma

    # Resultado da regra de 1/3 de Simpson
    regra_simpson_1_3 = simpson_1_3(h, y)
    print(
        f'O valor pelo método de 1/3 de Simpson é: S13 = {regra_simpson_1_3:.4f}')

    # Definindo função para o método de 1/8 de Simpson

    def simpson_1_8(h, y):
        n = len(y) - 1
        soma = y[0] + y[n]
        soma += 3 * np.sum(y[1:n:3])
        soma += 3 * np.sum(y[2:n-1:3])
        soma += 2 * np.sum(y[3:n-2:3])
        return (3*h / 8) * soma

    # Resultado da regra de 1/8 de Simpson
    regra_simpson_1_8 = simpson_1_8(h, y)
    print(
        f'O valor pelo método de 1/8 de Simpson é: S18 = {regra_simpson_1_8:.4f}')
    print()

    # Calculo do erro absoluto(Eabs_s13) e o erro relativo(Erel_s13) de S13
    Eabs_s13 = abs(regra_simpson_1_3 - valor_real_integral)
    Erel_s13 = abs((regra_simpson_1_3 - valor_real_integral) /
                   valor_real_integral)

    # Calculo do erro absoluto(Eabs_s18) e o erro relativo(Erel_s18) de S18
    Eabs_s18 = abs(regra_simpson_1_8 - valor_real_integral)
    Erel_s18 = abs((regra_simpson_1_8 - valor_real_integral) /
                   valor_real_integral)

    # Criando a tabela com os erros das integrações:
    table = PrettyTable()
    table.field_names = ["Método", "Erro Absoluto", "Erro Relativo"]
    table.add_row(["S13", "{:.4f}".format(
        Eabs_s13), "{:.2%}".format(Erel_s13)])
    table.add_row(["S18", "{:.4f}".format(
        Eabs_s18), "{:.2%}".format(Erel_s18)])
    table.title = 'Tabela de Erros'
    print(table)

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    # Plotando a função e a área aproximada
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=nomeDaFuncao, color='blue')
    plt.fill_between(x, y, color="gray", alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return
