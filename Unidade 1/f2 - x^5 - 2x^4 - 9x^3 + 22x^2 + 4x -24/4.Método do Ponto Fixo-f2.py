from prettytable import PrettyTable
import time

# variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x) = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x -24'
print(f'Método do Ponto Fixo da função f(x) = {nomeDaFuncao}')

# Valor ínicial do intervalo:
# a = 0
a = 0
# Valor final do intervalo:
# b = 3
b = 3
# A precisão da raíz.
precisao = 0.0000000001
# Número máximo de interações
maxIteracoes = 500

x = (a + b) / 2  # Inicialização de x

print(f'I=[{a},{b}], Precisão={precisao} e X0={x}.')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x):
    return x**5 - 2*x**4 - 9*x**3 + 22*x**2 + 4*x - 24


def fi(x):  # Definindo a função de iteração fi
    return (x**5 - 2 * x**4 - 9 * x**3 + 24) / (-22)

# Definindo a função que encontrará a raiz por meio do metodo do Ponto Fixo:


def pontoFixo(a, b, x, precisao, maxIteracoes):
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'a', 'b', 'x', 'f(x)', '|f(x)|']
    # tabelaResultados.float_format = ".10"  # Limitando para 10 casas decimais

    for numIteracoes in range(maxIteracoes):
        xAnterior = x
        x = fi(x)
        tabelaResultados.add_row([numIteracoes, a, b, "{:.10f}".format(x), f(x), abs(f(x))])
        if abs(x - xAnterior) < precisao:
            break  # Sai do loop quando a precisão é atingida
    else:
        print("\nO número máximo de iterações foi atingido.")

    return tabelaResultados, numIteracoes


# Chamando a função do Método do Ponto Fixo
tabelaResultados, numIteracoes = pontoFixo(a, b, x, precisao, maxIteracoes)

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')
