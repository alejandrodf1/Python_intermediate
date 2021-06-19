def divisiors(number):
    try:
        if number < 0:
            raise ValueError ('Debes ingresar numeros enteros positivos')
        divisior = [i for i in range(1, number+1) if number%i == 0]
        return divisior
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        number = int(input('Ingresa un numero: '))
        print(divisiors(number))
        print('termino programa')
    except ValueError: 
        print('Debes ingresar un numero')
if __name__ == '__main__':
    run()