from math import radians, sin, cos, tan

ang = float(input('Digite o angulo que voce deseja: '))

cos = cos(radians(ang))
sen = sin(radians(ang))
tan = tan(radians(ang))


print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tan))
