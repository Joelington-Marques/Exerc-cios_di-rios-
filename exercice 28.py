from random import randint
from time import sleep
adv = randint(0,5)

print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')

num = int(input('Em qual numero eu pensei? '))


print('PROCESSANDO...')
sleep(3)
if num == adv:
    print('Você ganhou, parabéns...')

else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(adv,num))