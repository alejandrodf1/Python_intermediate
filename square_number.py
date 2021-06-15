def run():
    result = []

    for number in range (1, 101):
        operation = number ** 2
        if operation%3 != 0:
            result.append(operation)
    
    print(result)

if __name__ == '__main__':
    run()