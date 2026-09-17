import numpy as np # Biblioteca para operações com matrizes e np e o seu nme abreviado
# Criar duas matrizes 2x2
A = np.array([[1, 2], [3, 4]])

print("Matriz A:")
print(A)

B= np.array([[5, 6], [7, 8]])

print("Matriz B:")
print(B)

print("Soma de A e B:")
C = A + B
print(C)

print("Produto de A e B:")
D = np.dot(A, B)
print(D)

print("Subtração de A e B:")
E = A - B
print(E)

print("Transposta de A:")
F = A.T
print(F)

# Problema 1:
#1.Uma empresa vende dois produtos: produto A e Produto B. Cada produto usa dois recursos:Recurso 1 e Recurso 2
# 2.Ou seja Produto A usa: 2 do recurso 1 e 1 do recurso 2 e o Produto B usa: 3 do recurso 1 e 2 do recurso 2
#3.Quantidade produzida (variáveis do DIA 1):Produção do produto A = x = 10 , Produção do produto B = y = 5
#4.O que queremos descobrir. Quanto de cada recurso é usado no total?

#1,2
M = np.array([[2, 1],
              [3, 2]])
print("Matriz de recursos por produto:")
print(M)
#3 quantidades do dia 1

x= 10 #Quantidade do produto A  
y= 2 #Quantidade do produto B

Q = np.array([x,
              y]) 
print(Q)

#4 mas aqui so trata como se fosse um vetor coluna porque se fosse linha nao dari para afzer esta operacao consumo_total = M @ Q
consumo_total = M @ Q # o @ e o operador de multiplicacao de matrizes por vetor ::::: 2*10 + 1*2= 22  ; 3*10 + 2*2= 34
c= M*Q # o * e o operador de multiplicacao elemento a elemento :::::: [[20 2]
#                                                                     [30 4]]
print("#########:")
print(c)

print("Consumo total de recursos:")
print(consumo_total)  


