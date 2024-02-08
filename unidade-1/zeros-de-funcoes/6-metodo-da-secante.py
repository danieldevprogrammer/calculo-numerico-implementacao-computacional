# Função que encontrará a raiz por meio do metodo da Secante:
def secante(f, x0, x1, precisao, maxInteracoes):
    # Realiza as primeiras iterações manualmente
    fx0 = f(x0)
    fx1 = f(x1)

    # Inicializando a tabela de resultados
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

    for numIteracoes in range(maxInteracoes):
        # Adiciona a linha na tabela para a iteração atual
        tabelaResultados.add_row(
            [numIteracoes, f'{x1:.5f}', f'{f(x1):.5f}', f'{abs(f(x1)):.5f}'])

        # Calcula a nova aproximação usando a fórmula da secante
        xAproximacao = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

        # Atualiza os valores para a próxima iteração
        x0, x1 = x1, xAproximacao
        fx0, fx1 = fx1, f(xAproximacao)

        # Verifica se a diferença entre as aproximações é menor que a tolerância
        if abs(x1 - x0) < precisao:
            return x1, tabelaResultados  # Retorna a raiz e a tabela de resultados

    return None, tabelaResultados  # Retorna None se não convergir
