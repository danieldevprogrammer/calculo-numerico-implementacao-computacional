# Função para isolamento das Raízes:
def isolamentoRaizes(a, b, amplitude, f):
    # Valores de x:
    valoresDeX = np.arange(a, b + amplitude, amplitude)

    # Valores de y:
    valoresDeY = [f(x) for x in valoresDeX]

    # Criando a tabela com PrettyTable
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['x', 'f(x)']

    for x, y in zip(valoresDeX, valoresDeY):
        tabelaResultados.add_row([x, y])

    # Imprimir a tabela no console
    print(tabelaResultados)

    # Retornar a tabela para ser usada fora da função
    return tabelaResultados, valoresDeX, valoresDeY
