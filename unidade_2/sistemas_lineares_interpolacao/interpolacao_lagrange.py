# Implementação da Interpolação do Método de Lagrange
import time

# Interpola o valor de yInterpolado para um determinado xi usando o método de interpolação de Lagrange.


def interLagrange(x, y, xi):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Função para calcular o polinômio de Lagrange
    def polinomioLagrange(x, y, xi):
        n = len(x)
        # yInterpolado é o valor interpolado de y para o xi fornecido.
        yInterpolado = 0
        for i in range(n):
            L = 1
            for j in range(n):
                if j != i:
                    L *= (xi - x[j]) / (x[i] - x[j])
            yInterpolado += y[i] * L
        return yInterpolado

    # Mostra os valores interpolados para cada x fornecido
    print("\nInterpolação para os valores em x:")
    for valorDeX in x:
        yInterpolado = polinomioLagrange(x, y, valorDeX)
        print(
            f'O valor interpolado de y para x={valorDeX} é y={yInterpolado}')

    # Mostra os valores interpolados para xi fornecido
    print("\nInterpolação para o valor de xi:")
    yInterpolado = polinomioLagrange(x, y, xi)
    print(f'O valor interpolado de y para x={xi} é y={yInterpolado:.4f}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return
