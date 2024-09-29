# Função que encontrará a raiz por meio do metodo do Ponto Fixo:
from prettytable import PrettyTable
import time


def pontoFixo(a, b, x, f, fi, precisao, maxIteracoes):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

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
            break

        tabelaResultados.add_row(
            [numIteracoes, a, b, "{:.5f}".format(x), f(x), abs(f(x))])

        if abs(x - xAnterior) < precisao:
            raizConvergente = x
            break  # Sai do loop quando a precisão é atingida
    else:
        print('\nO número máximo de iterações foi atingido.')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()

    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    # Imprimindo a tabela de resultados
    print(tabelaResultados)

    # Verificando se a raiz convergente foi encontrada:
    if raizConvergente is not None:
        print(f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}')
    else:
        print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

    return tabelaResultados, raizConvergente
