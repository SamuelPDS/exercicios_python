#DESAFIO 5
num = int(input('Informe um número:' ))
s = num+1
a = num-1
print('O sucesso de {} é {}. O antecesso de {} é {}'.format(num, s, num, a))

#DESAFIO 6
num1 = int(input('Informe o seu número: '))
d = num1*2
o = num1*3
r = num1**(1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz é {:.2f}'.format(num1, d, o, r))

#DESAFIO 7
num2 = float(input('Informe a primeira nota do aluno: '))
num3 = float(input('Informe a segunda nota do aluno'))
m = (num2+num3)/2
print('A média das notas {:.1f}, {:.1f} é = {:.1f}'.format(num2,num3,m))

#DESAFIO 8
num4 = int(input('Escreva uma medida: '))
m2 = num4
cm = num4/100
mm = num4/1000
print('A medida apresentada é de {} metros, {} centímetros e {} milímetros'.format(m2, cm, mm))

#DESAFIO 9
num5 = int(input('Informe um número qualquer: '))
print('{} * {} = {}'.format(num5, 1, num5*1))
print('{} * {} = {}'.format(num5, 2, num5*2))
print('{} * {} = {}'.format(num5, 3, num*3))
print('{} * {} = {}'.format(num5, 4, num5*4))
print('{} * {} = {}'.format(num5, 5, num5*5))
print('{} * {} = {}'.format(num5, 6, num5*6))
print('{} * {} = {}'.format(num5, 7, num5*7))
print('{} * {} = {}'.format(num5, 8, num5*8))
print('{} * {} = {}'.format(num5, 9, num5*9))



#DESAFIO 10
dinheiro = float(input('Quanto você tem de dinheiro?'))
dolar = dinheiro/5.05
print('Você possui {:.2f} dólares com {} reais'.format(dolar, dinheiro))

#DESAFIO 11
largura = float(input('Informe a largura da parede: '))
altura = float(input('Informa a altura: '))
area = largura * altura
tinta = area/2
print('A sua parede é {}x{} e sua área é de {}m²'.format(largura, altura, area))
print('Você precisará de {}L para ´pintar a parede'.format(tinta))

#DESAFIO 12
preco = float(input("Informe o preço do produto: "))
desconto = preco*0.95
print("O preço do produto com desconto é igual a {:.2f} R$".format(desconto))

#DESAFIO 13
salário = float(input("Qual o seu salário?: "))
acréscimo = salário*1.15
print("Com 15% de aumento, você receberia {:.2f} R$ de salário".format(acréscimo))

#DESAFIO 14
C =float(input("Qual a temperatura em graus °C?: "))
F = 9*C /5 +32
print("A temperatura {} °C em Fahrenheit equivale a {} °F".format(C, F))

#DESAFIO 15
dias = int(input("Informe os dias: "))
KM = int(input("Informe o KM rodado: "))
Vt = (60*dias)+(KM*0.15)
print("Você pagará {}R$ de aluguel".format(Vt))






