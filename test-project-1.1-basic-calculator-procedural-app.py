def addition(first_value, second_value):
    result = first_value + second_value
    return result


def subtraction(first_value, second_value):
    result = first_value - second_value
    return result


def multiplication(first_value, second_value):
    result = first_value * second_value
    return result


def division(first_value, second_value):
    result = first_value / second_value
    return result


def format_output(value):
    if value.is_integer():
        value = int(value)
    return value


def input_value(label):
    while True:
        user_input = input(f"Give me a {label} number: ")
        try:
            clean_value = float(user_input)
            print(f"First input value: {user_input}")
            break  # Exit the loop if the conversion is successful
        except ValueError:
            print(
                f"Error: '{user_input}' is not a valid number for {label} input. Please try again.")

    return user_input, clean_value


def operator_value():
    while True:
        user_input = input("Enter an operator (+, -, *, /): ")

        if user_input in ['+', '-', '*', '/']:
            break  # Exit the loop if the input is valid
        else:
            print(
                f"Error: '{user_input}' is not a valid operator. Please try again.")

    return user_input


def calculate(first_value, second_value, operator):
    if operator == '+':
        result = addition(first_value, second_value)
    elif operator == '-':
        result = subtraction(first_value, second_value)
    elif operator == '*':
        result = multiplication(first_value, second_value)
    elif operator == '/':
        result = division(first_value, second_value)

    return result


def initialize():
    execute = 'Y'

    while execute == 'Y':
        first_user_input, first_value = input_value('first')
        second_user_input, second_value = input_value('second')
        operator = operator_value()
        result = calculate(first_value, second_value, operator)
        print(
            f"{first_user_input} {operator} {second_user_input} = {format_output(result)}")

        execute = input(
            'Do you want to calculate another value? (Y or N)').strip().upper()
        if execute == 'N':
            break


initialize()  # Run Calculator App
