idade_gatos = {"miau":2, "princesa":5, "benjamim":1, "ana vitoria":1, "valentina":1}
dados = idade_gatos.values()
texto = []
for valor in dados:
    texto.append(valor)
#arquivo = open(".vscode\\gatosIdades.txt",'w')
#arquivo.write(str(texto))

with open("C:\\Users\\beatr\\OneDrive\\Desktop\\python project 1\\.vscode\\gatosIdades.txt", 'r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write("\namo meus gatos")    