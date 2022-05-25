peso = float(input('Qual é o seu peso ? '))
altura = float(input('Qual a sua altura ? '))

imc = peso / (altura ** altura)

print('Seu IMC é de {:.2f}'.format(imc))

if imc <= 18.5:
    print(' Atenção você está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print(' Parabéns voçê está no peso ideal')
elif imc > 25 and imc <= 30:
    print(' Você está com sobrepeso')
elif imc > 30 and imc <= 40:
    print('Você está obeso')
else:
    print ('Muito cuidado você está com obesidade morbida')

