
#autor: Náthally brito
#projeto: Desvio condiconal 

# DECLARAÇÃO DE VARIAVEIS
 
peso = float(input("digite o seu peso:"))
altura = float(input("digite sua altura:"))

def calcular (peso,altura):
    imc= peso / (altura * altura)
    print (f" seu imc é: {imc:.2f}")

  #chamada da função
calcular(peso,altura)
