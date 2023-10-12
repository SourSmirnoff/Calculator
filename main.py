import time as t
import os
import sys


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def experimental_txt(text):
    for char in text:
        print(char, end="", flush=True)
        t.sleep(0.01)


experimental_txt(" \n \n \nPossible Operations:\n \n1. Addition\n2. Subtraction\n3. Multiplication\n4. "
                 "Division\n5. All Operations\n")

while True:
    restart = 1
    experimental_txt("\nEnter your desired operation from the list above:\n")
    desiredOperation = input()
    if desiredOperation in ('1', '2', '3', '4', '5'):
        print(" ")
    elif len(desiredOperation) >= 3:
        findOperation = desiredOperation[0] + desiredOperation[1] + desiredOperation[2]
        findOperation = findOperation.lower()
        if (findOperation in ('one', 'two', 'thr', 'fou', 'fiv', 'all', 'add', 'sum', 'sub', 'mul', 'div', 'pro', 'dif',
                              'plu', 'min', 'tim', 'rat', 'quo')):
            if findOperation in ('one', 'plu', 'sum', 'add'):
                desiredOperation = '1'
            elif findOperation in ('two', 'sub', 'dif', 'min'):
                desiredOperation = '2'
            elif findOperation in ('thr', 'pro', 'mul', 'tim'):
                desiredOperation = '3'
            elif findOperation in ('fou', 'div', 'rat', 'quo'):
                desiredOperation = '4'
            elif findOperation in ('fiv', 'all'):
                desiredOperation = '5'
        else:
            experimental_txt(" \nYour input is invalid! Try to select your operation again!")
            t.sleep(2)
            print(" ")
            continue
    else:
        experimental_txt(" \nYour input is invalid! Try to select your operation again!")
        t.sleep(2)
        print(" ")
        continue

    if desiredOperation in ('1', '2', '3', '4', '5') and restart == 1:
        try:
            experimental_txt(" \nPlease enter the first number in your calculation:\n")
            numberOne = float(input())
            experimental_txt(" \nAlright, now enter the second number:\n")
            numberTwo = float(input())
        except ValueError:
            experimental_txt(" \nYou must input a valid number, written numbers and words are not accepted!\n")
            break

        if desiredOperation == '1':
            experimental_txt(" \nHere's your results:\n")
            answer = add(int(numberOne), int(numberTwo))
            experimental_txt("{} + {} = {}".format(numberOne, numberTwo, answer))
        elif desiredOperation == '2':
            experimental_txt(" \nHere's your results:\n")
            answer = sub(int(numberOne), int(numberTwo))
            experimental_txt("{} - {} = {}".format(numberOne, numberTwo, answer))
        elif desiredOperation == '3':
            experimental_txt(" \nHere's your results:\n")
            answer = mult(int(numberOne), int(numberTwo))
            experimental_txt("{} * {} = {}".format(numberOne, numberTwo, answer))
        elif desiredOperation == '4':
            experimental_txt(" \nHere's your results:\n")
            answer = div(int(numberOne), int(numberTwo))
            experimental_txt("{} / {} = {}".format(numberOne, numberTwo, answer))
        elif desiredOperation == '5' and numberOne >= 200 or numberTwo >= 200:
            experimental_txt(" \n \nCalculating.")
            t.sleep(1)
            experimental_txt(".")
            t.sleep(1)
            experimental_txt(".")
            t.sleep(1)
            experimental_txt(".")
            t.sleep(1)
            experimental_txt(".")
            t.sleep(1)
            experimental_txt(" \n \nHere's your results:\n")
            t.sleep(1)
            answer = add(int(numberOne), int(numberTwo))
            experimental_txt("{} + {} = {}\n".format(numberOne, numberTwo, answer))
            t.sleep(1)
            answer = sub(int(numberOne), int(numberTwo))
            experimental_txt("{} - {} = {}\n".format(numberOne, numberTwo, answer))
            t.sleep(1)
            answer = mult(int(numberOne), int(numberTwo))
            experimental_txt("{} * {} = {}\n".format(numberOne, numberTwo, answer))
            t.sleep(1)
            answer = div(int(numberOne), int(numberTwo))
            experimental_txt("{} / {} = {}\n".format(numberOne, numberTwo, answer))
        elif desiredOperation == '5' and numberOne < 200 and numberTwo < 200:
            experimental_txt("Calculating.")
            t.sleep(1)
            experimental_txt(".")
            t.sleep(1)
            experimental_txt(".")
            t.sleep(1)
            experimental_txt(" \n \nHere's your results:\n")
            t.sleep(1)
            answer = add(int(numberOne), int(numberTwo))
            experimental_txt("{} + {} = {}\n".format(numberOne, numberTwo, answer))
            t.sleep(1)
            answer = sub(int(numberOne), int(numberTwo))
            experimental_txt("{} - {} = {}\n".format(numberOne, numberTwo, answer))
            t.sleep(1)
            answer = mult(int(numberOne), int(numberTwo))
            experimental_txt("{} * {} = {}\n".format(numberOne, numberTwo, answer))
            t.sleep(1)
            answer = div(int(numberOne), int(numberTwo))
            experimental_txt("{} / {} = {}\n".format(numberOne, numberTwo, answer))

        t.sleep(1)
        experimental_txt(" \n \nWould you like to calculate another problem?\n")
        moreCalculations = input()
        moreCalculations = moreCalculations.lower()
        if moreCalculations == 'yes':
            # restart = 2
            if sys.platform.startswith('win'):
                os.system('cls')
                experimental_txt(" \n \n \nPossible Operations:\n\n")
                experimental_txt("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. All Operations\n")
                continue
            elif sys.platform.startswith('darwin' or 'linux'):
                os.system('clear')
                experimental_txt(" \n \n \nPossible Operations:\n\n")
                experimental_txt("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. All Operations\n")
                continue
            else:
                experimental_txt(" \n \n \nPossible Operations:\n\n")
                experimental_txt("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. All Operations\n")
                continue
        else:
            break
    break
    