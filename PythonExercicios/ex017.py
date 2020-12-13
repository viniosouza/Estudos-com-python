from math import hypot
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto adjacente: '))

# hip = (co ** 2 + ca ** 2) ** (1/2)
# Jeito antigo sem importação

hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))

