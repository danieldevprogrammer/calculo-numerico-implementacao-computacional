import numpy as np
import os
import time
from datetime import datetime
from unidade_2.sistemas_lineares_interpolacao import funcao_retrosubstituicao

# Variável para determinar qual vai ser a Matriz.
nome = 'Matriz 3x3 - Exemplo da Sala'
print(nome)

# Teste da função de retrosubstituição usando exemplo feito em sala
# Matriz de coeficientes A (triangular superior)
# Corrigido para adicionar listas internas
A = np.array([[3, 1, -1], [0, 1, -3], [0, 0, 8]])
# Vetor independente b
b = np.array([1, 6, 6])

# Chamando a função retrosubstituicao
x = funcao_retrosubstituicao.retrosubstituicao(A, b)
