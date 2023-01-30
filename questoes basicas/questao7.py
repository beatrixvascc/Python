#Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns
# às duas strings lidas.
#1ª string: AAACTBF
#2ª string: CBT
#Resultado: CBT
#A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras 
#comuns a ambas.


L1 = (input('digite uma string: '))
L2 = (input('digite uma string: '))
L3=''
for i in L1:
    if i in L2 and i not in L3:
        L3 += i
print(L3)