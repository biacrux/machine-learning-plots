
a= 10
b=3
c=1.5
d= 'numero inteiro'

print('1' ,a)
print('2' ,b)

print('3' ,a+b)
print('4' ,a-b)
print('5' ,a*b)
print('::' ,a,d) # para juntar uma string nao pode ser com + tem de ser por virgulas 


a=a+1 #aqui o a vai mudar, mas o de cima nao
print(':' ,a)

print(type(a)) # typed vai dar a que classe pertence cada variavel 
print(type(c))

print('\n')
#operacoes de oprocedencia matematica 
print(2 + 3 * 4)

#entrada como utilizador interacao 
u=int(input("Escreva um numero: "))
print('seu numero é: ' ,u*2)

print('\n')
u=int(input("Escreva um numero(maior que 0): "))
if u<0:
    print('seu numero é invalido: ')
elif u==0:                              #dica: o = guarda valor ;;; o == pregunta se e igual
    print('seu numero é: 0')
else:
    print('seu numero é: ' ,u*2)

print('\n')
# o valor do =
x = 5
x = x + 2
print(x)

print('########################################################################################')
#problema 1:
#Cria um programa que: pede dois números, diz qual é o maior,diz se são iguais

ask1= int(input("Write your first number: "))
ask2= int(input("Write your second number: "))

if(ask1 < ask2):
    print("The biggest number is: ", ask2)
elif(ask1 > ask2):
    print("The biggest number is: ", ask1)
else:
    print("Both numbers are equals")

# Problema 1 Avançado:
# Programa que pede dois números, verifica se são válidos, diz qual é o maior e qual é o menor

def get_number(prompt): #uma funcao que vai verificar os numero validos o promp é o texto que vai aparecer no usuario
    while True: #loop infinito para pedir o número várias vezes até o utilizador escrever certo.
        try: # e um bloco de erro se der erro vai no except
            return float(input(prompt)) #transforma o texto em numero decimal
        except ValueError:
            print('Invalid input. Please enter a number.')


ask3= int(input("Write your first number: "))
ask4= int(input("Write your second number: "))

if(ask3 < ask4):
    print("The biggest number is: ", ask3)
elif(ask3 > ask4):
    print("The biggest number is: ", ask4)
else:
    print("Both numbers are equals")

print('########################################################################################')

