dias = int(input('Quantos dias você gostaria de alugar o carro? '))
km = float(input('Quantos KM o carro vai rodar? '))

diaria = dias * 60
percursoRodado = km * 0.15

pago = diaria + percursoRodado

print('O total a pagar é de R${:.2f}'.format(diaria))
