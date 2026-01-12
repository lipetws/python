
salario = float(input('Qual e o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('seu novo salario e R${:.2f}'.format(novo))

