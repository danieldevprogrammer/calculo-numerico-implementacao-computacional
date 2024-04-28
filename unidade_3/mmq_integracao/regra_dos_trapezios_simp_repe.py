# Implementação do método da Regra dos Trapézios para integração numérica.
import numpy as np
import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt


def regraTrapezios(f, a, b, x, y, h, valor_real_integral, nomeDaFuncao):

    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()
    # Definindo função para o método do trapézio simples

    def trapezio_simples(f, a, b):
        return (b - a) * (f(a) + f(b)) / 2

    # Resultado do método de Trapézio simples
    regra_trapezio_simples = trapezio_simples(f, a, b)
    print(
        f'O valor pelo método dos trapézios simples é: RTs = {regra_trapezio_simples:.4f}')

    # Definindo função para o método do trapézio repetido

    def trapezio_repetido(y, h):
        regra_trapezio_rep = (h / 2) * (2 * np.sum(y) - (y[0] + y[-1]))
        return regra_trapezio_rep

    # Resultado do método de Trapézio repedito
    regra_trapezio_rep = trapezio_repetido(y, h)
    print(
        f'O valor pelo método dos trapézios repetidos é: RTr = {regra_trapezio_rep:.4f}\n')

    # Calculo do erro absoluto(Eabs_rts) e o erro relativo(Erel_rts) de RTs
    Eabs_rts = abs(regra_trapezio_simples - valor_real_integral)
    Erel_rts = abs((regra_trapezio_simples - valor_real_integral) /
                   valor_real_integral)

    # Calculo do erro absoluto(Eabs_rtr) e o erro relativo(Erel_rtr) de RTr
    Eabs_str = abs(regra_trapezio_rep - valor_real_integral)
    Erel_str = abs((regra_trapezio_rep - valor_real_integral) /
                   valor_real_integral)

    # Criando a tabela com os erros das integrações:
    table = PrettyTable()
    table.field_names = ["Método", "Erro Absoluto", "Erro Relativo"]
    table.add_row(["RTs", "{:.4f}".format(
        Eabs_rts), "{:.2%}".format(Erel_rts)])
    table.add_row(["RTr", "{:.4f}".format(
        Eabs_str), "{:.2%}".format(Erel_str)])
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
