salario = float(input('Qual é o salario do funcinário? R$ '))

aumento = salario + (salario * 15 /100)

print('Um funcionário que ganhava R${:.2f} hoje passou a ganhar R${:.2f}, ele obteve 15% de aumento'.format(salario, aumento))

