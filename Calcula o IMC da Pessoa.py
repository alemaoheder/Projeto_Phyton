#Calcula o IMC da Pessoa, após inserir peso, altura.
altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em Kg: '))

IMC = peso/ (altura/100)**2
print (IMC)

if IMC < 18.5:
    print(f'Seu IMC é de {IMC}, e é classificado como Magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de {IMC}, e é classificado como Normal')

elif IMC >= 25 and IMC < 29.9:
    print(f'Seu IMC é de {IMC}, e é classificado como Sobrepeso')

elif IMC >= 30 and IMC < 39.9:
    print(f'Seu IMC é de {IMC}, e é classificado como Obesidade')

else:
    print (f'Seu IMC é de {IMC}, Consulte seu médico, pare de comer e faça exercicio, sua classificação é Obesidade GRAVE!')