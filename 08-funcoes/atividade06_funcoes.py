#Autor: Náthally Brito
#projeto 4 operaçoes

#entrada de dados 

valor1 = float(input("Digite o segundo valor:"))
valor2 = float(input("Digite o segundo valor:"))

 #função calcular
 def calcular (valor1,valor2):
    somar = valor1+valor2
    subtrair = valor1-valor2
    multiplicar = valor1*valor2
    dividir = valor/valor2

   #imprimindo os resultados
   print(f"o resultado da soma é: {soma}")
   print(f"o resultado da subtração é: {subtrair}")
   print(f"o resultado da Multiplicação é: {multiplicar}")
   print(f"o resultado da dvisão é: {dividir}")

#chamada da função 
calcular(valor1,valor2)
