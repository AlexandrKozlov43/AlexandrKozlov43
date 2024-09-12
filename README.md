import sys

def calculate(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return max(divmod(operand1, operand2)[0], 0)
    else:
        raise ValueError("Оператор должен быть одним из знаков: +, -, *, /")

def main():
    while True:
        try:
            first_number = int(input("Введите первое число: "))
            second_number = int(input("Введите второе число: "))
            operator = input("Введите оператор (+, -, *, /): ")

            if not (1 <= first_number <= 10 and 1 <= second_number <= 10):
                print("Числа должны быть от 1 до 10 включительно.")
                continue

            result = calculate(first_number, second_number, operator)
            print(result)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nЗавершено!")
            break

if name == "main":
    main()
