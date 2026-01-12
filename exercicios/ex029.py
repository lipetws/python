velocidade = float(input('qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado!voce excedeu o limite permitido')
    multa = (velocidade - 80) * 7
    print('sua multa foi de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija em seguranca!')



