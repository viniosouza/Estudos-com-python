larg = float(input('Insira a largura da sua parede (metros):'))
alt = float(input('Insira a altura da sua parede (metros): '))

area = larg * alt

print('Sua parede tem a dimensão de {} x {} e sua area é de {}m²'.format(larg, alt, area))

tinta = area / 2

print('Para pintar a sua parede você precisará {}L de tinta'.format(tinta))