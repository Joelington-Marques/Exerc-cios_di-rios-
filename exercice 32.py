from datetime import date
ano = int(input('Digite o ano em que estamos: Coloque 0 para pegar o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O {} é Bissexto'.format(ano))
else:
    print('o ano não é bissexto')