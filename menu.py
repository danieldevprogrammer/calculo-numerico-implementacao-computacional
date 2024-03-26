import os
import subprocess
from colorama import Fore, Style, init

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
    print(Fore.GREEN + '1. Primeira unidade' + Style.RESET_ALL)
    print(Fore.GREEN + '2. Segunda unidade' + Style.RESET_ALL)
    print(Style.DIM +
          '3. Terceira unidade - Em andamento...' + Style.RESET_ALL)
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
                while True:
                    print(
                        Fore.GREEN + '\nA função Escolhida foi: f0 = x^3 - 9x + 5' + Style.RESET_ALL)
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
                            Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)
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

            # f1 = 2x^4 + 4x^3 + 3x^2 - 10x - 15
            if escolhaDaFuncao == 2:
                while True:
                    print(Fore.GREEN +
                          '\nA função Escolhida foi: f1 = 2x^4 + 4x^3 + 3x^2 - 10x - 15' + Style.RESET_ALL)
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
                            Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)
                        continue

                    script_directory = os.path.dirname(
                        os.path.realpath(__file__))

                    if escolhaDoMetodo == 1:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/1-isolamento-de-raizes-f1.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 2:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/2-metodo-da-bisseccao-f1.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 3:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/3-metodo-da-falsa-posicao-f1.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 4:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/4-metodo-do-ponto-fixo-f1.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 5:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/5-metodo-de-newton-f1.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 6:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/6-metodo-da-secante-f1.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 0:
                        break  # Voltar para o menu anterior

                    else:
                        print(Fore.RED + 'Escolha inválida!\n' + Style.RESET_ALL)

            # f2 = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x - 24
            if escolhaDaFuncao == 3:
                while True:
                    print(Fore.GREEN +
                          '\nA função Escolhida foi: f2 = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x - 24' + Style.RESET_ALL)
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
                            Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)
                        continue

                    script_directory = os.path.dirname(
                        os.path.realpath(__file__))

                    if escolhaDoMetodo == 1:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f2=x^5-2x^4-9x^3+22x^2+4x-24/1-isolamento-de-raizes-f2.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 2:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f2=x^5-2x^4-9x^3+22x^2+4x-24/2-metodo-da-bisseccao-f2.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 3:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f2=x^5-2x^4-9x^3+22x^2+4x-24/3-metodo-da-falsa-posicao-f2.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 4:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f2=x^5-2x^4-9x^3+22x^2+4x-24/4-metodo-do-ponto-fixo-f2.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 5:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f2=x^5-2x^4-9x^3+22x^2+4x-24/5-metodo-de-newton-f2.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 6:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f2=x^5-2x^4-9x^3+22x^2+4x-24/6-metodo-da-secante-f2.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 0:
                        break  # Voltar para o menu anterior

                    else:
                        print(Fore.RED + 'Escolha inválida!\n' + Style.RESET_ALL)

            # f3 = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20
            if escolhaDaFuncao == 4:
                while True:
                    print(Fore.GREEN +
                          '\nA função Escolhida foi: f3 = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20' + Style.RESET_ALL)
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
                            Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)
                        continue

                    script_directory = os.path.dirname(
                        os.path.realpath(__file__))

                    if escolhaDoMetodo == 1:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20/1-isolamento-de-raizes-f3.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 2:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20/2-metodo-da-bisseccao-f3.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 3:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20/3-metodo-da-falsa-posicao-f3.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 4:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20/4-metodo-do-ponto-fixo-f3.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 5:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20/5-metodo-de-newton-f3.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 6:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f3=5x^3+x^2-e^(1-2x)+cos(x)+20/6-metodo-da-secante-f3.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 0:
                        break  # Voltar para o menu anterior

                    # f3 = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20

            # f4 = sen(x)x + 4
            if escolhaDaFuncao == 5:
                while True:
                    print(Fore.GREEN +
                          '\nA função Escolhida foi:  f 4=sen(x ) x+4' + Style.RESET_ALL)
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
                            Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)
                        continue

                    script_directory = os.path.dirname(
                        os.path.realpath(__file__))

                    if escolhaDoMetodo == 1:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f4=sen(x)x+4/1-isolamento-de-raizes-f4.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 2:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f4=sen(x)x+4/2-metodo-da-bisseccao-f4.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 3:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f4=sen(x)x+4/3-metodo-da-falsa-posicao-f4.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 4:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f4=sen(x)x+4/4-metodo-do-ponto-fixo-f4.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 5:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f4=sen(x)x+4/5-metodo-de-newton-f4.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 6:
                        arquivo = os.path.join(
                            script_directory, "unidade-1/f4=sen(x)x+4/6-metodo-da-secante-f4.py")
                        comando = f"python3 '{arquivo}'"
                        subprocess.run(comando, shell=True)
                        print('Finalizado.\n')

                    elif escolhaDoMetodo == 0:
                        break  # Voltar para o menu anterior

            else:
                print(Fore.RED + 'Função inválida!\n' + Style.RESET_ALL)

    elif unidade == 2:
        while True:
            print(Fore.GREEN + '\nSegunda Unidade' + Style.RESET_ALL)
            # Escolher a função
            print('Escolha o que deseja executar:')
            print(Fore.GREEN + '1. Matriz 8x8' + Style.RESET_ALL)
            print(
                Fore.GREEN + '2. Matriz 20x20' + Style.RESET_ALL)
            print(
                Fore.GREEN + '3. Tabelamento 1' + Style.RESET_ALL)
            print(Fore.GREEN + '4. Tabelamento 2' + Style.RESET_ALL)
            print(Fore.YELLOW + '0. Voltar para o menu anterior' + Style.RESET_ALL)

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
                # rint('Finalizado.\n')

    elif unidade == 3:
        print(Fore.RED + '\nTerceira Unidade em construção!' +
              Fore.YELLOW + '\nAGUARDE...' + Style.RESET_ALL)

        usuarioDigitou = -1  # Inicializar para um valor diferente de 0

        while usuarioDigitou != 0:
            try:
                usuarioDigitou = int(
                    input('\nDigite 0 para voltar para o menu principal: '))
            except ValueError:
                print(
                    Fore.RED + 'Por favor, insira um número válido.\n' + Style.RESET_ALL)

        # Se o usuárioDigitou for 0, o código continuará para o próximo loop

    else:
        print(Fore.RED + 'Escolha de unidade inválida!\n' + Style.RESET_ALL)

# Limpar o console
clear()
