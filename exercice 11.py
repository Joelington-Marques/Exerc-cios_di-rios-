largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))

area = largura * altura
rendimento = area/2

print('Sua parede tem a dimensao de {}x{} e sua área é de {}m².'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(rendimento))