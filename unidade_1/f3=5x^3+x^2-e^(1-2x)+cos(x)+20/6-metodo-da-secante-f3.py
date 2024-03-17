# Implementação do Método da Secante:
from prettytable import PrettyTable
import numpy as np
import time
import os
from datetime import datetime

# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x)=5x^3+x^2-e^(1-2x)+cos(x)+20'

diretorio_resultados = "unidade-1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20/resultados-em-txt-e-grafico-f3"

# Criar a estrutura de diretório, se não existir
if not os.path.exists(diretorio_resultados):
    os.makedirs(diretorio_resultados)

# Obter a data e hora atual
data_e_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Definir o caminho completo para os arquivos
caminho_tabela = os.path.join(
    diretorio_resultados, f'6-metodo-da-secante-{nomeDaFuncao}-{data_e_hora_atual}.txt')

print(f'\nMétodo da Secante da função {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = -5
# Valor final do intervalo:
b = 5
# A precisão da raíz.
precisao = 1e-10
# Número máximo de iterações
maxIteracoes = 500

print(f'I=[{a},{b}], Precisão={precisao} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):  # Definindo a função f(x)
    return 5 * x**3 + x**2 - np.exp(1-2*x) + np.cos(x) + 20


# Palpite inicial para descobrir o valor de x:
x0 = a
x1 = b


# Função que encontrará a raiz por meio do metodo da Secante:
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

        # Calcula a nova aproximação usando a fórmula da secante
        xAproximacao = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

        # Atualiza os valores para a próxima iteração
        x0, x1 = x1, xAproximacao
        fx0, fx1 = fx1, f(xAproximacao)

        # Verifica se a diferença entre as aproximações é menor que a tolerância
        if abs(x1 - x0) < precisao:
            return x1, tabelaResultados  # Retorna a raiz e a tabela de resultados

    return None, tabelaResultados  # Retorna None se não convergir


raizConvergente, tabelaResultados = secante(f, x0, x1, precisao, maxIteracoes)

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Salvando a tabela em um arquivo txt com informações adicionais
with open(caminho_tabela, 'w') as file:
    file.write(f'Método da Secante da função {nomeDaFuncao}\n')
    file.write(
        f'I=[{a},{b}], Precisão={precisao} e Número Máximo de Iterações={maxIteracoes}.\n')
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
