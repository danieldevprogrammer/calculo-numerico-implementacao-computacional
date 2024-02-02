import os
import subprocess


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print('\033[1;34mCálculo Numérico - Implementação Computacional\033[m')
print('\033[4mAluno: Daniel Vitor da Silva\033[m')

while True:
    # Escolher a unidade
    print('Escolha a unidade desejada de Cálculo Numérico:')
    print('1. Primeira unidade')
    print('2. Segunda unidade')
    print('3. Terceira unidade')
    print('0. Sair')

    try:
        unidade = int(input('Digite o número da unidade ou 0 para sair: '))
    except ValueError:
        print('Por favor, insira um número válido.\n')
        continue

    if unidade == 0:
        break  # Sair do loop e encerrar o programa

    if unidade == 1:
        while True:
            # Escolher a função
            print('\nEscolha a função que deseja executar:')
            print('1. f0 = x^3 - 9x + 5')
            print('2. f1 = 2x^4 + 4x^3 + 3x^2 - 10x - 15')
            print('3. f2 = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x -24')
            print('4. f3 = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20')
            print('5. f4 = sen(x)x + 4')
            print('0. Voltar para o menu anterior')

            try:
                escolhaDaFuncao = int(
                    input('Digite o número da função ou 0 para voltar: '))
            except ValueError:
                print('Por favor, insira um número válido.')
                continue

            if escolhaDaFuncao == 0:
                break  # Voltar para o menu anterior

            if escolhaDaFuncao == 1:
                print('\nA função Escolhida foi: f1 = x^3 - 9x + 5')

                while True:
                    print('Escolha o método que deseja executar:')
                    print('1. Isolamento de Raízes')
                    print('2. Método da Bissecção')
                    print('3. Método da Falsa Posição')
                    print('4. Método do Ponto Fixo')
                    print('5. Método de Newton')
                    print('6. Método da Secante')
                    print('0. Voltar para o menu anterior')

                    try:
                        escolhaDoMetodo = int(
                            input('Digite o número do método que deseja executar ou 0 para voltar: '))
                    except ValueError:
                        print('Por favor, insira um número válido.')
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
                        print('Escolha inválida!\n')
            else:
                print('Função inválida!\n')

    else:
        print('Escolha de unidade inválida!\n')

# Limpar o console
clear()
