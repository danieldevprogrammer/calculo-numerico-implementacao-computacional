# Implementação do Método de Newton:
from prettytable import PrettyTable
import time

# Variável para determinar qual será a função.
nomeDaFuncao = '2x^4 + 4x^3 + 3x^2 - 10x - 15'
print(f'Método de Newton da função f(x) = {nomeDaFuncao}')

# Valor inicial do intervalo:
a = 0
# Valor final do intervalo:
b = 3
# A precisão da raiz.
precisao = 0.0000000001
# Número máximo de interações
maxIteracoes = 500
# Palpite inicial para descobrir o valor de x:
x0 = (a + b) / 2

print(f'I=[{a},{b}], Precisão={precisao}, X0={x0} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


# Definindo a função f(x)
def f(x):
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15


# Definindo a função da derivada numérica de f(x)
def derivadaNumericaDeF(x, h=0.0001):
    # h=0.0001, é um valor muito próximo de zero, para que não ocarra um erro de indeterminação na função e assim pode calcular a derivada númerica
    return (f(x + h) - f(x)) / h


# Definindo a função que encontrará a raiz por meio do metodo de Newton:
def Newton(x, precisao, maxIteracoes):
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".15"  # Limitando para 15 casas decimais

    raizConvergente = None

    # Inicializa o valor de x com o palpite inicial x0
    x = x0

    # Loop para as iterações
    for numIteracoes in range(maxIteracoes):
        valorDef = f(x)

        # Adiciona a iteração atual à tabela
        tabelaResultados.add_row(
            [numIteracoes, x, valorDef, abs(valorDef)])

        # Condição para quando a raiz convergir parar o loop
        if abs(valorDef) < precisao:
            raizConvergente = "{:.15f}".format(x)
            break

        # Calculando a derivada de numérica de f(x)
        derivadaNumerica = derivadaNumericaDeF(x)
        # Verificando se a derivade numérica é igual a 0, para evitar erros.
        if derivadaNumerica == 0:
            print("Derivada é zero. Escolha outro palpite inicial.")
            return None

        x = x - (valorDef / derivadaNumerica)

        if abs(valorDef) < precisao:
            raizConvergente = "{:.15f}".format(x)
            break

    else:
        print("\nO número máximo de iterações foi atingido.")

    return tabelaResultados, raizConvergente


# Chamando a função do Método de Newton
tabelaResultados, raizConvergente = Newton(x0, precisao, maxIteracoes)

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

print(f'\nO tempo de execução foi {tempoTotal:.6f} segundos.')
