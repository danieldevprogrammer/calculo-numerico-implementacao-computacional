import numpy as np
import time
import os
import datetime
from tabulate import tabulate

titulo_arquivo = datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
nome_arquivo = f"R_Lagrange/{titulo_arquivo}.txt"
start_time = time.time()

if not os.path.exists("R_Lagrange"):
    os.makedirs("R_Lagrange")

def lagrange_interpolacao(x_valores, y_valores, x):
    """
    Interpolação polinomial via método de Lagrange

    x_values: lista com os valores de x
    y_values: lista com os valores de y correspondentes a cada x
    x: valor a ser interpolado

    Grupo 1 - Noite - Rivaldo, Daniel, Lucas

    """
    n = len(x_valores)
    y_interp = 0
    p = ''
    L = []
    for i in range(n):
        # Calcula o polinômio Li(x)
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x - x_valores[j]) / (x_valores[i] - x_valores[j])

        # Acumula o termo Li(x)*yi
        y_interp += Li * y_valores[i]

        # Acumula o termo Li(x)*yi no polinômio interpolador
        p += f'{Li:.2f}*y({x_valores[i]:.2f}) + '

        # Armazena o polinômio Li(x)
        L.append(Li)

    # Remove o último sinal de adição e acrescenta a constante
    p = p[:-3] + f'= {y_interp:.2f}'

    return y_interp, p, L

x_valores = [-1, 0, 2]
y_valores = [4, 1, -1]
x = 1

# Cria o arquivo e salva o primeiro print
with open(nome_arquivo, "w", encoding="utf-8") as f:
    f.write(
        f"Grupo 1 - Método de Lagrange \nResultado obtido em: {titulo_arquivo}\n")
    print("Valores Tabelados", file=f)
    print("Valores Tabelados")
    table = []
    for i in range(len(x_valores)):
        table.append([f"x{i}", f"{x_valores[i]:.2f}",
                    "|", f"y{i}", f"{y_valores[i]:.2f}"])

    # Imprime a tabela
    print(tabulate(table, headers=["xi", "x", "|", "yi", "y"]), file=f)
    print(tabulate(table, headers=["xi", "x", "|", "yi", "y"]))

# Salva os demais prints no mesmo arquivo
with open(nome_arquivo, "a", encoding="utf-8") as f:

    y_interp, p, L = lagrange_interpolacao(x_valores, y_valores, x)
    print(f"Valor interpolado correspondente a f({x}) = ", y_interp, file=f)
    print(f"Valor interpolado correspondente a f({x}) = ", y_interp)
    # print("Polinômio interpolador:", p)
    for i, Li in enumerate(L):
        print(f'L{i}(x) = {Li:.2f}', file=f)
        print(f'L{i}(x) = {Li:.2f}')

    end_time = time.time()
    # Calculando o tempo de execução
    runtime = end_time - start_time
    print(
        f"Tempo de execução da interpolação via método de Lagrange foi: {runtime:.6f} segundos", file=f)
    print(
        f"Tempo de execução da interpolação via método de Lagrange foi: {runtime:.6f} segundos")
