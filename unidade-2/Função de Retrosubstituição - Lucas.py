
colunas = float(input("Digite o número de colunas: "))
linhas = float(input("Digite o número de linhas: "))
b = [5, 7, 3]
matriz = [[0 for j in range(colunas)] for i in range(linhas)]

tamanho = len(matriz)

x = [0] * tamanho

for l in range(0, linhas):
    for c in range(0, colunas):
        matriz[l][c] = int(input(f'Digite um valor para [{l} , {c}]: '))
# Acima estou recebendo os dados

print('-=' * 30)
print('A sua matriz ficou desse jeito:')
for l in range(0, linhas):
    for c in range(0, colunas):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
# acima estou imprimindo os dados

for i in range(tamanho-1, -1, -1):
    soma = 0
    for j in range(i+1, tamanho):
        soma += matriz[i][j] * x[j]
    x[i] = (b[i] - soma) / matriz[i][i]

print("Solução: ")
for i in range(tamanho):
    print("x" + str(i+1) + " =", x[i])
