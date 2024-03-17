# Função para a resolução do método de retrosubstituição
def retrosubstituicao(A, b):
    # Determina o tamanho do sistema (quantidade de equações)
    n = len(A)

    # Verifica se a matriz é triangular superior
    for i in range(n):
        for j in range(i):
            if A[i][j] != 0:
                raise ValueError("O sistema não está triangularizado")

    resultado = [0] * n  # Inicializa uma lista para armazenar as soluções

    # Itera pelas linhas da matriz de coeficientes de baixo para cima
    for i in range(n-1, -1, -1):
        # Calcula a soma dos produtos dos coeficientes das incógnitas já conhecidas (resultado[j])
        # pelos valores das incógnitas na linha atual
        soma = sum(A[i][j] * resultado[j] for j in range(i+1, n))
        # Calcula o valor da incógnita atual, dividindo a diferença entre o vetor independente
        # na linha atual e a soma calculada, pelo coeficiente correspondente à incógnita atual
        resultado[i] = (b[i] - soma) / A[i][i]

    print('\nFunção de Retrosubstituição:')
    print(f'A = {A}')
    print(f'b = {b}')

    # Imprime as soluções do sistema
    print("Solução: ")
    for i in range(n):
        print(f"x{i+1} = {resultado[i]:.4f}")

    return resultado
