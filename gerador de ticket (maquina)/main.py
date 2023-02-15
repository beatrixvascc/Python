import numbers


def question():
    print('welcome!!')
    while True:
       print("[P] perfume - [M] medicine -  [C] cosmetics")
       try:
           print("which product do you want?[P][M][C] ")
           answer=input().upper()
       except ValueError:
           print("invalid option")    
       else:
           break   
       
    numbers.function(answer)
    
def start():
        
    while True:
        question()
        try:
            print("do you want another ticket?[Y][N] ")
            answer=input().upper()
        except ValueError:
            print("invalid option")
        else:   
            if answer=="N":
                break 
            
start()                  
       
    