import scipy.integrate as spi
import numpy as np
import os
from prettytable import PrettyTable
from mmq_integracao import soma_riemman_esq_dir, regra_dos_trapezios_simp_repe, regra_13_38_simpson_simp_repe
from colorama import Fore, Style, init


# Inicializando colorama (chamada uma vez no início do seu script)
init()


# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = np.pi / 4
# Valor dos subintervalos:
n = 6
# h calcula o tamanho de cada subintervalo:
h = (b - a) / n
# Variável para armazenar o nome da função
nomeDaFuncao = 'f(x)=cos(x)'


# Gerando os valores de x baseado no valor de a e de n:
x = [a + i * h for i in range(n+1)]


def f(x):  # Função para calcular os valores de y:
    return np.cos(x)


# Gerando os valores de y pela função f(x):
y = [f(xi) for xi in x]

# Calcular o valor real da integral definida:
integral, error = spi.quad(f, a, b)
# Valor real é o resultado real da integral da função f(x):
valor_real_integral = integral


# Imprime cabeçalho, a tabela e o valor da integral
def cabecalho():
    print(f'{nomeDaFuncao}, I=[{a},{b:.5f}], n={n} e h={h:.5f}.')

    print(
        f'\nValor Real da integral de {nomeDaFuncao} no I=[{a},{b:.5f}] = {valor_real_integral:.5}\n')

    # Criação da tabela com os valores de x e y:
    table = PrettyTable()
    table.field_names = ["x", "|", "y"]
    for i in range(n+1):
        table.add_row(["{:.2f}".format(x[i]), "|", "{:.4f}".format(y[i])])
    print(table)
    print()

    return


cabecalho()


def main():
    while True:
        print(Fore.GREEN + f'\n{nomeDaFuncao}' + Style.RESET_ALL)
        print('Escolha uma opção:')
        print(Fore.GREEN + '1. Soma de Riemman(esquerda e direita)' + Style.RESET_ALL)
        print(Fore.GREEN + '2. Regra dos Trapézio(simpes e repetida)' + Style.RESET_ALL)
        print(Fore.GREEN + '3. Regras de 1/3 e 3/8 de Simpson' + Style.RESET_ALL)
        print(Fore.YELLOW + '0. Voltar' + Style.RESET_ALL)

        escolha = int(
            input('Digite o número da opção desejada ou 0 para voltar: '))

        if escolha == 1:
            os.system('clear')
            print(
                Fore.CYAN + f'\n1.Soma de Riemman(esquerda e direita) - {nomeDaFuncao}' + Style.RESET_ALL)
            cabecalho()
            soma_riemman_esq_dir.somaRiemman(
                x, y, h, valor_real_integral, nomeDaFuncao)

        elif escolha == 2:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n2.Regra dos Trapézio(simpes e repetida) - {nomeDaFuncao}' + Style.RESET_ALL)
            cabecalho()
            regra_dos_trapezios_simp_repe.regraTrapezios(
                f, a, b, x, y, h, valor_real_integral, nomeDaFuncao)

        elif escolha == 3:
            os.system('clear')
            print(Fore.CYAN +
                  f'\n3.Regras de 1/3 e 3/8 de Simpson - {nomeDaFuncao}' + Style.RESET_ALL)
            cabecalho()
            regra_13_38_simpson_simp_repe.regrasSimpson(
                x, y, h, valor_real_integral, nomeDaFuncao)

        elif escolha == 0:
            os.system('clear')
            print(Fore.YELLOW + '\nVoltou ao menu anterior!' + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED + '\nOpção inválida. Por favor, escolha novamente.' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
