#Cadastro em python

nome = str(input('>> Digite seu Nome: '))
email = str(input('>> Digite seu Email: '))
senha = str(input('>> Digite sua Senha: '))

print(f'Cadastro do usuário {nome}, de email {email} e senha {senha} realizado com sucesso')

print('>> Faça login: ')

confNome = str(input('>> Confirme seu Nome: '))
confEmail = str(input('>> Confirme seu email: '))
confSenha = str(input('>> Confirme sua senha:'))

if(confNome == nome and confEmail == email and confSenha == senha):
    print('Login realizado com sucesso!!')
else:
    print('Insira seus dados corretamente!')