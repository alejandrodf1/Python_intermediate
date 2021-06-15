def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Alejandro', 'lastname': 'Delgado'}

    super_list = [
        {'firstname': 'Alejandro', 'lastname': 'Delgado'},
        {'firstname': 'Fatima', 'lastname': 'Farias'},
        {'firstname': 'Sebastian', 'lastname': 'Vera'},
        {'firstname': 'Nubia', 'lastname': 'Martinez'},
        {'firstname': 'Santiago', 'lastname': 'Acosta'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_numbs': [1.1, 4.5, 6.5, 2.2]
    } 

    for keys, value in super_dict.items():
        print(keys, "-", value)

if __name__ == '__main__':
    run()