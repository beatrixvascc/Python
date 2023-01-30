#Escreva um programa que gere um dicionário, em que cada chave seja um caractere,
#e seu valor seja o número desse caractere encontrado em uma frase lida.

dic = {}
frase = input('digite uma frase: ')
for letra in frase:
    if letra not in dic:
        dic[letra] = 1
print(dic)