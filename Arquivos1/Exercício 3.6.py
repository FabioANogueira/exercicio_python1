materia1 = float(input('Digite a nota da primeira materia: '))
materia2 = float(input('Digite a nota da segunda materia: '))
materia3 = float(input('Digite a nota da terceira materia: '))
media = (materia1 * materia2 * materia3) / 3
if media >= 7:
    print('Parabéns, você foi aprovado')
else:
    print('Que Pena, você foi reprovado')