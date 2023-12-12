def my_numbers():
    with open("numbers.txt") as nbr:
        for number in nbr.read().split(','):
            print(number)

if __name__ == '__main__':
    my_numbers()