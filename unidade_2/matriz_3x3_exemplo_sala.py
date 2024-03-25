import os
import numpy as np
from sistemas_lineares_interpolacao import eliminacao_de_gauss, fatoracao_LU


# Variável para determinar qual vai ser o nome da Matriz.
nome = 'Matriz A - 3x3 - Exemplo da Sala'
print(nome)

# Matriz de coeficientes A
A = np.matrix([[13, 2, 2, 3], [0, 12, 1, 0], [0, 4, 11, 1], [1, 2, 2, 10]])
print('Matriz A:')
print(A)


# Vetor independente b
b = np.matrix([5, 4, 2, 1]).T
print('Valores de b:')
print(b)


# Menu para chamar os métodos
def main():
    while True:
        print(f'\n{nome}, escolha uma opção:')
        print('1.Método de Eliminação de Gauss')
        print('2.Método de Fatoração LU')
        print('3.Método de Gauss-Jacobi')
        print('4.Método de Gauss-Seidel')
        print('0.Voltar')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            print(f'1.Método de Eliminação de Gauss - {nome}')
            eliminacao_de_gauss.eliminacaoDeGauss(A, b)
        elif escolha == '2':
            print(f'2.Método de Fatoração LU - {nome}')
            fatoracao_LU.fatoracaoLU(A, b)
        # elif escolha == '3':
            # print(f'3.Método de Gauss-Jacobi - {nome}')
        #     #gauss_jacobi.gaussJacobi(A, b)
        # elif escolha == '4':
            # print(f'4.Método de Gauss-Seidel - {nome}')
        #     #gauss_seidel.gaussSeidel(A, b)
        elif escolha == '0':
            print('Voltando ao menu anterior!')
            break
        else:
            print('Opção inválida. Por favor, escolha novamente.')


if __name__ == '__main__':
    main()
