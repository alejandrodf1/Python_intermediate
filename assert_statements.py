def divisiors(number):
    divisior = [i for i in range(1, number+1) if number%i == 0]
    return divisior

   


def run():
    number = input('Ingresa un numero: ')
    assert number.isnumeric() and number > 0, 'Debes ingresar un numero entero positivo'
    print(divisiors(int(number)))
    print('termino programa')
    
if __name__ == '__main__':
    run()