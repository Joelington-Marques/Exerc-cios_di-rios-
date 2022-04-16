carteira = float(input('Quanto dinheiro você tem na carteira ? R$:'))

conversao = carteira / 4.70

print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira,conversao))
