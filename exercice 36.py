casa = float(input('Valor da casa: R$'))
sal = float(input('Salario do comprador:R$'))
anos = float(input('Quantos anos de financiamento?'))

parcela = casa / (anos/12)

print('Para pagar uma case de {:.2f} em {:.2f} anos a prestação sera de {:.2f}'.format(casa,anos,parcela))

if sal*0.30 <= parcela:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo sera concedido')
