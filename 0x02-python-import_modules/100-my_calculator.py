#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
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
            print("{} + {} = {}"
                  .format(int(argv[1]), argv[3], int(argv[1]) + int(argv[3])))
        elif argv[2] == '-':
            print("{} + {} = {}"
                  .format(int(argv[1]), argv[3], int(argv[1]) - int(argv[3])))
        elif argv[2] == '*':
            print("{} + {} = {}"
                  .format(int(argv[1]), argv[3], int(argv[1]) * int(argv[3])))
        else:
            print("{} + {} = {}"
                  .format(int(argv[1]), argv[3], int(argv[1]) / int(argv[3])))
