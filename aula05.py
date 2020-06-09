#Concatenação simples!

"""
#Usamos o + para concatenar string ou texto
print("Nome" + " outro nome")

#nome = "Luiz" #String
print("Meu nome é: "+nome) #Podemos fazer assim a concatenação

nome = str(input("Digite seu nome: ")) #Pegamos o nome
print("Seu nome é: "+nome) #Mostramos o nome concatenado

#Usamos , para concatenar texto com inteiro/número

idade = int(input("Digite sua idade: ")) #Pegamos o número
print("Sua idade é: ", idade) #Mostramos ele com a mensagem
"""

#Concatenação com format

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
#Onde tem {} será substituido pela variável
print("Seu nome é {0} e você tem {1} anos".format(nome, idade)) 



