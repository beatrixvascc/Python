resultados = []
with open(".\\.vscode\\cadastro.csv",'r') as arquivoEntrada:
    linhas = arquivoEntrada.readlines()[1:]   #retorna cada linha sem precisar de for
    for linha in linhas:
        dados = linha.split(",")
        comando = dados[3].replace("\n","")
        resultados.append(f'{dados[1]} {dados[2]} {comando}\n')   #tira o indice antes do nome
    
with open(".\\.vscode\\cadastroSaida.csv",'w') as arquivoSaida:
    for resultado in resultados:
        arquivoSaida.write(resultado)

