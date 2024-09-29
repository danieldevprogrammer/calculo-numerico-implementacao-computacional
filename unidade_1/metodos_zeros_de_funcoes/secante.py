from prettytable import PrettyTable
import time


def secante(f, a, b, precisao, maxIteracoes):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Palpite inicial para descobrir o valor de x:
    x0 = a
    x1 = b

    # Realiza as primeiras iterações manualmente
    fx0 = f(x0)
    fx1 = f(x1)

    # Inicializando a tabela de resultados
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

    for numIteracoes in range(maxIteracoes):
        # Adiciona a linha na tabela para a iteração atual
        tabelaResultados.add_row(
            [numIteracoes, f'{x1:.5f}', f'{fx1:.5f}', f'{abs(fx1):.5f}']
        )

        # Calcula a nova aproximação usando a fórmula da secante
        xAproximacao = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

        # Atualiza os valores para a próxima iteração
        x0, x1 = x1, xAproximacao
        fx0, fx1 = fx1, f(xAproximacao)

        # Verifica se a diferença entre as aproximações é menor que a tolerância
        if abs(x1 - x0) < precisao:
            # Imprimindo a tabela de resultados
            print(tabelaResultados)
            print(f'\nRaiz convergente encontrada foi: {x1:.5f}')
            break
    else:
        # Caso não converta dentro do número máximo de iterações
        print(tabelaResultados)
        print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()

    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return x1, tabelaResultados  # Retorna a raiz e a tabela de resultados
