#Faça um programa que leia duas listas e que 
#gere uma terceira com os elementos das duas primeiras.

lista1 = []
lista2 = []
while True:
    num = int(input('diga um num: '))
    if num == 0:
        break
    lista1.append(num)
while True:
    num = int(input('diga o numero: '))
    if num == 0:
        break
    lista2.append(num)
lista3 = lista1[:]    #copia os elementos da lista1
lista3.extend(lista2)  #adiciona a lista2 no fim
print(lista3)