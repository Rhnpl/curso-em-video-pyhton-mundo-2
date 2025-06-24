import math
angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
consseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno é de {:.2f}\nO cosseno é de {:.2f}\nA tangente é de {:.2f}'.format(seno, consseno, tangente))