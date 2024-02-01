#Inserindo os valores dados
x = [-1, 0, 3]  # Aqui se determina os valor de x0,x1,x2
y = [-2, 1, 4]  # Aqui se determina os valor de y0,y1,y2
xi = 1  # valor interpolado para xi


#Calculando as diferenças divididas, criando o polinomio
tam = len(x)  # calculando o tamanho da lista

#criando uma matriz de tamanho tam x tam
f = [[None] * tam for i in range(tam)]
for i in range(tam):
    f[i][0] = y[i]  #inserindo os dados no calculo
for j in range(1, tam):
    for i in range(tam-j):
        f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])  # calculo

#Calculando o valor interpolado para xi
resultado = f[0][0]  # valor da primeira entrada na matriz
temp = 1  # começa com o valor neutro 1 e será atualizado nas iterações seguintes com os valores das diferenças
for j in range(1, tam):
    temp *= (xi - x[j-1])  # atualiza o valor de temp
    # atualiza o valor de result adicionando o produto da diferença d
    resultado += f[0][j] * temp

#Imprime o resultado
print("")
print("O Valor interpolado corresponde a f({:}) = {:.4f}".format(
    xi, resultado))
print("")
