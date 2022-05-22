from datetime import date
ano = int(input('Qual o ano de nascimento do atleta: '))

anoatual = date.today().year
idade = anoatual - ano

if idade <= 9:
    print('O atleta é MIRIM')
elif idade > 9 and idade <= 14:
    print('O atleta é INFANTIL')
elif idade > 14 and idade <= 19:
    print('O atleta é Junior')
elif idade > 19 and idade <= 25:
    print('O atleta é Senior')
else:
    ('O atleta é Master')