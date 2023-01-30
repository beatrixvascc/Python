#Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
#os valores comuns às duas listas
#os valores que só existem na primeira
#os valores que existem apenas na segunda
#uma lista com os elementos não repetidos das duas listas.
#a primeira lista sem os elementos repetidos na segunda

L1 = []
L2 = []
while True:
    num = int(input('qual num? '))
    if num == 0:
        break
    L1.append(num)
while True:
    num = int(input('qual num? '))  
    if num == 0:
        break
    L2.append(num)  

print(f"Lista 1: {L1}")
print(f"Lista 2: {L2}")

conjunto_1 = set(L1)
conjunto_2 = set(L2)

print("Valores comuns às duas listas:", conjunto_1 & conjunto_2)
print("Valores que só existem na primeira:", conjunto_1 - conjunto_2)
print("Valores que só existem na segunda:", conjunto_2 - conjunto_1)

# Conjuntos suportam o operador ^ que realiza a subtração simétrica.
# A ^ B resulta nos elementos de A não presentes em B unidos
# com os elementos de B não presentes em A
# A ^ B = A - B | B - A
print("Elementos não repetidos nas duas listas:", conjunto_1 ^ conjunto_2)