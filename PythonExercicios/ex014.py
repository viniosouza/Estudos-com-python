c = float(input('Informe a temperatura em ºC: '))

f = (c * 9/5) + 32
k = c + 273.15

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(c, f))
print('A temperatura de {:.1f}ºC corresponde a {:.2f}K'.format(c,k))


