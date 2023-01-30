cadastros = ["bea,21,estagio","adriano,30"]   
def mostraDados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(',')
        if len(dados) != 3:
            raise ValueError("erro na quantidade de dados!")
        nome = dados[0] 
        idade = int(dados[1])
        cargo = dados[2] 
        print(f"a pessoa {nome} tem {idade} anos e exerce a profissao {cargo}")

try:
    mostraDados(cadastros)
except ValueError as excecao:
    print(f"o erro esta em {excecao}")