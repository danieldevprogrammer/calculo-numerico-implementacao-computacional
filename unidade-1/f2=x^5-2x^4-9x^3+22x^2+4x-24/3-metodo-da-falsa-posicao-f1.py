# Implementação do Método da Falsa Posição:
from prettytable import PrettyTable
import time
import os
from datetime import datetime


# Variável para determinar qual vai ser a função.
nomeDaFuncao = 'f(x)=x^5-2x^4-9x^3+22x^2+4x-24'

diretorio_resultados = "unidade-1/f2=x^5-2x^4-9x^3+22x^2+4x-24/resultados-em-txt-e-grafico-f2"
# Criar a estrutura de diretório, se não existir
if not os.path.exists(diretorio_resultados):
    os.makedirs(diretorio_resultados)

# Obter a data e hora atual
data_e_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Definir o caminho completo para os arquivos
caminho_tabela = os.path.join(
    diretorio_resultados, f'3-metodo-da-falsa-posicao-{nomeDaFuncao}-{data_e_hora_atual}.txt')

print(f'\nMétodo da Falsa Posição da função {nomeDaFuncao}')
# Valor ínicial do intervalo:
a = 0
# Valor final do intervalo:
b = 5
# A precisão da raíz.
precisao = 1e-10
# Número máximo de interações
maxIteracoes = 500

print(f'I=[{a},{b}], Precisão={precisao} e Número Máximo de Iterações={maxIteracoes}.\n')

# Medindo o tempo de início do cálculo
inicioTempo = time.time()


# Definindo a função f(x):
def f(x):
    return x**5 - 2*x**4 - 9*x**3 + 22*x**2 + 4*x - 24


# Definindo a função que encontrará a raiz por meio do metodo da Falsa Posição:
def falsaPosicao(a, b, precisao, maxIteracoes):
    if f(a) * f(b) >= 0:
        raise ValueError(
            "Os valores de 'a' e 'b' devem ser tais que f(a) * f(b) < 0.")

    # Gerando a tabela
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = [
        'Iteração', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".15"  # Limitando para 15 casas decimais

    # Inicializando raizConvergente como None
    raizConvergente = None

    for i in range(maxIteracoes):
        x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        tabelaResultados.add_row(
            [i, a, b, "{:.5f}".format(x), f(a), f(b), f(x), abs(f(x))])

        if abs(f(x)) < precisao:
            raizConvergente = x
            break  # Sai do loop quando a precisão é atingida
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

    return tabelaResultados, raizConvergente


# Chamando a função da Falsa Posição
tabelaResultados, raizConvergente = falsaPosicao(a, b, precisao, maxIteracoes)

# Medindo o tempo de fim do cálculo
fimTempo = time.time()

# Imprimindo a tabela de resultados
print(tabelaResultados)

# Salvando a tabela em um arquivo txt com informações adicionais
with open(caminho_tabela, 'w') as file:
    file.write(f'Método da Falsa Posição da função {nomeDaFuncao}\n')
    file.write(
        f'I=[{a},{b}], Precisão={precisao} e Número Máximo de Iterações={maxIteracoes}.\n')
    file.write(str(tabelaResultados))

# Verificando se a raiz convergente foi encontrada:
if raizConvergente is not None:
    print(f'\nRaiz convergente encontrada foi: {raizConvergente:.15f}')
else:
    print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

# Adicionar se a raiz convergente foi encontrada ao arquivo de texto
with open(caminho_tabela, 'a') as file:
    if raizConvergente is not None:
        file.write(
            f'\nRaiz convergente encontrada foi: {raizConvergente:.15f}\n')
    else:
        file.write(
            '\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.\n')

# Calculando e mostrando o tempo total de cálculo
tempoTotal = fimTempo - inicioTempo

print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

# Adicionar o tempo de execução ao arquivo de texto
with open(caminho_tabela, 'a') as file:
    file.write(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.\n')
