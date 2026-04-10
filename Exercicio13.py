quantidade = 0
maiores = 0

while True:
    nome = input("Digite o nome (ou 'encerrar' para sair): ")

    if nome == "encerrar":
        break

    idade = int(input("Digite a idade: "))

    quantidade += 1

    if idade >= 18:
        maiores += 1

print("Quantidade de usuários cadastrados:", quantidade)
print("Maiores de idade:", maiores)