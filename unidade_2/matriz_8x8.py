import numpy as np
from sistemas_lineares_interpolacao import eliminacao_de_gauss, fatoracao_LU

# Variável para determinar qual vai ser o nome da Matriz.
nome = 'Matriz A-8x8'
print(nome)

# Matriz de coeficientes A
A = np.matrix([[15, 2, 3, 1, 0.7, 0.5, 3, 1],
               [1, 11, -3, 4, 0.8, 0.6, 0.9, 2],
               [-6, 4, -17, 2, 1, 3, 2, 4],
               [3, -8, 3, 30, 8, 5, 7, 6],
               [1, 4, 2, 3, 55, 17, 12, 5],
               [1.5, 2, 0.7, 0.8, 3, 17, 1, 0.9],
               [0.5, 1, 1.8, 6, 2, 5, 27, 1],
               [8, 3, 2, 2, 0.3, 1, 5, 35]], dtype=float)
print('Matriz A:')
print(A)


# Vetor independente b
b = np.matrix([3, 2, 5, -7, 10, 2, -7, 9], dtype=float).T
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
