# Função que encontrará a raiz por meio do método da bissecção:
def bisseccao(a, b, precisao, f, maxIteracoes):
    # Inicialize x com o valor médio do intervalo inicial [a, b]
    x = (a + b) / 2

    # Gerando a tabela
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração',
                                    'a', 'b', 'x', 'f(a)', 'f(x)', '|f(x)|']
    # Limitando para 5 casas decimais que vão aparecer na tabela
    tabelaResultados.float_format = ".15"

    raizConvergente = None
    numIteracoes = 0

    # Laço de repetição para que enquanto o valor absoluto de f(x) for maior do que a precisão a operação se repita:
    while abs(f(x)) > precisao and numIteracoes < maxIteracoes:
        # Atualizamos o x usando a fórmula do método da bissecção:
        x = (a + b) / 2
        tabelaResultados.add_row(
            [numIteracoes, a, b, x, f(a), f(x), abs(f(x))])

        # Atualizamos a e b de acordo com o sinal de f(a) e f(x):
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        numIteracoes += 1

        if abs(f(x)) < precisao:
            raizConvergente = x

    return tabelaResultados, raizConvergente
