def fazDivisao(dividendo, divisor):
    return dividendo/divisor

try:
    num1 = int(input("diga um num: "))
    num2 = int(input("diga outro num: "))
    resp = fazDivisao(num1, num2)
except ZeroDivisionError:
    print("nao pode dividir po zero. mude o divisor")   
except TypeError:
    print("revise os tipos das variaveis. ocorreu um erro")     
else:
    print(resp)    
finally:
    print("finalizando programa...")  