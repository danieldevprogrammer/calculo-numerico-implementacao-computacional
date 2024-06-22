from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import time


# Função para isolamento das Raízes:
def isolamentoRaizes(a, b, amplitude, f, nomeDaFuncao):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

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

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

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

    # Exibir o gráfico na tela
    plt.show()

    # Retornar a tabela para ser usada fora da função
    return tabelaResultados, valoresDeX, valoresDeY
