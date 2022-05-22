n1 = float(input(' Qual foi a sua primeira nota? '))
n2 = float(input(' Qual foi a sua segunda nota? '))

media = (n1+n2)/2

if media >= 7.0:
    print('Aprovado')
elif media >= 5.0 and media < 7.0:
    print('Recuperação')
else:
    print('Reprovado')


