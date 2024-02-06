# Implementação do Método da Bissecção:
from prettytable import PrettyTable
import time
import os
from datetime import datetime

# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x)=2x^4+4x^3+3x^2-10x-15'

diretorio_resultados = "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/resultados-em-txt-e-grafico-f1"

# Criar a estrutura de diretório, se não existir
if not os.path.exists(diretorio_resultados):
    os.makedirs(diretorio_resultados)

# Obter a data e hora atual
data_e_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Definir o caminho completo para os arquivos
caminho_tabela = os.path.join(
    diretorio_resultados, f'2-metodo-da-bisseccao-{nomeDaFuncao}-{data_e_hora_atual}.txt')

print(f'\nMétodo da Bissecção da função {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 3
# A precisão da raíz.
precisao = 1e-10
# Equação inicial para descobrir o valor de x:
x = (a + b) / 2
# Número máximo de iterações
maxIteracoes = 500

print(f'I=[{a},{b}], Precisão={precisao}, X0={x} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


# Definindo a função que encontrará a raiz por meio do metodo da bissecção:
def f(x):
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15


# Gerando a tabela
tabelaResultados = PrettyTable()
tabelaResultados.field_names = ['Iteração',
                                'a', 'b', 'x', 'f(a)', 'f(x)', '|f(x)|']
# Limitando para 15 casas decimais que vão aparecer na tabela
tabelaResultados.float_format = ".15"

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
        raizConvergente = x


# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Salvando a tabela em um arquivo txt com informações adicionais
with open(caminho_tabela, 'w') as file:
    file.write(f'Método da Bissecção da função {nomeDaFuncao}\n')
    file.write(
        f'I=[{a},{b}], Precisão={precisao}, X0={x} e Número Máximo de Iterações={maxIteracoes}.\n')
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
