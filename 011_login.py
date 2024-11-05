user = str(input('Digite um usuario para ser armazenado: '))
senha = str(input('digite uma senha para ser armazenada : '))

while True:
    login_user = str(input('Qual é seu User: '))
    login_senha = str(input('Qual é sua senha: '))
    if login_user == user and login_senha == senha:
        print(f'olá {user}, voce entrou com sucesso')
        break
    else:
        print('Voce errou seu user ou senha, por favor tente novamente')