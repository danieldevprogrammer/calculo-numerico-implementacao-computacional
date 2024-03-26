from colorama import Fore, Style, init
import os
import numpy as np
from sistemas_lineares_interpolacao import eliminacao_de_gauss, fatoracao_LU, gauss_jacobi, gauss_seidel
# Inicializando colorama (chamada uma vez no início do seu script)
init()

# Variável para determinar qual vai ser o nome da Matriz
nome = Fore.GREEN + 'Matriz A - 8x8' + Style.RESET_ALL
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

# Vetor independente b
b = np.matrix([3, 2, 5, -7, 10, 2, -7, 9], dtype=float).T


def imprimindoMatrizes():  # Imprime as matrizes na tela
    print('Matriz A:')
    print(A)

    print('Valores de b:')
    print(b)

    return


imprimindoMatrizes()


# Menu para chamar os métodos
def main():
    while True:
        print(Fore.GREEN + f'\n{nome}' + Style.RESET_ALL)
        print('Escolha uma opção:')
        print(Fore.GREEN + '1.Método de Eliminação de Gauss' + Style.RESET_ALL)
        print(Fore.GREEN + '2.Método de Fatoração LU' + Style.RESET_ALL)
        print(Fore.GREEN + '3.Método de Gauss-Jacobi' + Style.RESET_ALL)
        print(Fore.GREEN + '4.Método de Gauss-Seidel' + Style.RESET_ALL)
        print(Fore.YELLOW + '0.Voltar' + Style.RESET_ALL)

        escolha = int(
            input('Digite o número da opção desejada ou 0 para voltar: '))

        if escolha == 1:
            os.system('clear')
            print(
                Fore.CYAN + f'\n1.Método de Eliminação de Gauss - {nome}' + Style.RESET_ALL)
            imprimindoMatrizes()
            eliminacao_de_gauss.eliminacaoDeGauss(A, b)

        elif escolha == 2:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n2.Método de Fatoração LU - {nome}' + Style.RESET_ALL)
            imprimindoMatrizes()
            fatoracao_LU.fatoracaoLU(A, b)

        elif escolha == 3:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n3.Método de Gauss-Jacobi - {nome}' + Style.RESET_ALL)
            imprimindoMatrizes()
            gauss_jacobi.gaussJacobi(A, b)

        elif escolha == 4:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n4.Método de Gauss-Seidel - {nome}' + Style.RESET_ALL)
            imprimindoMatrizes()
            gauss_seidel.gaussSeidel(A, b)

        elif escolha == 0:
            os.system('clear')
            print(Fore.YELLOW + '\nVoltou ao menu anterior!' + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED + '\nOpção inválida. Por favor, escolha novamente.' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
