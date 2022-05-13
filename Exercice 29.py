vel = int(input('Qual é a velocidade atual do carro? '))
multa = (vel - 80) * 7

if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')

else:
    print('MULTADO! Voçê excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${}!'.format(multa))
