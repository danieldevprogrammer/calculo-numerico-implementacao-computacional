# Implementação da Interpolação do Método de Newton
import numpy as np
import time


# Interpola o valor de yi para um determinado xi usando o método de interpolação de Newton.

def interNewton(x, y, xi):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    def diferencasDivididas(x, y):  # Calcula as diferenças divididas.

        n = len(x)
        # tabelaDifDiv é tabela de diferenças divididas.
        # Inicializa a tabela de diferenças divididas com zeros
        tabelaDifDiv = np.zeros((n, n))

        # Preenche a primeira coluna com os valores de y
        tabelaDifDiv[:, 0] = y

        # Calcula as diferenças divididas
        for j in range(1, n):
            for i in range(n - j):
                tabelaDifDiv[i, j] = (tabelaDifDiv[i + 1, j - 1] -
                                      tabelaDifDiv[i, j - 1]) / (x[i + j] - x[i])
        return tabelaDifDiv

    def polinomioNewton(tabelaDifDiv, x, xi):
        n = len(x)
        # yInterpolado: o valor interpolado de y para o xi fornecido.
        yInterpolado = tabelaDifDiv[0, 0]
        # prod é o produto acumulado do fator (x - xi) em cada iteração do loop.
        produto = 1
        for i in range(1, n):
            produto *= (xi - x[i - 1])
            yInterpolado += tabelaDifDiv[0, i] * produto
        return yInterpolado

    tabelaDifDiv = diferencasDivididas(x, y)

    # Mostra os valores interpolados para cada x fornecido
    print("\nInterpolação para os valores em x:")
    for valorDeX in x:
        yInterpolado = polinomioNewton(tabelaDifDiv, x, valorDeX)
        print(
            f'O valor interpolado de y para x={valorDeX} é y={yInterpolado}')

    # Mostra os valores interpolados para xi fornecido
    print("\nInterpolação para o valor de xi:")
    yInterpolado = polinomioNewton(tabelaDifDiv, x, xi)
    print(f'O valor interpolado de y para x={xi} é y={yInterpolado:.4f}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return
