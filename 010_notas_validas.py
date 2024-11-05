while True:
    nota_aluno = int(input('Digite uma nota válida entre 0 e 10: '))
    if nota_aluno >= 0 and nota_aluno <= 10:
        print(f'A nota foi armazenada com sucesso {nota_aluno}')
        break
    else:
        nota_aluno = int(input('Digite uma nota válida entre 0 e 10: '))