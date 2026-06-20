 # Autor: Náthally Brito

#PROJETO: definião das variaveis 

nome = input("digite seu nome")
nota = float(input("Digite sua nota "))

# função status do aluno
def status (nota):
    if nota >= 6:
        print("aluno Aprovado!")
    else:
            print("Aluno reprovado!")
# chamada da função
status (nota)            