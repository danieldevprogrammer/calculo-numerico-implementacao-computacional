# Implementação do método de retrosubstituição
def retrosubstituicao(A, b):
    # Verifica se a matriz é quadrada
    n = len(A)
    if len(A[0]) != n:
        print("A matriz não é quadrada")
        return []

    # Verifica se a matriz é triangular superior
    for i in range(n):
        for j in range(i):
            if A[i][j] != 0:
                print("A matriz não está triangularizada")
                return []

    x = [0] * n  # Inicializa uma lista para armazenar as soluções

    # Itera pelas linhas da matriz de coeficientes de baixo para cima
    for i in range(n-1, -1, -1):
        # Calcula a soma dos produtos dos coeficientes das incógnitas já conhecidas (x[j])
        # pelos valores das incógnitas na linha atual
        soma = sum(A[i][j] * x[j] for j in range(i+1, n))
        # Calcula o valor da incógnita atual, dividindo a diferença entre o vetor independente
        # na linha atual e a soma calculada, pelo coeficiente correspondente à incógnita atual
        x[i] = (b[i] - soma) / A[i][i]

    print('Retrosubstituição de:')
    print(f'A = {A}')
    print(f'b = {b}')

    # Imprime as soluções do sistema
    print('Resolução por Retrosubstituição:')
    for i in range(n):
        print(f'x{i+1} = {x[i]:.4f}')

    return x
