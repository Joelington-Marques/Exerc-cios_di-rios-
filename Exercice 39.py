ano = int(input(' Ano de nascimento: '))

anos = 2022 - ano
alis = ano + 18
faltam = alis - 2022

print('Quem nasceu  em {} tem {} anos em 2022'.format(alis,anos))

if alis > 2022:
        print('Ainda faltam {} anos para o alistamento'.format(faltam))
        print('Seu alistamento será em {}'.format(alis))
else:
    print('Seu alistamento foi em {}'.format(alis))
    print('Voce deve se alistar imdediatamente')