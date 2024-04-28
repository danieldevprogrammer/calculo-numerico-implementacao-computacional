# Implementação do método de Riemman para integração numérica.
import numpy as np
import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt


def somaRiemman(x, y, h, valor_real_integral, nomeDaFuncao):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    def riemman_esq(y, h):  # Definindo função para calcular a soma de Riemman pela esquerda
        soma_riemman_esq = h * np.sum(y[:-1])
        return soma_riemman_esq

    # Resultado da soma de Riemman pelo lado esquerdo
    soma_riemman_esq = riemman_esq(y, h)
    print(
        f'O valor da soma de Riemman pela esquerda é: SRe = {soma_riemman_esq:.4f}')

    def riemman_dir(y, h):  # Definindo função para calcular a soma de Riemman pela direita
        soma_riemman_dir = h * np.sum(y[1:])
        return soma_riemman_dir

    # Resultado da soma de Riemman pelo lado direito
    soma_riemman_dir = riemman_dir(y, h)
    print(
        f'O valor da soma de Riemman pela direita é: SRd = {soma_riemman_dir:.4f}')

    def riemman_med():  # Definindo função para calcular a soma de Riemman médio
        soma_riemman_med = (soma_riemman_esq + soma_riemman_dir) / 2
        return soma_riemman_med

    soma_riemman_med = riemman_med()
    print(f'O valor da soma de Riemman Média é: SRm = {soma_riemman_med:.4f}')
    print()

    # Calculo do erro absoluto(Eabs_srd) e o erro relativo(Erel_srd) de SRe
    Eabs_sre = abs((soma_riemman_esq) - (valor_real_integral))
    Erel_sre = abs(soma_riemman_esq - valor_real_integral) / \
        valor_real_integral

    # Calculo do erro absoluto(Eabs_srd) e o erro relativo(Erel_srd) de SRe
    Eabs_srd = abs((soma_riemman_dir) - (valor_real_integral))
    Erel_srd = abs((soma_riemman_dir - valor_real_integral) /
                   valor_real_integral)

    # Calculo do erro absoluto(Eabs_srm) e o erro relativo(Erel_srm) de SRe
    Eabs_srm = abs((soma_riemman_med) - (valor_real_integral))
    Erel_srm = abs((soma_riemman_med - valor_real_integral) /
                   valor_real_integral)

    # Criando a tabela com os erros da Soma de Riemann:
    table = PrettyTable()
    table.field_names = ["Soma de Riemann", "Erro Absoluto", "Erro Relativo"]
    table.add_row(["SRe", "{:.4f}".format(
        Eabs_sre), "{:.2%}".format(Erel_sre)])
    table.add_row(["SRd", "{:.4f}".format(
        Eabs_srd), "{:.2%}".format(Erel_srd)])
    table.add_row(["SRm", "{:.4f}".format(
        Eabs_srm), "{:.2%}".format(Erel_srm)])
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
