preco = float(input('Qual é o preço do produto? R$'))

desconto = preco - (preco * 5 /100)

print('O produto que custava R$ {:..2f}, na promoção com desconto 5%, agora vai custar R${:.2f}'.format(preco, desconto))
