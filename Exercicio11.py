senha_correta="12345"
tentativas=0

while tentativas<3:
    senha=input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        tentativas +=1
        print("Senha incorreta")

if tentativas==3:
    print("Conta bloqueada")