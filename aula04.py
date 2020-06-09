"""
nome = "Luiz"
print("Nome:")

print( type(nome) ) #str - string - texto

#Mudando o valor, mudamos o tipo também
nome = 17

print("Novo valor de nome")
print( type(nome) ) #Nome agora virou inteiro

#Forçando a mudança de tipo

print("Transformando em string")
nome = str(nome) #Transformando em string
print(type(nome))

#Podemos fazer a transformação de qualquer tipo

valor = "17" #Aqui é String
valor = int(valor) #Aqui virou inteiro

"""
#Tudo que está entre """ virou comentário igual esse

#input - Entrada de dados

#entrada
nome = str(input("Digite seu nome: ")) #Transformando em str como padrão
idade = int(input("Digite sua idade: ")) #Transformando em inteiro

#saida
print(nome)
print(idade)


