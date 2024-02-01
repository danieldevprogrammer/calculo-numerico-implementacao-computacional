from prettytable import PrettyTable
import time
import numpy as np

# Variável para determinar qual será a função.
nomeDaFuncao = '5x^3 + x^2 - e^(1-2x) + cos(x) + 20'
print(f'Método da Secante da função f(x) = {nomeDaFuncao}')

# Valor inicial do intervalo:
a = -5
# Valor final do intervalo:
b = 5
# A precisão da raiz.
precisao = 0.0000000001

print(f'I=[{a},{b}], Precisão={precisao}.')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x)
    return 5 * x**3 + x**2 - np.exp(1-2*x) + np.cos(x) + 20


# Palpite inicial para descobrir o valor de x:
x0 = a
x1 = b


def secante(f, x0, x1, precisao, maxInteracoes):
    # Realiza as primeiras iterações manualmente
    fx0 = f(x0)
    fx1 = f(x1)

    for i in range(maxInteracoes):
        # Verifica se a diferença entre as aproximações é menor que a tolerância
        if abs(x1 - x0) < precisao:
            return x1

        # Calcula a nova aproximação usando a fórmula da secante
        xAproximacao = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

        # Atualiza os valores para a próxima iteração
        x0, x1 = x1, xAproximacao
        fx0, fx1 = fx1, f(xAproximacao)
        # Verifica se atingiu o número máximo de iterações e retorna o resultado
        if i == maxInteracoes - 1:
            return None  # Se o número máximo de iterações for atingido, retornamos None
    return x1


# Gerando a tabela
tabelaResultados = PrettyTable()
tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
# tabelaResultados.float_format = ".10"  # Limitando para 10 casas decimais

raizConvergente = None
numIteracoes = 0
maxIteracoes = 500

while numIteracoes < maxIteracoes:
    x = secante(f, x0, x1, precisao, maxIteracoes)

    numIteracoes += 1
    tabelaResultados.add_row([numIteracoes, x, f(x), abs(f(x))])

    # Verifica se o f(x) é menor que precisão.
    if abs(f(x)) < precisao:
        raizConvergente = x
        break

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')
