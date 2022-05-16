print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Analisador de Triâgulos')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < c + a and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMA um triângulo')
