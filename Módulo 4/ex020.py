n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")  
n4 = input("Digite o nome do quarto aluno: ")
alunos = [n1, n2, n3, n4]
from random import choice
sorteado = choice(alunos)
print("O aluno sorteado foi {}".format(sorteado))