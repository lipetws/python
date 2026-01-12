n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
soma = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e{},\n o produto e {} e a \n divisao e {:.3f}'.format(soma, m, d),end='')
print('divisia inteira {} e potencia {}'.format(di, e))