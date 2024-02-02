# Implementação do Método da Bissecção:
from prettytable import PrettyTable
import time

# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'x^3 - 9x + 5'
print(f'Método da Bissecção da função f(x) = {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 1
# A precisão da raíz.
precisao = 1e-2
# Equação inicial para descobrir o valor de x:
x = (a + b) / 2
# Número máximo de interações
maxIteracoes = 500

print(f'I=[{a},{b}], Precisão={precisao}, X0={x} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


# Definindo a função que encontrará a raiz por meio do metodo da bissecção:
def f(x):
    return x**3 - 9 * x + 5


# Gerando a tabela
tabelaResultados = PrettyTable()
tabelaResultados.field_names = ['Iteração',
                                'a', 'b', 'x', 'f(a)', 'f(x)', '|f(x)|']
# Limitando para 5 casas decimais que vão aparecer na tabela
tabelaResultados.float_format = ".5"

raizConvergente = None
numIteracoes = 0


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
        raizConvergente = "{:.5f}".format(x)


# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Verificando se a raiz convergente foi encontrada:
if raizConvergente is not None:
    print(f'\nRaiz convergente encontrada foi: {raizConvergente}')
else:
    print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')


# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')
