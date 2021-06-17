def run():
    # result = []

    # for number in range (1, 101):
    #     if number%3 != 0:
    #         result.append(number ** 2)
    
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    # multiples = [i for i in range(1, 99999) if i%4==0 and i%6==0 and i%9 == 0]

    multiples = [i for i in range(1, 99999) if i%36 == 0]

    print(multiples)

if __name__ == '__main__':
    run()