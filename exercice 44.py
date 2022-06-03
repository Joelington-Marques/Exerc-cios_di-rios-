print('========== LOJAS JOJO ==========')
preco = float(input('Preco das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
pgto = int(input('Qual é a opção? '))

if pgto == 1:
    V1 = preco * 0.90
    print('O valor da sua compra será de R$ {:.2f}'.format(V1))
elif pgto == 2:
    V2 = preco * 0.95
    print('O valor da sua compra será de R$ {:.2f}'.format(V2))
elif pgto == 3:
    V3 = preco / 2
    print(' O valor da sua compra será de R$ {:.2f} pago em duas vezes de R${:.2f}'.format(preco,V3))
elif pgto == 4:
    V4 = preco * 1.2
    print(' O valor da sua compra será de R$ {:.2f}'.format(V4))
