import numpy as np
import time
import os
import datetime

titulo_arquivo = datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
nome_arquivo = f"R_EliminacaoGauss/{titulo_arquivo}.txt"

if not os.path.exists("R_EliminacaoGauss"):
    os.makedirs("R_EliminacaoGauss")

# Matriz e vetor b
A = np.array([[25.9912, 3.5970, 9.8469, 4.2332, 34.7726, 27.3573, 42.4294, 23.7293, 32.5902, 5.2457, 15.5347, 30.4976, 23.8243, 2.6875, 3.1043, 8.2600, 22.7991, 28.6107, 1.9863, 22.3779],
              [27.5150, 11.6134, 21.8972, 3.9585, 47.0922, 14.4264, 13.8740, 20.5405, 5.8629, 9.4681,
                  39.0348, 16.5360, 11.3016, 40.0497, 3.8644, 24.1319, 23.7222, 43.7957, 0.9373, 13.2087],
              [24.0127, 12.7567, 38.8971, 27.4739, 24.1394, 24.6710, 21.4854, 31.2840, 44.3081, 48.4670,
                  23.1294, 45.4513, 15.0620, 43.9511, 35.4743, 44.6662, 45.4353, 20.8848, 6.9530, 39.5928],
              [17.2247, 24.1012, 39.3125, 40.5014, 23.8175, 28.1473, 19.4170, 34.4578, 13.5618, 26.2925,
               20.0502, 25.9280, 30.4854, 2.6948, 44.9628, 11.1522, 32.9802, 2.6331, 31.4438, 7.3993],
              [38.3010, 2.5536, 5.3225, 11.5662, 3.8627, 45.2881, 38.9639, 41.9614, 7.9155, 1.6839,
               24.1143, 49.5188, 2.2456, 41.3303, 41.1228, 0.8342, 2.3390, 40.4997, 3.2865, 28.6288],
              [29.4035, 18.7453, 14.1898, 14.5555, 14.8429, 6.2584, 40.2102, 15.0716, 8.5625, 16.0001,
               32.6796, 25.9817, 3.1318, 4.4688, 28.8178, 28.2966, 21.9404, 46.9778, 6.0105, 44.2187],
              [47.4318, 27.8799, 4.1246, 35.6247, 29.6943, 17.3475, 49.8659, 17.7255, 48.7461, 35.9461,
               0.4752, 3.0264, 33.6818, 27.0865, 29.9132, 49.8034, 12.0512, 17.8282, 44.7058, 0.8590],
              [26.0571, 42.3460, 26.8624, 31.3020, 23.3236, 38.2144, 3.7498, 17.4426, 43.6287, 47.8138,
               13.9971, 20.8457, 29.8216, 37.2478, 27.5096, 31.5582, 27.0015, 19.1845, 26.2130, 24.6012],
              [35.5450, 33.7343, 30.1752, 7.1046, 5.7773, 16.5032, 49.2501, 34.6238, 47.7127, 34.9745,
               16.0034, 31.7337, 45.7497, 37.9706, 46.8178, 47.4970, 19.1735, 14.9837, 27.3104, 7.9055],
              [36.4029, 40.7650, 27.4499, 43.7357, 20.4064, 24.8010, 24.0493, 4.8495, 6.6130, 39.5465,
               7.0996, 16.5272, 2.2924, 19.8485, 4.6905, 8.5942, 44.1106, 32.1502, 3.4548, 28.9755],
              [20.5734, 28.5464, 7.9724, 9.7784, 2.3351, 32.5191, 25.6488, 8.9284, 11.9055, 45.8057,
               5.6992, 17.495, 12.6232, 20.0658, 30.9219, 37.0543, 42.1311, 17.5571, 47.2811, 4.5041],
              [16.9235, 2.488, 16.7162, 3.2648, 20.8257, 19.8963, 37.5233, 0.8241, 20.3117, 8.3805,
               16.4194, 23.7695, 13.9425, 42.4739, 37.1793, 17.9694, 18.9548, 40.3722, 5.2048, 26.7414],
              [24.9236, 35.073, 19.7356, 41.2959, 18.8251, 13.0565, 38.1969, 9.8102, 6.6108, 35.7143,
               32.8824, 43.8445, 44.2042, 43.6896, 49.2848, 23.3128, 27.369, 27.762, 38.2494, 25.0142],
              [8.1347, 49.8483, 37.7969, 14.2606, 32.7716, 39.9544, 14.6147, 3.6723, 31.1751, 27.1158,
               25.5338, 10.034, 46.4516, 39.6304, 1.1259, 46.6044, 44.7934, 31.5724, 32.706, 7.3429],
              [27.5424, 3.3831, 9.471, 36.8023, 43.4264, 41.4315, 18.1645, 20.452, 4.3419, 46.0158,
               14.6602, 5.6187, 33.4496, 8.1363, 40.1052, 12.5039, 17.3538, 4.2424, 11.4864, 3.9262],
              [28.0826, 19.5612, 6.933, 41.8091, 20.494, 14.9644, 33.6951, 32.0018, 41.491, 48.9065,
               5.843, 8.6043, 38.8255, 5.4775, 29.762, 12.8112, 9.7328, 40.4439, 2.2981, 48.1627],
              [32.6374, 6.9866, 22.8888, 11.758, 5.123, 22.8841, 43.3391, 21.9157, 30.3355, 20.726,
               0.7067, 37.361, 25.7343, 32.7891, 42.9858, 7.2287, 23.7361, 49.701, 31.2349, 44.4439],
              [17.9171, 36.9246, 13.3357, 9.284, 11.7589, 7.9458, 41.5403, 13.6596, 22.3272, 27.6684,
               1.1278, 33.5705, 26.3999, 40.1055, 21.5612, 13.2327, 22.7153, 40.5347, 22.6012, 2.7225],
              [6.182, 29.2679, 32.4382, 4.7003, 14.1065, 0.4651, 37.9867, 40.4509, 9.3526, 32.5984,
               47.7834, 0.1777, 46.9684, 47.6789, 0.9149, 40.5299, 39.0676, 9.2677, 42.9246, 28.1954],
              [49.0218, 44.2264, 49.3287, 28.8533, 49.3146, 2.9371, 46.475, 42.784, 35.5059, 10.5379, 39.8764, 21.7893, 33.5127, 44.3185, 27.8742, 29.3751, 0.9935, 33.8722, 38.0926, 19.1896]], dtype=float)
b = np.array([40.4554, 10.1067, 48.7878, 30.4491, 49.0677, 43.4887, 43.3943, 30.3153, 33.6710, 26.7800,
             40.7279, 17.5335, 33.5339, 17.1401, 0.9459, 32.7490, 5.8962, 34.1086, 36.2167, 28.7823], dtype=float)

# Determina a ordem da matriz contando o número de linhas
n = A.shape[0]

# Construção da matriz aumentada [A|b]
augmented_matrix = np.column_stack((A, b))

# Verifica se o usuário deseja salvar a matriz no arquivo
save_matrix = input("Deseja salvar a matriz no arquivo TXT? (s/n)")

with open(nome_arquivo, "w", encoding="utf-8") as f:
    f.write(
        f"Grupo 1 - Método de Eliminação de Gauss \nResultado obtido em: {titulo_arquivo}\n")

    # Se o usuário deseja salvar a matriz no arquivo, imprime a matriz e o vetor b no arquivo
    if save_matrix.lower() == 's':
        print("O usuário confirmou em mostrar a matriz dentro do arquivo", file=f)
        print("A matriz A é:", file=f)
        print(A, file=f)
        print("O vetor b é:", file=f)
        print(b, file=f)
        print("\n", file=f)
    else:
        print("O usuário não confirmou em mostrar a matriz dentro do arquivo", file=f)

    start_time = time.time()
    # Eliminação de Gauss
    for i in range(n):
        # Pivô é o elemento da diagonal principal
        pivot = augmented_matrix[i, i]
        # Se o pivô for zero, então ocorreu uma divisão por zero. Nesse caso, encerra a execução
        if pivot == 0:
            print("Erro: divisão por zero!", file=f)
            print("Erro: divisão por zero!")
            exit()
        # Zera os elementos abaixo do pivô
        for j in range(i+1, n):
            multiplier = augmented_matrix[j, i] / pivot
            augmented_matrix[j, i:] = augmented_matrix[j, i:] - \
                multiplier * augmented_matrix[i, i:]

    # Solução do sistema
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented_matrix[i, -1] -
                np.dot(augmented_matrix[i, i:-1], x[i:])) / augmented_matrix[i, i]

    # Exibição da solução
    print("A solução do sistema para a matriz definida dentro do código é: ", file=f)
    print("A solução do sistema para a matriz definida dentro do código é: ")
    for i in range(n):
        if abs(x[i]) < 0.01:
            x[i] = 0.0
        print(f"x{i+1} = {x[i]:.4f}", file=f)
        print(f"x{i+1} = {x[i]:.4f}")
    end_time = time.time()
    # Calculando o tempo de execução
    runtime = end_time - start_time
    print(
        f"Tempo de execução do método de Eliminação de Gauss foi: {runtime:.6f} segundos", file=f)
    print(
        f"Tempo de execução do método de Eliminação de Gauss foi: {runtime:.6f} segundos")
