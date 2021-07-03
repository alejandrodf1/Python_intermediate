import os
import random

def read():         ##esta funcion lee y limpia los datos
    with open('./data.txt','r', encoding='utf-8') as words:
        my_words = {(int(i) + 1):j.replace('\n', '') for i,j in list(enumerate(words))}
        my_words = {i:j.replace('á', 'a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u') for i,j in my_words.items()}
        
         #for i,j in my_words.items():    #no necesario
          #   my_words[i] = j.replace('\n', '')
       

    secrete_word = my_words[random.randint(1, len(my_words))]  ##sacamos la palabra aleatoria
    #secrete_word = list(word)
    return secrete_word

def interfaz(secrete_word):
    length = len(secrete_word)
    line = ['-' for i in secrete_word]
    line = ''.join(line)
    return line



def game(secrete_word):  ##funcion que escoge una palabra aleatoria
    gess_ones = list('-'*len(secrete_word))
    print(gess_ones)
    secrete_word = list(secrete_word)
    interfaz(secrete_word)
    print('Pista la palabra es de: '+ str(len(secrete_word)) +' letras')
    while gess_ones != secrete_word:
        user_word = input('Escriba una letra: ')
        os.system('clear')
        assert len(user_word) == 1 and user_word.isnumeric() == False , 'Solo agregar una letra, intenta de nuevo!!'
        for i in range(0, len(secrete_word)):
            if secrete_word[i] == user_word:
                gess_ones[i]=secrete_word[i]
        #adivinadas=[gess_ones.append(i) for i in secrete_word if i == user_word]
        print(gess_ones)
    return print('Ganaste felicidades!!!')
        
    



def run():
    print('Adivina la Palabra!')
    read()
    game(read())
 
    


if __name__ == '__main__': 
    run()