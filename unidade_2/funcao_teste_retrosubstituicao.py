# Importação da Função de Retrosubstituição
from metodos_sistemas_lineares_e_interpolacao import funcao_de_retrosubstituicao

# Exemplo de utilização
# Matriz de coeficientes (triangular superior)
A = [[3, 1, -1], [0, 1, -3], [0, 0, 8]]
b = [1, 6, 6]  # Vetor independente

# Chamada da função retrosubstituicao para resolver o sistema
funcao_de_retrosubstituicao.retrosubstituicao(A, b)
