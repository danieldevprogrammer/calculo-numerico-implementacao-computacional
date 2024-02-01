import os
import subprocess

print('\033[1;34mCálculo Numérico - Implementação Computacional\033[m')
print('\033[4mAluno: Daniel Vitor da Silva\033[m')

# Escolher a unidade
print('Escolha a unidade desejada de Cálculo Numérico:')
print('1. Primeira unidade')
print('2. Segunda unidade')
print('3. Terceira unidade')

unidade = input('Digite o número da unidade: ')

if unidade == '1':
    print('\nEscolha a função que deseja executar:')
    print('1. f1 = x^3 - 9x + 5')
    print('2. f2 = 2x^4 + 4x^3 + 3x^2 - 10x - 15')
    print('3. f3 = x^5 - 2x^4 - 9x^3 + 22x^2 + 4x -24')
    print('4. f4 = 5x^3 + x^2 - e^(1-2x) + cos(x) + 20')
    print('5. f5 = sen(x)x + 4')

    escolhaDaFuncao = input('Digite o número da função que deseja executar: ')

    # 1. f1 = x^3 - 9x + 5
    if escolhaDaFuncao == '1':
        print('\nA função Escolhida foi: f1 = x^3 - 9x + 5')

        print('Escolha o método que deseja executar:')
        print('1. Isolamento de Raízes')
        print('2. Método da Bissecção')
        print('3. Método da Falsa Posição')
        print('4. Método do Ponto Fixo')
        print('5. Método de Newton')
        print('6. Método da Secante')

        escolhaDoMetodo = int(input('Digite o número do método que deseja executar: '))

        # Isolamento de Raízes
        if escolhaDoMetodo == 1:
            arquivo = "Unidade 1/1.Isolamento de Raízes.py"
            comando = f"python3 '{arquivo}'"
            subprocess.run(comando, shell=True)
            exit('Programa finalizado.')

        # Bissecção
        elif escolhaDoMetodo == 2:
            os.system("python /home/ubuntu_daniel/DANIEL/Cálculo Numérico - Implementação Computacional/Unidade 1/2.Método da Bissecção.py")
            exit('Programa finalizado.')

        # Falsa Posição
        elif escolhaDoMetodo == 3:
            os.system("python /home/ubuntu_daniel/DANIEL/Cálculo Numérico - Implementação Computacional/Unidade 1/3.Método da Falsa Posição-f1.py")
            exit('Programa finalizado.')

        # Ponto Fixo
        elif escolhaDoMetodo == 4:
            os.system("python /home/ubuntu_daniel/DANIEL/Cálculo Numérico - Implementação Computacional/Unidade 1/4.Método do Ponto Fixo.py")
            exit('Programa finalizado.')

        # Newton
        elif escolhaDoMetodo == 5:
            os.system("python /home/ubuntu_daniel/DANIEL/Cálculo Numérico - Implementação Computacional/Unidade 1/5.Método de Newton.py")
            exit('Programa finalizado.')

        # Secante
        elif escolhaDoMetodo == 6:
            os.system("python /home/ubuntu_daniel/DANIEL/Cálculo Numérico - Implementação Computacional/Unidade 1/Secante.py")
            exit('Programa finalizado.')
        else:
            print("Escolha inválida!")
else:
    print("Unidade inválida!")



'''
# limpar o console


#def clear():
#    os.system('clear')


# limpa o console
#1
# clear()
'''