# Implementação do Método da Falsa Posição:
from prettytable import PrettyTable
import time

# variável para determinar qual vai ser a função.
nomeDaFuncao = '2x^4 + 4x^3 + 3x^2 - 10x - 15'
print(f'Método da Falsa Posição da função f(x) = {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = int(0)
# Valor final do intervalo:
b = int(3)
# A precisão da raíz.
precisao = float(0.0000000001)
# Número máximo de interações
maxIteracoes = 500

print(f'I=[{a},{b}], Precisão={precisao} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x):
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15


# Definindo a função que encontrará a raiz por meio do metodo da Falsa Posição:
def falsaPosicao(a, b, precisao, maxIteracoes):
    if f(a) * f(b) >= 0:
        raise ValueError(
            "Os valores de 'a' e 'b' devem ser tais que f(a) * f(b) < 0.")

    # Gerando a tabela
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = [
        'Iteração', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".15"  # Limitando para 15 casas decimais

    # Inicializando raizConvergente como None
    raizConvergente = None

    for i in range(maxIteracoes):
        x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        tabelaResultados.add_row(
            [i, a, b, "{:.5f}".format(x), f(a), f(b), f(x), abs(f(x))])

        if abs(f(x)) < precisao:
            raizConvergente = x
            break  # Sai do loop quando a precisão é atingida
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

    return tabelaResultados, raizConvergente


# Chamando a função da Falsa Posição
tabelaResultados, raizConvergente = falsaPosicao(a, b, precisao, maxIteracoes)

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