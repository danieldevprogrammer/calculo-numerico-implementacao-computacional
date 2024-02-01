from prettytable import PrettyTable
import time
import numpy as np

# Variável para determinar qual será a função.
nomeDaFuncao = 'sen(x)x + 4'
print(f'Método de Newton da função f(x) = {nomeDaFuncao}')

# Valor inicial do intervalo:
a = 1
# Valor final do intervalo:
b = 5
# A precisão da raiz.
precisao = 0.0000000001
# Palpite inicial para descobrir o valor de x:
x0 = (a + b) / 2

print(f'I=[{a},{b}], Precisão={precisao} e Palpite inicial X0={x0}.')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x)
    return np.sin(x) * x + 4


h = 0.0001  # É um valor muito próximo de zero, para que não ocarra um erro de indeterminação na função e assim pode calcular a derivada númerica
# Calculo da derivada númerica da função f
derivadaNumericaDef = (f(x0 + h) - f(x0)) / h


def Newton(x0, precisao, maxIteracoes):
    x = x0  # Inicializa o valor de x com o palpite inicial x0
    for i in range(maxIteracoes):
        valorDef = f(x)

        if abs(valorDef) < precisao:
            break

        if derivadaNumericaDef == 0:
            print("Derivada é zero. Escolha outro palpite inicial.")
            return None

        x = x - valorDef / derivadaNumericaDef
    return x


# Gerando a tabela
tabelaResultados = PrettyTable()
tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
tabelaResultados.float_format = ".10"  # Limitando para 10 casas decimais

raizConvergente = None
numIteracoes = 0
maxIteracoes = 500

x = x0  # Atribui o valor do palpite inicial a x antes do loop
for numIteracoes in range(maxIteracoes):
    valorDef = f(x)
    tabelaResultados.add_row([numIteracoes, x, valorDef, abs(valorDef)])

    if abs(valorDef) < precisao:
        raizConvergente = "{:.10f}".format(x)
        break

    # Atualiza o valor de x para a próxima iteração
    x = Newton(x, precisao, maxIteracoes)

    # numIteracoes += 1  # Incrementa o contador de iterações

# Adicionando a última iteração à tabela
tabelaResultados.add_row([numIteracoes + 1, x, f(x), abs(f(x))])

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(
    f'\nO tempo de execução foi {tempoTotal:.6f} segundos.')
