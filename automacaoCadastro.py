import pyautogui
from time import sleep ##estou fazendo isso pro programa nao travar

pyautogui.click(1133,753,duration=2) ##coloca a coordenada do usuario e os segundos pra fazer isso
pyautogui.write("usuario")
pyautogui.click(1136,807,duration=2) ##coordenada da senha
pyautogui.write("senha")
pyautogui.click(940,849,duration=2) ##coordenada do botao entrar

with open("C:\\Users\\beatr\\Downloads\\produtos.txt","r") as arquivo:   ##produto.txt e meu arquivo cm dados
    for linha in arquivo:
        produto = linha.split(",")[0]
        quantidade = linha.split(",")[1]
        preco = linha.split(",")[2]
        pyautogui.click(570,729,duration=2)
        pyautogui.write(produto)
        pyautogui.click(567,780,duration=2)
        pyautogui.write(quantidade)
        pyautogui.click(562,832,duration=2)
        pyautogui.write(preco)
        pyautogui.click(386,1131,duration=1)
        sleep(1)  ##para o codigo nao funcionar na velocidade da luz
