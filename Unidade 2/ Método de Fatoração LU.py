#Implementação do Método de Fatoração de LU
import numpy as np
import time

start_time = time.time()
print('Método de Fatoração LU')

#Inserir a dimensão da matriz:
n = int(input('Digite o número de linhas e colunas da matriz: '))

#Inserir os dados da matriz A: 
print('Digite a matriz A, separando os elementos por espaço:')
A = []
for i in range(n):
    row = input()
    row = [float(x) for x in row.split()]
    A.append(row)
matrix = np.array(A)

#Inserir os valores de b:
print('Digite o valor de b, separado por espaço:')
b = np.fromstring(input().replace('\n', ' '), dtype=float, sep=' ')

def fatoracao_lu(matrix):

    n = len(matrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    #Inicializa a diagonal de L com 1s, ou seja vai atribuir o valor 1 às posições (i, i) da matriz L, onde i é a linha e a coluna correspondentes:
    for i in range(n):
        L[i, i] = 1.0

    #Calculo ds matrizes L e U:
    for k in range(n):
        U[k, k:] = matrix[k, k:] - L[k, :k] @ U[:k, k:]
        L[(k+1):, k] = (matrix[(k+1):, k] - L[(k+1):, :k] @ U[:k, k]) / U[k, k]

    return L, U


#Execução da fatoração LU:
L, U = fatoracao_lu(matrix)

#Resolvendo o sistema de equações:
y = np.zeros(n)
for i in range(n):
    y[i] = b[i] - L[i, :i] @ y[:i]

x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (y[i] - U[i, i+1:] @ x[i+1:]) / U[i, i]

#Definindo das casas decimais da matriz para no máximo 4 casa:
np.set_printoptions(precision=4)

#Mostrar as Matrizes L e U para conferência e os resultados dos valores de x:
print('Matriz L:')
print(L)
print('Matriz U:')
print(U)
print('Valores de y:')
for i in range(n):
    if np.isclose(y[i], 0, atol=1e-15):
        y[i] = 0
    print(f'y{i+1} = {y[i]: .4f}')

print('Valores de x:')
for i in range(n):
    if np.isclose(x[i], 0, atol=1e-15):
        x[i] = 0
    print(f'x{i+1} = {x[i]: .4f}')

    end_time = time.time()
# Calculando o tempo de execução
runtime = end_time - start_time
print(f"Tempo de execução do Método de Fatoração LU foi: {runtime:.6f} segundos")