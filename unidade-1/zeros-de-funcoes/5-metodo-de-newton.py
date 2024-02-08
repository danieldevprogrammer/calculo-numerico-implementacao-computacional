# Definindo a função da derivada numérica de f(x)
def derivadaNumericaDeF(x, h=0.0001):
    # h=0.0001, é um valor muito próximo de zero, para que não ocarra um erro de indeterminação na função e assim pode calcular a derivada númerica
    return (f(x + h) - f(x)) / h


# Função que encontrará a raiz por meio do metodo de Newton:
def Newton(x, precisao, maxIteracoes):
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

    raizConvergente = None

    # Inicializa o valor de x com o palpite inicial x0
    x = x0

    # Loop para as iterações
    for numIteracoes in range(maxIteracoes):
        valorDef = f(x)

        # Adiciona a iteração atual à tabela
        tabelaResultados.add_row(
            [numIteracoes, x, valorDef, abs(valorDef)])

        # Condição para quando a raiz convergir parar o loop
        if abs(valorDef) < precisao:
            raizConvergente = x
            break

        # Calculando a derivada de numérica de f(x)
        derivadaNumerica = derivadaNumericaDeF(x)
        # Verificando se a derivade numérica é igual a 0, para evitar erros.
        if derivadaNumerica == 0:
            print("Derivada é zero. Escolha outro palpite inicial.")
            return None

        x = x - (valorDef / derivadaNumerica)

        if abs(valorDef) < precisao:
            raizConvergente = "{:.5f}".format(x)
            break

    else:
        print("\nO número máximo de iterações foi atingido.")

    return tabelaResultados, raizConvergente
