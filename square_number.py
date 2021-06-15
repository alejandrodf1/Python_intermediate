def run():
    result = []

    for number in range (1, 101):
        if number%3 != 0:
            result.append(number ** 2)
    
    print(result)

if __name__ == '__main__':
    run()