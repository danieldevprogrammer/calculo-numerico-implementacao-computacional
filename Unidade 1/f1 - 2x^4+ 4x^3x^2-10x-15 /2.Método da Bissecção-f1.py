from prettytable import PrettyTable
import time

# variável para determinar qual vai ser a função.
nomeDaFuncao = '2x^4 + 4x^3 + 3x^2 - 10x - 15'
print(f'Método da Bissecção da função f(x) = {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = int(0)
# Valor final do intervalo:
b = int(3)
# A precisão da raíz.
precisao = float(0.0000000001)
# Equação inicial para descobrir o valor de x:
x = (a + b) / 2

print(f'I=[{a},{b}], Precisão={precisao} e X0={x}.')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


# Definindo a função que encontrará a raiz por meio do metodo da bissecção:


def f(x):
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15


# Gerando a tabela
tabelaResultados = PrettyTable()
tabelaResultados.field_names = ['Iteração', 'a', 'b', 'x', 'f(a)', 'f(x)', '|f(x)|']
tabelaResultados.float_format = ".10"  # Limitando para 10 casas decimais

raizConvergente = None
numIteracoes = 0
maxIteracoes = 500

# Laço de repetição para que enquanto o valor absoluto de f(x) for maior do que a precisão a operação se repita:
while abs(f(x)) > precisao and numIteracoes < maxIteracoes:
    # Atualizamos o x usando a fórmula do método da bissecção:
    x = (a + b) / 2
    tabelaResultados.add_row([numIteracoes, a, b, x, f(a), f(x), abs(f(x))])

    # Atualizamos a e b de acordo com o sinal de f(a) e f(x):
    if f(a) * f(x) < 0:
        b = x
    else:
        a = x

    numIteracoes += 1

    if abs(f(x)) < precisao:
        raizConvergente = "{:.10f}".format(x)

# Adicionando a última iteração à tabela, mesmo que a precisão já tenha sido alcançada
tabelaResultados.add_row([numIteracoes, a, b, "{:.10f}".format(x), f(a), f(x), abs(f(x))])

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')
