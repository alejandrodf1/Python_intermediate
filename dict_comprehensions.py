# sentence = "is2 Thi1s T4est 3a" #forma para ordenar frases 

# words = [(int(l), w) for w in sentence.split() for l in w if l.isdigit()]
# print(words)
# words.sort(key=lambda j: j[0])
# result = ' '.join(i[1] for i in words)
# print(result)

def run():
    # my_dict = {}  ## Una forma de iterar y guardar cosas en un diccionario

    # for i in range(1, 101):    ##iteracion para ir guardan llaves y values
    #     my_dict[i] = i**3
    
    ##Guardemos los numero no divisibles para 3

    # my_dict = {}  

    # for i in range(1, 101):
    #     if i%3 != 0:
    #          my_dict[i] = i**3


    dicci = {i:i**3 for i in range(1,101) if i%3 != 0}  ##forma eficiente de hacer lo de arriba
    print(dicci)         

    my_dict = {i:i**0.5 for i in range(1, 1001)}
    print(my_dict)



if __name__ == '__main__':
    run()