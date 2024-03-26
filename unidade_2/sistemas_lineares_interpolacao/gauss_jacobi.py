# Implementação do método de Gauss-Jacobi
from colorama import Fore, Style, init
import numpy as np
from prettytable import PrettyTable
import time
# Inicializando colorama (chamada uma vez no início do seu script)
init()


def gaussJacobi(A, b, tolerancia=1e-6, maxIteracoes=100):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    print(
        f'\nA tolerância é {tolerancia} e o número máximo de iterações sugerido é de {maxIteracoes}.')

    x0 = np.zeros_like(b)
    n = len(b)
    x = x0.copy()  # Estimativa inicial da solução
    x_novo = np.zeros_like(x)
    numIteracao = 0  # Contador de iterações
    # Erro inicial (inicializado para garantir que o loop comece)
    erro = tolerancia + 1

    # Verifica se a matriz A é diagonalmente dominante pela regra das colunas e das linhas
    def diagonalmenteDominante(A):

        n = A.shape[0]
        for i in range(n):
            soma_linha = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
            soma_coluna = np.sum(np.abs(A[:, i])) - np.abs(A[i, i])
            if np.abs(A[i, i]) <= soma_linha or np.abs(A[i, i]) <= soma_coluna:
                return False
        return True

    if not diagonalmenteDominante(A):
        print('A matriz não é diagonalmente dominante, baseando pelo critério das linhas e colunas, logo a convergência não é garantida.')

    # Loop principal do método de Gauss-Jacobi
    while erro > tolerancia and numIteracao < maxIteracoes:
        x_novo = x.copy()  # Armazena as estimativas atuais em x_novo
        for i in range(n):
            soma = np.dot(A[i, :], x_novo) - A[i, i] * x_novo[i]
            x[i] = (b[i] - soma) / A[i, i]

        # Calcula o erro entre as estimativas atuais e as novas
        erro = np.linalg.norm(x - x_novo, np.inf)
        numIteracao += 1  # Incrementa o contador de iterações

    # Verifica se o método convergiu dentro do número máximo de iterações
    if numIteracao == maxIteracoes:
        print(Fore.RED + '\nO método de Gauss-Jacobi atingiu o numéro máximo de iterações e não me retornou uma solução satisfatória.' + Style.RESET_ALL)

    # Calcula o vetor de resíduos
    residuo = np.dot(A, x) - b

    # Calcula o resíduo por distância relativa
    residuoRelativo = np.linalg.norm(residuo) / np.linalg.norm(b)

    # Abaixo exibe o resultado final que é a tabela, o número de iterações, o erro e o resíduo.
    print('\nA solução do sistema é: ')
    table = PrettyTable()
    table.field_names = ['xi', 'x']
    for i in range(len(x)):
        table.add_row([f'x{i+1}', f'{x[i, 0]:.5f}'])
    print(table)

    print('Número de iterações:', numIteracao)

    print('Erro na solução:', erro)

    # Exibir o resíduo por distância relativa
    print(f'Resíduo: {residuoRelativo}')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()
    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return x, erro, numIteracao
