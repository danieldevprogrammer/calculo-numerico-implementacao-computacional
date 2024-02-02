
#aqui estou definindo a razão da matriz(pedindo ao usuario)
colunas = int(input("digite o numero de colunas: "))
linhas = int(input("digite o numero de linhas: "))

#aqui estou criando ela
matriz = [[0 for j in range(colunas)] for i in range(linhas)]
b = [0 for j in range(linhas)] 

# aqui estou pedindo para o usuário inserir os dados da matriz
for l in range(0, linhas):
    for c in range(0, colunas):
        matriz[l][c] = int(input(f'digite um valor para [{l} , {c}]: '))
# aqui estou pedindo para o usuário inserir os dados da matriz b
for l in range(0, linhas):
    b[l] = int(input(f'digite o valor do termo idependente da linha[{l}]: '))


# Definindo a tolerância de erro desejada 
tol = float(input("digite a tolerância:"))

# Definindo o número máximo de iterações 

max_iter = int(input("digite o numero de máximo de interações: "))


#aqui estou imprimindo para mostrar a matriz
print('-=' * 30)
print('A sua matriz ficou desse jeito')
for l in range(0, linhas):
    for c in range(0, colunas):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


# aqui estou deifinindo o vetor inicial usado na aula para comparar com o metodo jacobi
x0 = [0.7, -1.6, 0.6]



# Inicializando as soluções, passando os dados da lista x0 para x
x = x0.copy()

# Aqui Inicia as iterações do método de GS
for k in range(max_iter):
    # Atualizando cada solução usando as soluções mais recentes
    for i in range(len(matriz)):
        sum1 = sum([matriz[i][j] * x[j] for j in range(i)])
        sum2 = sum([matriz[i][j] * x[j] for j in range(i+1, len(matriz))])
        x[i] = (b[i] - sum1 - sum2) / matriz[i][i]
    
    # Verificando a convergência do método
    error = max(abs(x[i] - x0[i]) for i in range(len(matriz)))
    if error < tol:
        break
    
    # Atualizando as soluções anteriores
    x0 = x.copy()

# Verificando se o método convergiu
if k == max_iter-1:
    print("O metodo de Gauss Seidel não convergiu após {max_iter} iterações")
else:
    print("As soluções aproximadas de x1, x2, x3 são:", x)
