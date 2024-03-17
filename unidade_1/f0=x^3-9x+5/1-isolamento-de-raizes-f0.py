from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import time
import os
from datetime import datetime

# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x)=x^3-9x+5'

diretorio_resultados = "unidade-1/f0=x^3-9x+5/resultados-em-txt-e-grafico-f0"

# Criar a estrutura de diretório, se não existir
if not os.path.exists(diretorio_resultados):
    os.makedirs(diretorio_resultados)

# Obter a data e hora atual
data_e_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Definir o caminho completo para os arquivos
caminho_tabela = os.path.join(
    diretorio_resultados, f'1-isolamento-de-raizes-{nomeDaFuncao}-{data_e_hora_atual}.txt')
caminho_grafico = os.path.join(
    diretorio_resultados, f'1-isolamento-de-raizes-{nomeDaFuncao}-grafico-{data_e_hora_atual}.jpg')

print(f'\nIsolamento das raízes da função {nomeDaFuncao}')
# a = Início do intervalo.
a = -4
# b = Final do intervalo.
b = 5
# h = Amplitude do intervalo.
amplitude = 1
print(f'I=[{a},{b}] e Amplitude={amplitude}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


def f(x):
    return x**3 - 9 * x + 5


# Função para isolamento das Raízes:
def isolamentoRaizes(a, b, amplitude, f):
    # Valores de x:
    valoresDeX = np.arange(a, b + amplitude, amplitude)

    # Valores de y:
    valoresDeY = [f(x) for x in valoresDeX]

    # Criando a tabela com PrettyTable
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['x', 'f(x)']

    for x, y in zip(valoresDeX, valoresDeY):
        tabelaResultados.add_row([x, y])

    # Imprimir a tabela no console
    print(tabelaResultados)

    # Retornar a tabela para ser usada fora da função
    return tabelaResultados, valoresDeX, valoresDeY


# Chamar a função e salvar a tabela em um arquivo txt com informações adicionais
tabelaResultados, valoresDeX, valoresDeY = isolamentoRaizes(a, b, amplitude, f)

# Salvando a tabela em um arquivo txt com informações adicionais
with open(caminho_tabela, 'w') as file:
    file.write(f'Isolamento das raízes da função {nomeDaFuncao}\n')
    file.write(
        f'I=[{a},{b}] e Amplitude={amplitude}.\n')
    file.write(str(tabelaResultados))


# Medindo o tempo de fim do cálculo
fimTempo = time.time()
# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo
print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

# Adicionar o tempo de execução ao arquivo de texto
with open(caminho_tabela, 'a') as file:
    file.write(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.\n')

# Criação do gráfico:
x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y)
plt.scatter(valoresDeX, valoresDeY, color='red',
            label='Pontos para isolamento de raízes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Função {nomeDaFuncao} no I=[{a}, {b}] e h={amplitude}')
plt.legend()
plt.grid(True)

# Salvar o gráfico em um arquivo jpg
plt.savefig(caminho_grafico)

# Exibir o gráfico na tela
plt.show()
