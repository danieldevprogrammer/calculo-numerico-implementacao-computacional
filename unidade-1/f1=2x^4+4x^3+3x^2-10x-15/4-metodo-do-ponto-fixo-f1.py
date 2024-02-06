# Implementação do Método do Ponto Fixo:
from prettytable import PrettyTable
import time
import os
from datetime import datetime

# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x)=2x^4+4x^3+3x^2-10x-15'

diretorio_resultados = "unidade-1/f1=2x^4+4x^3+3x^2-10x-15/resultados-em-txt-e-grafico-f1"

# Criar a estrutura de diretório, se não existir
if not os.path.exists(diretorio_resultados):
    os.makedirs(diretorio_resultados)

# Obter a data e hora atual
data_e_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Definir o caminho completo para os arquivos
caminho_tabela = os.path.join(
    diretorio_resultados, f'4-metodo-do-ponto-fixo-{nomeDaFuncao}-{data_e_hora_atual}.txt')

print(f'\nMétodo do Ponto Fixo da função {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 3
# A precisão da raíz.
precisao = 1e-10
# Número máximo de iterações
maxIteracoes = 500

# Inicialização de x0, é uma opção começar com x no meio do intervalo, mas não é obrigatório.
x = (a + b) / 2

print(f'I=[{a},{b}], Precisão={precisao}, X0={x} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()

# Definindo a função f(x):


def f(x):
    return 2 * x**4 + 4 * x**3 + 3 * x**2 - 10 * x - 15

# Definindo a função fi


def fi(x):
    return (2 * x**4 + 4 * x**3 + 3 * x**2 - 15) / 10


# Definindo a função que encontrará a raiz por meio do metodo do Ponto Fixo:
def pontoFixo(a, b, x, precisao, maxIteracoes):
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = [
        'Iteração', 'a', 'b', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".15"  # Limitando para 15 casas decimais

    raizConvergente = None

    # Acrescentando na tabela uma linha a mais para aparecer a iteração 0
    tabelaResultados.add_row([0, a, b, "{:.15f}".format(x), f(x), abs(f(x))])

    for numIteracoes in range(1, maxIteracoes + 1):
        xAnterior = x
        x = fi(x)

        # Verificar se a função está saindo de controle
        if abs(x) > 1e10:
            print(
                'A função está saindo de controle, para evitar um erro de overflow as iterações foram paradas!\nO erro aconteceu provavelmente por causa da má definição da função Fi.\n')

            # Adicionando a mensagem ao arquivo de texto
            with open(caminho_tabela, 'w') as file:
                file.write(
                    'A função está saindo de controle, para evitar um erro de overflow as iterações foram paradas!\nO erro aconteceu provavelmente por causa da má definição da função Fi.\n')
            break

        tabelaResultados.add_row(
            [numIteracoes, a, b, "{:.5f}".format(x), f(x), abs(f(x))])

        if abs(x - xAnterior) < precisao:
            raizConvergente = x
            break  # Sai do loop quando a precisão é atingida
    else:
        print('\nO número máximo de iterações foi atingido.')

    return tabelaResultados, raizConvergente


# Chamando a função do Método do Ponto Fixo
tabelaResultados, raizConvergente = pontoFixo(a, b, x, precisao, maxIteracoes)

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Salvando a tabela em um arquivo txt com informações adicionais
with open(caminho_tabela, 'a') as file:
    file.write(f'Método do Ponto Fixo da função {nomeDaFuncao}\n')
    file.write(
        f'I=[{a},{b}], Precisão={precisao}, X0={x} e Número Máximo de Iterações={maxIteracoes}.\n')
    file.write(str(tabelaResultados))

# Verificando se a raiz convergente foi encontrada:
if raizConvergente is not None:
    print(f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}')
else:
    print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

# Adicionar se a raiz convergente foi encontrada ao arquivo de texto
with open(caminho_tabela, 'a') as file:
    if raizConvergente is not None:
        file.write(
            f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}\n')
    else:
        file.write(
            '\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.\n')

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo
print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

# Adicionar o tempo de execução ao arquivo de texto
with open(caminho_tabela, 'a') as file:
    file.write(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.\n')
