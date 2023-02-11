from random import choice

words = ["potter","granger","riddle"]
correct_letter=[]
incorrect_letter=[]
tries=6
game_over=False
match=0

def choose_word(words): ##escolhe a palavra com choice
    choose=choice(words)
    letter_without_repetition=len(set(choose))
    return choose,letter_without_repetition ##retorna a palavra e a quantidade de letras sem repeticao

def option(): ##escolhe as letras
    
    valid=False
    letter=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    while not valid:
       letter=input("choose a letter: ")
       if letter in alphabet and len(letter)==1:
           valid=True
       else:
           print("the letter doens't exist")     
    return letter    
 
def showing(choose): ##coloca as tentativas certas
    word_list=[]
    for l in choose:
        if l in correct_letter:
            word_list.append(l)
        else:
            word_list.append('-')    
    print(' '.join(word_list))     
    
def checking(letter,word_list,tries,match): ##verifica se acertou 
    end=False
    if letter in word_list and letter not in correct_letter:
        correct_letter.append(letter)
        match+=1
    elif letter in word_list and letter in correct_letter:
        print("you've already add this letter")   
    else:
        incorrect_letter.append(letter)    
        tries-=1
    if tries==0:
        end=lose() 
    elif match==letter_without_repetition:
        end = win(word_list)    
    return end,tries,match      

def lose():
    print(f"you're lose the game and the hidden word is {choose}")
    return True

def win(choose):
    showing(choose)
    print("you win")
    return True

choose,letter_without_repetition=choose_word(words)

while not game_over:
    print("\n"+"-"*20+"\n")
    showing(choose)
    print(f"tries: {tries}\n")
    print(f"incorrect letters: {incorrect_letter}\n")
    print("\n"+"-"*20+"\n")
    letter=option()
    over,tries,match=checking(letter,choose,tries,match)
    game_over=over
    
           
            
