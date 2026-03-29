peso=float(input("Digite o seu peso: "))
altura=float(input("Digite a sua altura: "))

imc =  peso/(altura*altura)

if imc<18.5:
    print("Seu imc é:", round(imc,2))
    print("Você esta abaixo do peso normal")
elif imc >=18.5 and imc<=24.9:
    print("Seu imc é:",round(imc,2))
    print("Você esta no peso normal")
elif imc>=25 and imc<=29.9:
    print("Seu imc é:",round(imc,2))
    print("Você esta com excesso de peso")
elif imc>=30 and imc<=34.9:
    print("Seu imc é:",round(imc,2))
    print("Você esta na obesidade classe1 ")
elif imc>=35 and imc<=39.9:
    print("Seu imc é:",round(imc,2))
    print("Você esta na obesidade classe2 ")
else:
    print("Seu imc é:",round(imc,2))
    print("Você esta na obesidade classe3 ")