# Implementação do Método da Secante:
from prettytable import PrettyTable
import time

# Variável para determinar qual será a função.
nomeDaFuncao = '2x^4 + 4x^3 + 3x^2 - 10x - 15'
print(f'\nMétodo da Secante da função f(x) = {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 3
# A precisão da raíz.
precisao = 1e-10
# Número máximo de interações
maxIteracoes = 500


print(f'I=[{a},{b}], Precisão={precisao} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x)
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15


# Palpite inicial para descobrir o valor de x:
x0 = a
x1 = b


# Definindo a função que encontrará a raiz por meio do metodo da Secante:
def secante(f, x0, x1, precisao, maxInteracoes):
    # Realiza as primeiras iterações manualmente
    fx0 = f(x0)
    fx1 = f(x1)

    # Inicializando a tabela de resultados
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".15"  # Limitando para 15 casas decimais

    for numIteracoes in range(maxInteracoes):
        # Adiciona a linha na tabela para a iteração atual
        tabelaResultados.add_row(
            [numIteracoes, f'{x1:.15f}', f'{f(x1):.15f}', f'{abs(f(x1)):.15f}'])

        # Verifica se a diferença entre as aproximações é menor que a tolerância
        if abs(x1 - x0) < precisao:
            return x1, tabelaResultados  # Retorna a raiz e a tabela de resultados

        # Calcula a nova aproximação usando a fórmula da secante
        xAproximacao = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

        # Atualiza os valores para a próxima iteração
        x0, x1 = x1, xAproximacao
        fx0, fx1 = fx1, f(xAproximacao)

    return None, tabelaResultados  # Retorna None se não convergir


raizConvergente, tabelaResultados = secante(f, x0, x1, precisao, maxIteracoes)

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Verificando se a raiz convergente foi encontrada:
if raizConvergente is not None:
    print(f'\nRaiz convergente encontrada foi: {raizConvergente:.15f}')
else:
    print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')
