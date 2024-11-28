import math
from src.dal.constants.globalVariables import history

def calculator():

    memory = None

    decimal_places = int(input("Enter the number of decimal places: "))

    while True:
        try:
            first_number = input("Enter the first number or press m to memory: ").lower()
            if first_number == 'm':
                if memory is None:
                    print("Memory is empty!")
                    continue
                first_number = memory
            else:
                first_number = float(first_number)

            operator = input("Enter the operator (+, -, *, /, ^, √, %): ")

            if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                print("Wrong operator! Try again!")
                continue

            if operator != "√":      # √ need only one number
                second_number = input("Enter the second number or press m to memory: ").lower()
                if second_number == 'm':
                    if memory is None:
                        print("Memory is empty!")
                        continue
                    second_number = memory
                else:
                    second_number = float(second_number)
            else:
                second_number = None

            result = calculateExpression(first_number, second_number, operator)

            if result is None:
                continue

            result = round(result, decimal_places)
            print(f"Result: {result}")

            expression = f"{first_number} {operator} {second_number if second_number is not None else ''} = {result}"
            history.append(expression)           # expression recording

            save_to_memory = input("Save result in memory? (yes/no): ").lower()
            if save_to_memory == 'yes':
                memory = result
                print("Result has been saved in the memory.")

        except ValueError:
            print("Please, enter right numbers.")
            continue

        repeat = input("Do you want to make another operation? (yes/no): ").lower()
        if repeat != 'yes':
            viewHistory(history)
            print("finished!")
            break

def calculateExpression(first_number, second_number, operator):
    match operator:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number
        case '/':
            if second_number == 0:
                print("You cannot divide by zero!")
                return None
            return first_number / second_number
        case '^':
            return first_number ** second_number
        case '√':
            if first_number < 0:
                print("Number cannot be lower than zero!")
                return None
            return math.sqrt(first_number)
        case '%':
            return first_number % second_number
        case _:
            print("Invalid operator!")
            return None

def viewHistory(history):
    view_history = input("Do you want to watch history? (yes/no): ").lower()
    if view_history == 'yes':
        print("History: ")
        for record in history:
            print(record)




# def changeSettings(decimal_places):
#    change_settings = input("Do you want to change the number of decimal places? (yes/no): ").lower()
#    if change_settings == 'yes':
#        decimal_places = int(input("Enter the new number of decimal places: "))
#        print(f"Number of decimal places has been changed to {decimal_places}.")
#    return decimal_places