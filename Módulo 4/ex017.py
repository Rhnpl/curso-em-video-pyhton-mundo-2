from math import hypot

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hi = hypot(co, ca)
print('A hipotenusa é de {:.2f}'.format(hi))