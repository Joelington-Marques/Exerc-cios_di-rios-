import string

name = str(input('Digite seu nome completo:').strip())

name2 = name.upper()
name3 = name.lower()
quant = (len(name) - name.count(' '))
print('Analisando seu nome ...')
print('Seu nome em maiúsculas é:',name2)
print('Seu nome em minúsculas é:',name3)
print('Seu nome ao todo {} letras'.format(quant))
separa = name.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))