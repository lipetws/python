from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print('--------------------')
print('Vou pensar ewm um numero entra 0 e 5. tente adivinhar..')
print('--------------------')
jogador = int(input('em que numero pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('Parabens voce conseguiu me vencer!')
else:
    print('voce foi brutalmente derrotado, pensei no numero {} e nao no {}!'.format(computador, jogador))


