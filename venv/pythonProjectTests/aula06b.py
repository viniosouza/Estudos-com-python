# mostrando o tipo de variável

# int() float() bool() e str().

n = str(input('Digite um valor: '))

print('É número ?', n.isnumeric())

print('É alfanúmero? ', n.isalpha())

print('É alfabético e númerico ', n.isalnum())

#Está somento com letras maiuscula
print('Letra maiuscula', n.isupper())

