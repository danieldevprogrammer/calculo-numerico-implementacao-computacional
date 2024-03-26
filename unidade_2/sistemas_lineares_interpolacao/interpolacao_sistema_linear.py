# Implementação do Método de Interpoação Via Sistema Linear
import numpy as np
import time
from sistemas_lineares_interpolacao import eliminacao_de_gauss


# Interpola os pontos (x, y) através do método de interpolação via sistema linear
def interSistemaLinear(x, y):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Construindo a matriz do sistema linear a partir do tabelamento
    n = len(x)
    A = np.zeros((n, n))
    for i in range(n):
        A[:, i] = x ** i
    # Imprimindo a matriz na tela:
    print('A matriz gerada é:')
    print(A)

    # Resolvendo o sistema linear para obter os coeficientes
    # coeficientes é o array contendo os coeficientes do polinômio interpolador
    coeficientes = eliminacao_de_gauss.eliminacaoDeGauss(A, y)

    print(
        f'\nOs valores de x da tabela de resolução da matriz são os coeficientes "a" do polinômio interpolador, que são respectivamente: {[f"{coef:.2f}" for coef in coeficientes]}')

    # Função interpoladora

    def fInterpoladora(x):
        y = 0
        for i in range(n):
            y += coeficientes[i]*x**i
        return y

    # Imprimindo os valores interpolados para cada x fornecido
    for valoresDeX in x:
        print(
            f'O valor interpolado de y para x={valoresDeX} é y={fInterpoladora(valoresDeX):.0f}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return
