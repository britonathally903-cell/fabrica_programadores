#autor: Náthally brito
#projeto: Desvio condiconal 

#criação de variaveis
 nome= input("digite o seu nome;")
 peso = float(input("digite o seu peso:"))
 altura = input(input("digite sua altura:"))
imc = peso / (altura**2)
print(f"\nSeu IMC é:{imc:.2f}")

if imc <18.5:
    print("abaixo do peso")
