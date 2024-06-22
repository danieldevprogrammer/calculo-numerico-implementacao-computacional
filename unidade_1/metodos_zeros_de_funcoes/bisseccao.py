# Implementação do Método da Bissecção:
from prettytable import PrettyTable
import time


# Função que encontrará a raiz por meio do método da bissecção:
def bisseccao(a, b, precisao, f, maxIteracoes):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Inicialize x com o valor médio do intervalo inicial [a, b]
    x = (a + b) / 2

    # Gerando a tabela
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração',
                                    'a', 'b', 'x', 'f(a)', 'f(x)', '|f(x)|']
    # Limitando para 5 casas decimais que vão aparecer na tabela
    tabelaResultados.float_format = ".15"

    raizConvergente = None
    numIteracoes = 0

    # Laço de repetição para que enquanto o valor absoluto de f(x) for maior do que a precisão a operação se repita:
    while abs(f(x)) > precisao and numIteracoes < maxIteracoes:
        # Atualizamos o x usando a fórmula do método da bissecção:
        x = (a + b) / 2
        tabelaResultados.add_row(
            [numIteracoes, a, b, x, f(a), f(x), abs(f(x))])

        # Atualizamos a e b de acordo com o sinal de f(a) e f(x):
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        numIteracoes += 1

        if abs(f(x)) < precisao:
            raizConvergente = x

    # Imprimindo a tabela de resultados
    print(tabelaResultados)

    # Verificando se a raiz convergente foi encontrada:
    if raizConvergente is not None:
        print(f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}')
    else:
        print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()

    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return tabelaResultados, raizConvergente
