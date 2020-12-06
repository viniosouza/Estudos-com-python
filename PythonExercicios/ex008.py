medida = float(input('Insira uma distância em metros: '))

cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
pol = medida * 39.37
pe = medida * 3.281
mil = medida / 1609
jard = medida * 1.094

print('A médida de {}m corresponde a'.format(medida))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
print('{:.0f}dm'.format(dm))
print('{:.3f}hm'.format(hm))
print('{}km'.format(km))
print('{} polegadas'.format(pol))
print('{} pés'.format(pe))
print('{:.5f} Milhas'.format(mil))
print('{} Jardas'.format(jard))
