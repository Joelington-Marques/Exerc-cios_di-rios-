first = int(input('Primeiro valor:'))
second = int(input('Segundo valor:'))
third = int(input('Terceiro valor:'))

if first <= second and first <= third:
    print('O menor valor digitado foi {}'.format(first))
if second <= first and second <= third:
    print('O menor valor digitado foi {}'.format(second))
if third <= second and third <= first:
    print('O menor valor digitado foi {}'.format(third))
if first >= second and first >= third:
    print('O maior valor digitado foi {}'.format(first))
if second >= first and second >= third:
    print('O maior valor difitado foi {}'.format(second))
if third >= second and third >= first:
    print('O maior valor digitado foi {}'.format(third))
