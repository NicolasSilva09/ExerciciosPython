n1 = int(input("Digite sua nota1: "))
n2 = int(input("Digite sua nota2: "))
n3 = int(input("Digite sua nota3: "))
mencao = (n1+n2+n3) /3

if mencao >=8:
    print("Sua media final: ",round(mencao,2))
    print("Seu conceito:A")
elif mencao >=5:
    print("Sua media final: ",round(mencao,2))
    print("Seu conceito:b")
else:
    print("Sua media final: ",round(mencao,2))
    print("Seu conceito:c")