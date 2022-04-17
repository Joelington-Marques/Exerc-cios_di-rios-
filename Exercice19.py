import random

first = (input('Primeito aluno '))
second = (input('Segundo aluno '))
third = (input('Terceiro aluno '))
forth = (input('Quarto aluno '))

pessoas = [first,second,third,forth]
sorteado = random.choice(pessoas)

print('O aluno escolhido foi {}'.format(sorteado))