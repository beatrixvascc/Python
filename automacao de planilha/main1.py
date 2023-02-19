import openpyxl
 
planilha = openpyxl.Workbook()   #parte 1 - criar uma planilha

planilha.create_sheet("Clientes")   #parte 2 - criar pagina 

dashboard = planilha["Clientes"]    #parte 3 - escolher pagina

dashboard.append(["cliente","quantidade","status"])  #parte 4 - estabelecer as categorias e preencher as celulas
dashboard.append(["atacadao","60","venda feita"])
dashboard.append(["cometa","70","venda feita"])
dashboard.append(["atacadista","40","analise"])
dashboard.append(["carrefur","",""])

planilha.save("Planilha de clientes.xlsx")   #parte 5 - salvar como excel
