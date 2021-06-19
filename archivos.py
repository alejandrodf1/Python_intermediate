def read():
    number = []
    with open('./archivos/number.txt', 'r', encoding='utf-8') as data:  ##abrimos un archivo
        for line in data:                                  ##con este for leemos lo que hay y lo guaradamos en una lista
            number.append(int(line))
    print(number)

def write():         ##funcion para escribir un nuevo archivo
    names = ['sebastian', 'Facundo', 'sofia', 'fernanda']  ##lo que queremos poner en el arhivo 
    with open('./archivos/names.txt', 'a', encoding='utf-8') as data:  ##asi creamos un archivo nuevo
        for name in names: ##funcion para sorbreescrbiir el nuevo archivo
            data.write(name)
            data.write('\n') #da un salto de linea


def run():
    write()

if __name__ == '__main__':
    run()