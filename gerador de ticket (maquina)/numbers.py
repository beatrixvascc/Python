def perfume_generator():
    for num in range(1,1000):
        yield f"P-{num}"
    
def cosmetic_generator():
    for num in range(1,1000):
        yield f"C-{num}"
        
def medicine_generator():       
    for num in range(1,1000):
        yield f"M-{num}"
        

p=perfume_generator()
m=medicine_generator()
c=cosmetic_generator()


def function(answer):
    if answer=="P":
        print(next(p))
    elif answer=="M":
        print(next(m))
    elif answer=="C":
        print(next(c)) 
    print("please wait for your ticket")     
             
