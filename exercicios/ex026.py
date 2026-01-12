frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('letra A aparece a primeira vez na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A aparece a ultima posicao {}'.format(frase.rfind('A')+1))

