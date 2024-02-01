# Implementação do Método da Secante:
from prettytable import PrettyTable
import time

# Variável para determinar qual será a função.
nomeDaFuncao = 'x^3 - 9x + 5'
print(f'Método da Secante da função f(x) = {nomeDaFuncao}')

# Valor inicial do intervalo:
a = 0
# Valor final do intervalo:
b = 1
# A precisão da raiz.
precisao = 0.01
# Número máximo de interações
maxIteracoes = 500

print(f'I=[{a},{b}], Precisão={precisao} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x)
    return x**3 - 9 * x + 5


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
            return x1, i + 1  # Retorna a raiz e o número de iterações

        # Calcula a nova aproximação usando a fórmula da secante
        xAproximacao = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

        # Atualiza os valores para a próxima iteração
        x0, x1 = x1, xAproximacao
        fx0, fx1 = fx1, f(xAproximacao)

    return None, maxInteracoes  # Retorna None se não convergir


# Gerando a tabela
tabelaResultados = PrettyTable()
tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

raizConvergente = None
numIteracoes = 0

while numIteracoes < maxIteracoes:
    raizConvergente, _ = secante(f, x0, x1, precisao, maxIteracoes)

    if raizConvergente is not None:
        tabelaResultados.add_row(
            [numIteracoes, f'{raizConvergente:.5f}', f'{f(raizConvergente):.5f}', f'{abs(f(raizConvergente)):.5f}'])

    numIteracoes += 1

    # Verifica se o f(x) é menor que precisão.
    if abs(f(raizConvergente)) < precisao:
        break

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Verificando se a raiz convergente foi encontrada:
if raizConvergente is not None:
    print(f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}')
else:
    print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')


# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(
    f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')
