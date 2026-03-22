IDvendedor= int(input("Digite o id da vendedor:"))
IDpeca=int(input("Digite o id da peça:"))
PrecoUni= float(input("Digite o preço unitario da peça:R$"))
quant= int(input("Digite a quantidade de peças:"))

total = quant * PrecoUni
comissao = total * 0.05

print("O Vendedor: ",IDvendedor)
print("Peça",IDpeca)
print("Quantidade vendida: ",quant)
print("Preço unitario: R$",PrecoUni)
print("Total da Venda: R$",total)
print("Tendo uma comissão de: R$",comissao)
