
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < c + a and c < a + b:
    if a == b == c:
        print('Os segmentos formaram um triângulo Equilatero')
    elif a != b and a != c and b != c:
        print('Os segmentos formaram um triangulo Escaleno')
    else:
        print('Os segmentos formaram um triângulo Isoceles')

else:
    print('Os segmentos acima NÃO PODEM FORMA um triângulo')


