dist =float(input('Qual a distancia da sua viagem?'))
print('Voce está prestes a comecar uma viagem de {}'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))

