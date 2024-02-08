# Função que encontrará a raiz por meio do metodo da Falsa Posição:
def falsaPosicao(a, b, precisao, maxIteracoes):
    if f(a) * f(b) >= 0:
        raise ValueError(
            "Os valores de 'a' e 'b' devem ser tais que f(a) * f(b) < 0.")

    # Gerando a tabela
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = [
        'Iteração', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

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
