dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

aluguel = (dias * 100) + ( km * 0.10 )

print('O total a pagar é de R${}'.format(aluguel))