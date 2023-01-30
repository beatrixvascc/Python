import string
import random
senha = []
tamanho = int(input("qual o tamanho da senha? "))
for caractere in range(0, tamanho):
    senha.append(random.choice(string.ascii_letters))
print("".join(senha))