preco = float(input('qual e o preco do produto? R$'))
novo = preco - (preco * 5/100)
print('O produto que custava R${:.2f}, na promocao vai custar R${:.2f}'.format(preco, novo))
