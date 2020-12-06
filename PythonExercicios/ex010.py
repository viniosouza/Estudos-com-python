moeda = float(input('Quanto de dinheiro eu tenho na carteira? '))
dolar = moeda / 5.23
euro = moeda / 6.31
dolar_canada = moeda / 4.04
libra = moeda / 6.97
print('-'*30)
print('R$ {:.1f} em dolar é ${:.2f}'.format(moeda, dolar))
print('R$ {:.1f} em euro é {:.2f} USD'.format(moeda, euro))
print('R$ {:.1f} em dolar canadenese é  ${:.2f}'.format(moeda, dolar_canada))
print('R$ {:.1f} em libra esterlina é {:.2f} GBD'.format(moeda, libra))


