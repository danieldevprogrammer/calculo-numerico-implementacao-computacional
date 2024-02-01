from prettytable import PrettyTable
import time
import numpy as np

# variável para determinar qual vai ser a função.
nomeDaFuncao = '5x^3 + x^2 - e^(1-2x) + cos(x) + 20'
print(f'Método da Falsa Posição da função f(x) = {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = -5
# Valor final do intervalo:
b = 5
# A precisão da raíz.
precisao = float(0.0000000001)
# Número máximo de interações
maxIteracoes = 500

print(f'I=[{a},{b}], Precisão={precisao}.')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x):
    return 5 * x**3 + x**2 - np.exp(1-2*x) + np.cos(x) + 20


# Definindo a função que encontrará a raiz por meio do metodo da Falsa Posição:
def falsaPosicao(a, b, precisao, maxIteracoes):
    if f(a) * f(b) >= 0:
        raise ValueError("Os valores de 'a' e 'b' devem ser tais que f(a) * f(b) < 0.")

    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração','a', 'b', 'x', 'f(a)', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".10"  # Limitando para 10 casas decimais

    # Indicador de que as interações máximas foram atingindas
    maxIteracoesAtingida = False

    for i in range(maxIteracoes):
        x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        tabelaResultados.add_row(
            [i, a, b, "{:.10f}".format(x), f(a), f(x), abs(f(x))])

        if abs(f(x)) < precisao:
            break  # Sai do loop quando a precisão é atingida

        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

    else:
        maxIteracoesAtingida = True

    if maxIteracoesAtingida:
        print('\nO número de iterações foi atingido.')

    return tabelaResultados


# Chamando a função da Falsa Posição
tabelaResultados = falsaPosicao(a, b, precisao, maxIteracoes)

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')
