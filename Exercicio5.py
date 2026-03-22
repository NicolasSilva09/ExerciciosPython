Nome=str(input("Digite o Nome do Jogador: "))
S_antigo=float(input("Digite o Salario atual do Jogador: R$"))

if S_antigo <= 1000.00:
    Aumento = S_antigo * 0.20

elif S_antigo<=5000:
    Aumento=S_antigo*0.10

else:
    Aumento=S_antigo*0.05

S_novo=Aumento+S_antigo

print("Jogador: ",Nome)
print("Salario Antigo: R$",S_antigo)
print("Novo Salario: R$",S_novo)