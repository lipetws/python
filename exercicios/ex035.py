print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
r1 = float(input('primeiro valor: '))
r2 = float(input('segundo valor: '))
r3 = float(input('terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses valores podem formar um triangulo')
else:
    print('Esses valores nao podem formar um triangulo')