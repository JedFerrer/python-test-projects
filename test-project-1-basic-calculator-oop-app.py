class Calculator:
    def __init__(self):
        self.execute = 'Y'

    def addition(self, first_value, second_value):
        return first_value + second_value

    def subtraction(self, first_value, second_value):
        return first_value - second_value

    def multiplication(self, first_value, second_value):
        return first_value * second_value

    def division(self, first_value, second_value):
        return first_value / second_value

    def format_output(self, value):
        return int(value) if value.is_integer() else value

    def input_value(self, label):
        while True:
            user_input = input(f"Give me a {label} number: ")
            try:
                clean_value = float(user_input)
                return user_input, clean_value
            except ValueError:
                print(
                    f"Error: '{user_input}' is not a valid number. Try again.")

    def operator_value(self):
        while True:
            user_input = input("Enter an operator (+, -, *, /): ")
            if user_input in ['+', '-', '*', '/']:
                return user_input
            print(f"Error: '{user_input}' is not a valid operator. Try again.")

    def calculate(self, first_value, second_value, operator):
        operations = {
            '+': self.addition,
            '-': self.subtraction,
            '*': self.multiplication,
            '/': self.division
        }
        return operations[operator](first_value, second_value)

    def run(self):
        while self.execute == 'Y':
            first_user_input, first_value = self.input_value('first')
            second_user_input, second_value = self.input_value('second')
            operator = self.operator_value()
            result = self.calculate(first_value, second_value, operator)

            print(
                f"{first_user_input} {operator} {second_user_input} = {self.format_output(result)}")

            self.execute = input(
                "Do you want to calculate another value? (Y or N): ").strip().upper()
            if self.execute == 'N':
                break


# Run the calculator
if __name__ == "__main__":
    Calculator().run()
