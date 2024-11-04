nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
nota4 = float(input('digite a quarta nota: '))


media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'você foi aprovado e ficou com a média de {media}')
elif media >= 4:
    print(f'você está de recuperação e ficou com a média de {media}')
else: 
    print(f'você foi reprovado com a média {media}')