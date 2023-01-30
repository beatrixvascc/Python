import csv

with open("C:\\Users\\beatr\\OneDrive\\Desktop\\python project 1\\.vscode\\gatos.csv", 'r') as arquivo:
    for linha in arquivo:
        lista = linha.split(',')
        print(lista[0],lista[1],lista[2],lista[3])