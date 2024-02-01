# Implementação de Função para o Isolamento de Raízes:
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import time

# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'x^3 - 9x + 5'
print(f'Isolamento das raízes da função f(x) = {nomeDaFuncao}')
# a = Início do intervalo.
a = int(-4)
# b = Final do intervalo.
b = int(5)
# h = Amplitude do intervalo.
amplitude = float(1)
print(f'I=[{a},{b}] e Amplitude={amplitude}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()

# Função para isolamento das Raízes:
def f(x):  
    return x**3 - 9 * x + 5


# Valores de x:
valoresDeX = np.arange(a, b + amplitude, amplitude)

# Valores de y:
valoresDeY = [f(x) for x in valoresDeX]

# Criando a tabela com PrettyTable
tabela = PrettyTable()
tabela.field_names = ['x', 'f(x)']

for x, y in zip(valoresDeX, valoresDeY):
    tabela.add_row([x, y])

print(tabela)

# Medindo o tempo de fim do cálculo
fimTempo = time.time()
# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo
print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

# Criação do gráfico:
x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y)
plt.scatter(valoresDeX, valoresDeY, color='red', label='Pontos para isolamento de raízes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Função f(x) = {nomeDaFuncao} no I=[{a}, {b}] e h={amplitude}')
plt.legend()
plt.grid(True)
# Exibir o gráfico na tela
plt.show()

