import PySimpleGUI as sg    #parte 1 - importar pysimpleGUI

def create():     #parte 2 - funcao que cria uma janela inicial
    sg.theme("LightGreen5")
    linha = [
        [sg.Checkbox(''),sg.Input('')]
            ]
    layout=[
        [sg.Frame("To Do",layout=linha,key="bloco")],    #nesse frame vai usar a linha de modelo
        [sg.Button("Add new task"),sg.Button("Reset")]
    ]        
    return sg.Window("TO DO LIST",layout=layout,finalize=True)  #precisa usar finalize quando cria funcao


app = create()    #parte 3 - cria a janela padrao

while True:
    event,values=app.read()   
    if event==sg.WIN_CLOSED:
        break
    elif event=="Add new task":   #parte 4 - se clicar no botao adiciona mais uma linha com checkbox na parte do frame
        app.extend_layout(app["bloco"], [[sg.Checkbox(''),sg.Input('')]])
    elif event=="Reset":
        app.close()     
        app = create()    
