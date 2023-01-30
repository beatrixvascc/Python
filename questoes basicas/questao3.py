#Imprima o menor elemento da lista

lista = []
while True:
    num = int(input('digite um numero: '))
    if num == 0:
        break
    lista.append(num)
min = min(lista)   
print(min)