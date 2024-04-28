import numpy as np
import os
from prettytable import PrettyTable
from mmq_integracao import mmq_linear, mmq_logaritimico, mmq_exponencial, mmq_potencia, mmq_polinomial_grau_2
from colorama import Fore, Style, init


# Inicializando colorama (chamada uma vez no início do seu script)
init()

# Variável para determinar qual vai ser o tabelamento
nome = Fore.GREEN + 'Tabelamento 1' + Style.RESET_ALL
print(nome)

# Entrada dos valores de x e y:
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 6, 7, 9])


def tabelaDoTabelamento():  # Imprime a tabela com o tabelamento
    print("Valores Tabelados:")
    table = PrettyTable()
    table.field_names = ["xi", "x", "yi", "y"]

    for i in range(len(x)):
        table.add_row([f"x{i+1}", f"{x[i]}", f"y{i+1}", f"{y[i]}"])
    print(table)

    return


tabelaDoTabelamento()

# Menu para chamar os métodos


def main():
    while True:
        print(Fore.GREEN + f'\n{nome}' + Style.RESET_ALL)
        print('Escolha uma opção:')
        print(Fore.GREEN + '1. MMQ Linear' + Style.RESET_ALL)
        print(Fore.GREEN + '2. MMQ Logaritimico' + Style.RESET_ALL)
        print(Fore.GREEN + '3. MMQ Exponencial' + Style.RESET_ALL)
        print(Fore.GREEN + '4. MMQ Potência' + Style.RESET_ALL)
        print(Fore.GREEN + '5. MMQ Polinomial de Grau 2' + Style.RESET_ALL)
        print(Fore.YELLOW + '0. Voltar' + Style.RESET_ALL)

        escolha = int(
            input('Digite o número da opção desejada ou 0 para voltar: '))

        if escolha == 1:
            os.system('clear')
            print(
                Fore.CYAN + f'\n1.MMQ Linear - {nome}' + Style.RESET_ALL)
            tabelaDoTabelamento()
            mmq_linear.mmqLinear(x, y)

        elif escolha == 2:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n2.MMQ Logaritimico - {nome}' + Style.RESET_ALL)
            tabelaDoTabelamento()
            mmq_logaritimico.mmqLogaritimico(x, y)

        elif escolha == 3:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n3.MMQ Exponencial - {nome}' + Style.RESET_ALL)
            tabelaDoTabelamento()
            mmq_exponencial.mmqExponencial(x, y)

        elif escolha == 4:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n4.MMQ Potência - {nome}' + Style.RESET_ALL)
            tabelaDoTabelamento()
            mmq_potencia.mmqPotencia(x, y)

        elif escolha == 5:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n5.MMQ Polinomial de Grau 2 - {nome}' + Style.RESET_ALL)
            tabelaDoTabelamento()
            mmq_polinomial_grau_2.mmqPolinomialGrau2(x, y)

        elif escolha == 0:
            os.system('clear')
            print(Fore.YELLOW + '\nVoltou ao menu anterior!' + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED + '\nOpção inválida. Por favor, escolha novamente.' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
