# Implementação do Método do Ponto Fixo:
from prettytable import PrettyTable
import time

# variável para determinar qual vai ser a função.
nomeDaFuncao = '2x^4 + 4x^3 + 3x^2 - 10x - 15'
print(f'Método do Ponto Fixo da função f(x) = {nomeDaFuncao}')

# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 3
# A precisão da raíz.
precisao = 0.0000000001
# Número máximo de interações
maxIteracoes = 500

# Inicialização de x0, é uma opção começar com x no meio do intervalo, mas não é obrigatório.
x = (a + b) / 2


print(f'I=[{a},{b}], Precisão={precisao}, X0={x} e Número Máximo de Iterações={maxIteracoes}.\n')


# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x):
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15


def fi(x):  # Definindo a função fi
    return (2 * x**4 + 4 * x**3 + 3 * x**2 - 15) / 10


# Definindo a função que encontrará a raiz por meio do metodo do Ponto Fixo:
def pontoFixo(a, b, x, precisao, maxIteracoes):
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = [
        'Iteração', 'a', 'b', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".15"  # Limitando para 15 casas decimais

    raizConvergente = None

    # Acrescentando na tabela uma linha a mais para aparecer a iteração 0
    tabelaResultados.add_row([0, a, b, "{:.15f}".format(x), f(x), abs(f(x))])

    for numIteracoes in range(1, maxIteracoes + 1):
        xAnterior = x
        x = fi(x)

        # # Verificar se a função está saindo de controle
        if abs(x) > 1e10:
            print(
                'A função está saindo de controle, para evitar um erro de overflow as iterações foram paradas!\n')
            break

        tabelaResultados.add_row(
            [numIteracoes, a, b, "{:.15f}".format(x), f(x), abs(f(x))])

        if abs(x - xAnterior) < precisao:
            raizConvergente = x
            break  # Sai do loop quando a precisão é atingida
    else:
        print('\nO número máximo de iterações foi atingido.')

    return tabelaResultados, raizConvergente


# Chamando a função do Método do Ponto Fixo
tabelaResultados, raizConvergente = pontoFixo(a, b, x, precisao, maxIteracoes)

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
