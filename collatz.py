def collatz(num):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = num * 3 + 1
    else:
        print(num)
        print('Done!')


def main():
    try:
        num = int(input('Input an integer: '))
        collatz(num)
    except ValueError:
        print('ValueError: Please enter an integer.')


main()
