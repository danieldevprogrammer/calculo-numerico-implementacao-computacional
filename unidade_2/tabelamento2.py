import numpy as np
import os
from prettytable import PrettyTable
from sistemas_lineares_interpolacao import interpolacao_sistema_linear, interpolacao_lagrange, interpolacao_newton
from colorama import Fore, Style, init

# Inicializando colorama (chamada uma vez no início do seu script)
init()


# Variável para determinar qual vai ser o tabelamento
nome = Fore.GREEN + 'Tabelamento 2' + Style.RESET_ALL
print(nome)

# Entrada dos valores de x e y:
x = np.array([-1, 0, 3])
y = np.array([-2, 1, 4])
xi = 0.5


def tabelaDoTabelmaneto():  # Imprime a tabela com o tabelamento
    print("Valores Tabelados:")
    table = PrettyTable()
    table.field_names = ["xi", "x", "yi", "y"]

    for i in range(len(x)):
        table.add_row([f"x{i+1}", f"{x[i]}", f"y{i+1}", f"{y[i]}"])
    print(table)

    return


tabelaDoTabelmaneto()


# Menu para chamar os métodos
def main():
    while True:
        print(Fore.GREEN + f'\n{nome}' + Style.RESET_ALL)
        print('Escolha uma opção:')
        print(Fore.GREEN + '1.Interpolação via Sistema Linear' + Style.RESET_ALL)
        print(Fore.GREEN + '2.Método de Lagrande' + Style.RESET_ALL)
        print(Fore.GREEN + '3.Método de Newton' + Style.RESET_ALL)
        print(Fore.YELLOW + '0.Voltar' + Style.RESET_ALL)

        escolha = int(
            input('Digite o número da opção desejada ou 0 para voltar: '))

        if escolha == 1:
            os.system('clear')
            print(
                Fore.CYAN + f'\n1.Interpolação via Sistema Linear - {nome}' + Style.RESET_ALL)
            tabelaDoTabelmaneto()
            interpolacao_sistema_linear.interSistemaLinear(x, y)

        elif escolha == 2:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n2.Método de Lagrande - {nome}' + Style.RESET_ALL)
            tabelaDoTabelmaneto()
            interpolacao_lagrange.interLagrange(x, y, xi)

        elif escolha == 3:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n3.Método de Newton - {nome}' + Style.RESET_ALL)
            tabelaDoTabelmaneto()
            interpolacao_newton.interNewton(x, y, xi)

        elif escolha == 0:
            os.system('clear')
            print(Fore.YELLOW + '\nVoltou ao menu anterior!' + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED + '\nOpção inválida. Por favor, escolha novamente.' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
