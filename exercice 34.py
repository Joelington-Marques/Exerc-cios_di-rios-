sal = float(input('Qual é o salario do funcionário? R$'))

if sal > 1250:
    salnovo = sal * 1.10
    print ('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal,salnovo))
else:
    salnovo = sal * 1.15
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal,salnovo))