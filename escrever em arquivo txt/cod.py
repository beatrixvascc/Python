texto = "mas eh caro"
arquivo = open("arquivo\\arq.txt", 'a+')
arquivo.write(texto)
leitura = arquivo.read()
print(leitura)

