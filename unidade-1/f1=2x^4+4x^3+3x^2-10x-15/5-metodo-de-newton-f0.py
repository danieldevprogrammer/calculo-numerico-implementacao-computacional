# Implementação do Método de Newton:
from prettytable import PrettyTable
import time
import os
from datetime import datetime

# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x)=x^3 - 9x + 5'

diretorio_resultados = "unidade-1/f0=x^3-9x+5/resultados-em-txt-e-grafico-f0"

# Criar a estrutura de diretório, se não existir
if not os.path.exists(diretorio_resultados):
    os.makedirs(diretorio_resultados)

# Obter a data e hora atual
data_e_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Definir o caminho completo para os arquivos
caminho_tabela = os.path.join(
    diretorio_resultados, f'5-metodo-de-newton-{nomeDaFuncao}-{data_e_hora_atual}.txt')

print(f'\nMétodo de Newton da função {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 1
# A precisão da raíz.
precisao = 1e-2
# Número máximo de interações
maxIteracoes = 500
# Palpite inicial para descobrir o valor de x:
x0 = (a + b) / 2

print(f'I=[{a},{b}], Precisão={precisao}, X0={x0} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


# Definindo a função f(x)
def f(x):
    return x**3 - 9 * x + 5


# Definindo a função da derivada numérica de f(x)
def derivadaNumericaDeF(x, h=0.0001):
    # h=0.0001, é um valor muito próximo de zero, para que não ocarra um erro de indeterminação na função e assim pode calcular a derivada númerica
    return (f(x + h) - f(x)) / h


# Definindo a função que encontrará a raiz por meio do metodo de Newton:
def Newton(x, precisao, maxIteracoes):
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

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
            raizConvergente = x
            break

        # Calculando a derivada de numérica de f(x)
        derivadaNumerica = derivadaNumericaDeF(x)
        # Verificando se a derivade numérica é igual a 0, para evitar erros.
        if derivadaNumerica == 0:
            print("Derivada é zero. Escolha outro palpite inicial.")
            return None

        x = x - (valorDef / derivadaNumerica)

        if abs(valorDef) < precisao:
            raizConvergente = "{:.5f}".format(x)
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

# Salvando a tabela em um arquivo txt com informações adicionais
with open(caminho_tabela, 'w') as file:
    file.write(f'Método de Newton da função {nomeDaFuncao}\n')
    file.write(
        f'I=[{a},{b}], Precisão={precisao}, X0={x0} e Número Máximo de Iterações={maxIteracoes}.\n')
    file.write(str(tabelaResultados))

# Verificando se a raiz convergente foi encontrada:
if raizConvergente is not None:
    print(f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}')
else:
    print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

# Adicionar se a raiz convergente foi encontrada ao arquivo de texto
with open(caminho_tabela, 'a') as file:
    if raizConvergente is not None:
        file.write(
            f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}\n')
    else:
        file.write(
            '\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.\n')

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo
print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

# Adicionar o tempo de execução ao arquivo de texto
with open(caminho_tabela, 'a') as file:
    file.write(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.\n')
