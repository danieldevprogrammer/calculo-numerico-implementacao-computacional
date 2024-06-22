# Função que encontrará a raiz por meio do metodo do Ponto Fixo:
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import time


def pontoFixo(a, b, x, precisao, maxIteracoes):
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = [
        'Iteração', 'a', 'b', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

    raizConvergente = None

    # Acrescentando na tabela uma linha a mais para aparecer a iteração 0
    tabelaResultados.add_row([0, a, b, "{:.5f}".format(x), f(x), abs(f(x))])

    for numIteracoes in range(1, maxIteracoes + 1):
        xAnterior = x
        x = fi(x)

        # Verificar se a função está saindo de controle
        if abs(x) > 1e10:
            print(
                'A função está saindo de controle, para evitar um erro de overflow as iterações foram paradas!\n')

            # Adicionando a mensagem ao arquivo de texto
            with open(caminho_tabela, 'w') as file:
                file.write(
                    'A função está saindo de controle, para evitar um erro de overflow as iterações foram paradas!\nO erro aconteceu provavelmente por causa da má definição da função Fi.\n')
            break

        tabelaResultados.add_row(
            [numIteracoes, a, b, "{:.5f}".format(x), f(x), abs(f(x))])

        if abs(x - xAnterior) < precisao:
            raizConvergente = x
            break  # Sai do loop quando a precisão é atingida
    else:
        print('\nO número máximo de iterações foi atingido.')

    return tabelaResultados, raizConvergente
