#Implementação do Método de Interpolação via Sistema Linear
import numpy as np
import time

print('Interpolação via Sistema Linear do Tabelamento 1.')

start_time = time.time()

#Entrada dos valores de x e y:
x = np.array([-1, 1, 2])
y = np.array([-4, 2, 5])
print(f'Valores de x: {x}')
print(f'Valores de y: {y}')

#Gerando a matriz de sistema linear:
n = len(x)
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i,j] = x[i]**j
print('A Matriz é:')
print(A)

#Resolvendo o sistema linear:
a = np.linalg.solve(A, y)
print(f"Os coeficientes do polinômio são: {a}")


#Função interpoladora:
def f(x):
    result = 0
    for i in range(n):
        result += a[i]*x**i
    return result
print(f'A função é: {f(x)}')
print(f'O valor da função interpoladora para o x escolhido é: {f(0)}')

end_time = time.time()
# Calculando o tempo de execução
runtime = end_time - start_time
print(f"Tempo de execução da interpolação via sistema linear foi: {runtime:.6f} segundos")