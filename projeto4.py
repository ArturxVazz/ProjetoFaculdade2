nome = input ("qual seu nome?")  
altura =float(input("quanto de altura?"))
peso = float (input ("qual seu peso?") )

imc = peso / (altura * altura ) 
imc_arredondado = round(imc, 2) 
print("Olá " + str(nome) + ", seu IMC é: " + str(imc_arredondado))
