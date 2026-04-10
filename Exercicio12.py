i = 0
soma = 0.0

while True:
    n = float(input("digite a nota (-1 para sair): "))

    if n == -1:
        break

    if n > 10:
        print("erro: nota maior que 10")
        continue

    if i == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    soma += n
    i += 1

if i > 0:
    media = soma / i
    print("Média:", media)
    print("Maior:", maior)
    print("Menor:", menor)
else:
    print("Nenhuma nota informada")