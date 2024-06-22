import numpy as np
import os
from metodos_zeros_de_funcoes import isolamento_de_raizes, bisseccao, falsa_posicao
from colorama import Fore, Style, init


# Inicializando colorama (chamada uma vez no início do seu script)
init()


# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x)=2x^4+4x^3+3x^2-10x-15'


# Início do intervalo para o isolamento das raízes.
inicioDoInt = -4
# Final do intervalo para o isolamento das raízes.
fimDoInt = 5
# Amplitude do intervalo.
amplitude = 1

# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 1
# A precisão da raíz.
precisao = 1e-2
# Equação inicial para descobrir o valor de x:
x = (a + b) / 2

# Número máximo de iterações
maxIteracoes = 500


def f(x):
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15


def main():
    while True:
        print(Fore.GREEN + f'\n{nomeDaFuncao}' + Style.RESET_ALL)
        print('Escolha uma opção:')
        print(Fore.GREEN + '1. Isolamento de Raizes' + Style.RESET_ALL)
        print(Fore.GREEN + '2. Método da Bissecção' + Style.RESET_ALL)
        print(Fore.GREEN + '3. Método da Falsa Posição' + Style.RESET_ALL)
        print(Fore.GREEN + '4. Método do Ponto Fixo' + Style.RESET_ALL)
        print(Fore.GREEN + '5. Método Newton' + Style.RESET_ALL)
        print(Fore.GREEN + '6. Método da Secante' + Style.RESET_ALL)
        print(Fore.YELLOW + '0. Voltar' + Style.RESET_ALL)

        escolha = int(
            input('Digite o número da opção desejada ou 0 para voltar: '))

        if escolha == 1:
            os.system('clear')
            print(
                Fore.CYAN + f'\n1.Isolamento de Raizes - {nomeDaFuncao}' + Style.RESET_ALL)
            print(
                f'{nomeDaFuncao}, I=[{inicioDoInt},{fimDoInt}], Amplitude={amplitude}.')
            isolamento_de_raizes.isolamentoRaizes(
                inicioDoInt, fimDoInt, amplitude, f, nomeDaFuncao)

        elif escolha == 2:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n2.Método da Bissecção - {nomeDaFuncao}' + Style.RESET_ALL)
            print(
                f'I=[{a},{b}], Precisão={precisao}, X0={x} e Número Máximo de Iterações={maxIteracoes}.\n')
            bisseccao.bisseccao(a, b, precisao, f, maxIteracoes)

        elif escolha == 3:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n3.Método da Falsa Posição - {nomeDaFuncao}' + Style.RESET_ALL)
            falsa_posicao.falsaPosicao(a, b, precisao, maxIteracoes, f)

        elif escolha == 4:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n4.Método do Ponto Fixo - {nomeDaFuncao}' + Style.RESET_ALL)

        elif escolha == 5:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n5.Método Newton - {nomeDaFuncao}' + Style.RESET_ALL)

        elif escolha == 6:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n6.Método da Secante - {nomeDaFuncao}' + Style.RESET_ALL)

        elif escolha == 0:
            os.system('clear')
            print(Fore.YELLOW + '\nVoltou ao menu anterior!' + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED + '\nOpção inválida. Por favor, escolha novamente.' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
