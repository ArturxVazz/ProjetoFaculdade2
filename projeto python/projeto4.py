ano = int(input("insira quantos anos você tem?"))
meses = int(input("insira quantos meses você tem?"))
dias = int(input("insira quantos dias você tem?")) 

resultado = ano * 360
resultado2 = meses * 30 + resultado
resultado3 = resultado2 + dias 

print (resultado3)