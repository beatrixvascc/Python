import PySimpleGUI as sg    #parte 1 - importando pysimpleGUI

layout = [                  #parte 2 - criando o formato 
      [sg.Text("Usuario")],
      [sg.Input(key="usuario")],
      [sg.Text("Senha")],
      [sg.Input(key="senha")],
      [sg.Button("Login"),sg.Button("Sair")],
      [sg.Text("",key="mensagem")],
]
window = sg.Window('Login',layout=layout)   #parte 3 - nome da tela

while True:     #parte 4 - interagir com a janela
    event,values=window.read()
    if event==sg.WINDOW_CLOSED or event=="Sair":    #parte 5 - interromper se clicar no botao de sair ou fechar a janela
        break
    elif event=="Login":
        correct_password="123456"
        correct_user="beatriz"
        usuario=values["usuario"]
        senha=values["senha"]
        if correct_password==senha and correct_user==usuario:  #parte 6 - verificando os dados
            window["mensagem"].update("Login concluido")
        else:
            window["mensagem"].update("senha ou usuario incorreto")    
