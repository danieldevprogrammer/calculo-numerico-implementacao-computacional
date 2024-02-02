import os
import subprocess
from colorama import Fore, Style, init

# Inicializando colorama (chamada uma vez no início do seu script)
init()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print(Fore.CYAN + Style.BRIGHT +
      'Cálculo Numérico - Implementação Computacional' + Style.RESET_ALL)

print(Style.BRIGHT + 'Aluno: \033[4mDaniel Vitor da Silva' + Style.RESET_ALL)

while True:
    # Escolher a unidade
    print('\nEscolha a unidade desejada de Cálculo Numérico:')
    print(Fore.GREEN + '1. Primeira unidade' + Style.RESET_ALL)
    print(Fore.GREEN + '2. Segunda unidade - Aguarde' + Style.RESET_ALL)
    print(Fore.GREEN + '3. Terceira unidade - Aguarde' + Style.RESET_ALL)
    print(Fore.RED + '0. Sair' + Style.RESET_ALL)

    try:
        unidade = int(input(
            'Digite o número da unidade ou 0 para sair: '))
    except ValueError:
        print(Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)
        continue

    if unidade == 0:
        break  # Sair do loop e encerrar o programa

    if unidade == 1:
        while True:
            # Escolher a função
            print('\nEscolha a função que deseja executar:')
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
                print(Fore.RED + 'Por favor, insira um número válido.' +
                      Style.RESET_ALL)
                continue

            if escolhaDaFuncao == 0:
                break  # Voltar para o menu anterior

            if escolhaDaFuncao == 1:
                print('\nA função Escolhida foi: f1 = x^3 - 9x + 5')

                while True:
                    print('Escolha o método que deseja executar:')
                    print(Fore.GREEN + '1. Isolamento de Raízes' + Style.RESET_ALL)
                    print(Fore.GREEN + '2. Método da Bissecção')
                    print(Fore.GREEN + '3. Método da Falsa Posição' +
                          Style.RESET_ALL)
                    print(Fore.GREEN + '4. Método do Ponto Fixo' + Style.RESET_ALL)
                    print(Fore.GREEN + '5. Método de Newton')
                    print(Fore.GREEN + '6. Método da Secante')
                    print(Fore.YELLOW +
                          '0. Voltar para o menu anterior' + Style.RESET_ALL)

                    try:
                        escolhaDoMetodo = int(
                            input('Digite o número do método que deseja executar ou 0 para voltar: '))
                    except ValueError:
                        print(
                            Fore.RED + 'Por favor, insira um número válido.' + Style.RESET_ALL)
                        continue

                    script_directory = os.path.dirname(
                        os.path.realpath(__file__))

                    if escolhaDoMetodo == 1:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f0=x^3-9x+5/1-isolamento-de-raizes-f0.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 2:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f0=x^3-9x+5/2-metodo-da-bisseccao-f0.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 3:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f0=x^3-9x+5/3-metodo-da-falsa-posicao-f0.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 4:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f0=x^3-9x+5/4-metodo-do-ponto-fixo-f0.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 5:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f0=x^3-9x+5/5-metodo-de-newton-f0.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 6:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f0=x^3-9x+5/6-metodo-da-secante-f0.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 0:
                        break  # Voltar para o menu anterior

                    else:
                        print(Fore.RED + 'Escolha inválida!\n' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Função inválida!\n' + Style.RESET_ALL)

    else:
        print(Fore.RED + 'Escolha de unidade inválida!\n' + Style.RESET_ALL)

# Limpar o console
clear()
