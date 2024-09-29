import os
import subprocess
from colorama import Fore, Style, init
import time

# Inicializando colorama (chamada uma vez no início do seu script)
init()

# Definindo o diretório do script
script_directory = os.path.dirname(os.path.realpath(__file__))


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print(Fore.CYAN + Style.BRIGHT +
      'Cálculo Numérico - Implementação Computacional' + Style.RESET_ALL)

print(Style.BRIGHT + 'Aluno: \033[4mDaniel Vitor da Silva' + Style.RESET_ALL)

while True:
    # Escolher a unidade
    print('\nEscolha a unidade desejada de Cálculo Numérico:')
    print(Fore.GREEN + '1.Primeira unidade' + Style.RESET_ALL)
    print(Fore.GREEN + '2.Segunda unidade' + Style.RESET_ALL)
    print(Fore.GREEN + '3.Terceira unidade' + Style.RESET_ALL)
    print(Fore.RED + '0. Sair' + Style.RESET_ALL)

    try:
        unidade = int(input(
            'Digite o número da unidade ou 0 para sair: '))
    except ValueError:
        print(Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)
        continue

    if unidade == 0:
        # Define o tempo de espera em segundos
        tempo_de_espera = 5

        # Mensagem de encerramento
        print(Fore.YELLOW +
              f'O programa será encerrado em {tempo_de_espera} segundos...' + Style.RESET_ALL)
        print(Fore.GREEN + 'Obrigado!' + Style.RESET_ALL)
        # Espera pelo tempo especificado
        time.sleep(tempo_de_espera)

        break  # Sair do loop e encerrar o programa

    if unidade == 1:
        while True:
            print(Fore.GREEN + '\nPrimeira Unidade' + Style.RESET_ALL)
            # Escolher a função
            print('Escolha a função que deseja executar:')
            print(Fore.GREEN + '1. f0 = x^3 - 9x + 5' + Style.RESET_ALL)
            print(Fore.GREEN + '2. f1 = 2x^4 + 4x^3 + 3x^2 - 10x - 15' + Style.RESET_ALL)
            print(
                Fore.GREEN + '3. f2 = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x -24' + Style.RESET_ALL)
            print(
                Fore.GREEN + '4. f3 = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20' + Style.RESET_ALL)
            print(Fore.GREEN + '5. f4 = sen(x)x + 4' + Style.RESET_ALL)
            print(Fore.YELLOW + '0. Voltar para o menu anterior' + Style.RESET_ALL)

            try:
                escolhaDaFuncao = int(
                    input('Digite o número da função ou 0 para voltar: '))
            except ValueError:
                print(Fore.RED + 'Por favor, insira um número válido.\n' +
                      Style.RESET_ALL)
                continue

            if escolhaDaFuncao == 0:
                break  # Voltar para o menu anterior

            # f0 = x^3 - 9x + 5
            if escolhaDaFuncao == 1:
                arquivo = os.path.join(
                    script_directory, "unidade_1/f0=x^3-9x+5.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            # f1 = 2x^4 + 4x^3 + 3x^2 - 10x - 15
            if escolhaDaFuncao == 2:
                arquivo = os.path.join(
                    script_directory, "unidade_1/f1=2x^4+4x^3+3x^2-10x-15.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            # f2 = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x - 24
            if escolhaDaFuncao == 3:
                arquivo = os.path.join(
                    script_directory, "unidade_1/f2=x^5-2x^4-9x^3+22x^2+4x-24.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            # f3 = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20
            if escolhaDaFuncao == 4:
                arquivo = os.path.join(
                    script_directory, "unidade_1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            # f4 = sen(x)x + 4
            if escolhaDaFuncao == 5:
                arquivo = os.path.join(
                    script_directory, "unidade_1/f4=sen(x)x+4.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

    elif unidade == 2:
        while True:
            print(Fore.GREEN + '\nSegunda Unidade' + Style.RESET_ALL)
            # Escolher a função
            print('Escolha o que deseja executar:')
            print(Fore.GREEN + '1.Matriz 8x8' + Style.RESET_ALL)
            print(
                Fore.GREEN + '2.Matriz 20x20' + Style.RESET_ALL)
            print(
                Fore.GREEN + '3.Tabelamento 1' + Style.RESET_ALL)
            print(Fore.GREEN + '4.Tabelamento 2' + Style.RESET_ALL)
            print(Fore.YELLOW + '0.Voltar para o menu anterior' + Style.RESET_ALL)

            try:
                escolhaDaFuncao = int(
                    input('Digite o número da opção desejada ou 0 para voltar: '))
            except ValueError:
                print(Fore.RED + 'Por favor, insira um número válido.\n' +
                      Style.RESET_ALL)
                continue

            if escolhaDaFuncao == 0:
                break  # Voltar para o menu anterior

            if escolhaDaFuncao == 1:
                arquivo = os.path.join(
                    script_directory, "unidade_2/matriz_8x8.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 2:
                arquivo = os.path.join(
                    script_directory, "unidade_2/matriz_20x20.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 3:
                arquivo = os.path.join(
                    script_directory, "unidade_2/tabelamento1.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 4:
                arquivo = os.path.join(
                    script_directory, "unidade_2/tabelamento2.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

    elif unidade == 3:
        while True:
            print(Fore.GREEN + '\nTerceira Unidade' + Style.RESET_ALL)
            # Escolher a função
            print('Escolha o que deseja executar:')
            print(Fore.GREEN + '1.Tabelamento 1' + Style.RESET_ALL)
            print(
                Fore.GREEN + '2.Tabelamento 2' + Style.RESET_ALL)
            print(
                Fore.GREEN + '3.Tabelamento 3' + Style.RESET_ALL)
            print(Fore.GREEN + '4.F1 = f(x) = x**3' + Style.RESET_ALL)
            print(Fore.GREEN + '5.F2 = f(x)=x**2 + 2*x' + Style.RESET_ALL)
            print(Fore.GREEN + '6.F3 = f(x)=cos(x)' + Style.RESET_ALL)
            print(Fore.YELLOW + '0.Voltar para o menu anterior' + Style.RESET_ALL)

            try:
                escolhaDaFuncao = int(
                    input('Digite o número da opção desejada ou 0 para voltar: '))
            except ValueError:
                print(Fore.RED + 'Por favor, insira um número válido.\n' +
                      Style.RESET_ALL)
                continue

            if escolhaDaFuncao == 0:
                break  # Voltar para o menu anterior

            if escolhaDaFuncao == 1:
                arquivo = os.path.join(
                    script_directory, "unidade_3/tabelamento1.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 2:
                arquivo = os.path.join(
                    script_directory, "unidade_3/tabelamento2.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 3:
                arquivo = os.path.join(
                    script_directory, "unidade_3/tabelamento3.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 4:
                arquivo = os.path.join(
                    script_directory, "unidade_3/funcao1_itegracao.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 5:
                arquivo = os.path.join(
                    script_directory, "unidade_3/funcao2_itegracao.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

            if escolhaDaFuncao == 6:
                arquivo = os.path.join(
                    script_directory, "unidade_3/funcao3_itegracao.py")
                comando = f"python3 '{arquivo}'"
                subprocess.run(comando, shell=True)
                # print('Finalizado.\n')

    else:
        print(Fore.RED + 'Escolha de unidade inválida!\n' + Style.RESET_ALL)

# Limpar o console
clear()
