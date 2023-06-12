#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, div, mul, sub
    len = len(argv) - 1
    op = ['+', '-', '/', '*']
    if len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == '+':
            print('{} + {} = {}'.format
                  (int(argv[1]), argv[3], add(int(argv[1]), int(argv[3]))))
            exit(0)
        elif argv[2] == '-':
            print("{} + {} = {}".format
                  (int(argv[1]), argv[3], sub(int(argv[1]), int(argv[3]))))
            exit(0)
        elif argv[2] == '*':
            print("{} + {} = {}".format
                  (int(argv[1]), argv[3], mul(int(argv[1]), int(argv[3]))))
            exit(0)
        else:
            print("{} + {} = {}".format
                  (int(argv[1]), argv[3], div((argv[1]), int(argv[3]))))
            exit(0)
