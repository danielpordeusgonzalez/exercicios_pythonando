numero1 = int(input('digite o primeiro número: '))
numero2 = int(input('digite o segundo número: '))
numero3 = int(input('digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O número {numero1} é maior que {numero2}, {numero3}.')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O número {numero2} é maior que {numero1}, {numero3}.')
elif numero3 > numero1 and numero3 > numero2:
    print(f'O número {numero3} é maior que {numero1}, {numero2}.')
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print(f'existe no minimo dois numeros iguais e são {numero1} e {numero2} ou {numero2} e {numero3}')