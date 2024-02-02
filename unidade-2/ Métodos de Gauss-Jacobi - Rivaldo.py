import numpy as np


def gauss_jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        print(f"Iteração {k+1}: x = {x}")
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x_old[j]
            x[i] = (b[i] - s) / A[i][i]
        print(f"  -> x' = {x}")
        if np.linalg.norm(x - x_old) < tol:
            return x
    print(
        f"Atenção: O método não convergiu para a tolerância desejada em {max_iter} iterações.")
    return x


# Entrada dos dados
num_linhas = int(input("Digite o número de linhas da matriz A: "))
num_colunas = int(input("Digite o número de colunas da matriz A: "))
A = np.zeros((num_linhas, num_colunas))
b = np.zeros(num_linhas)
for i in range(num_linhas):
    linha = input(
        f"Digite os coeficientes da linha {i+1} da matriz A separados por espaço: ")
    A[i] = np.array([float(x) for x in linha.split()])
    b[i] = float(input(f"Digite o termo independente da equação {i+1}: "))

# Mostra a matriz A digitada pelo usuário
print("A = ")
for i in range(num_linhas):
    print("[ ", end="")
    for j in range(num_colunas):
        print(f"{A[i][j]:^7.2f}", end="")
    print(" ]")
# Vetor inicial definido como número de linhas da matriz
x0 = np.zeros(num_linhas)
tol = float(input("Digite a tolerância desejada: "))
max_iter = int(input("Digite o número máximo de iterações permitidas: "))
# Resolução do sistema
x = gauss_jacobi(A, b, x0, tol, max_iter)
# Mostrando a resposta
print(f"A solução do sistema é x = {x}")
