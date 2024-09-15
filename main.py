def calculator(expression):
    try:
        # Разделяем строку по пробелам
        parts = expression.split()

        # Проверяем, что строка состоит из трех частей (a, оператор, b)
        if len(parts) != 3:
            raise Exception("throws Exception")

        # Пробуем преобразовать первый и третий элемент в целые числа
        a = int(parts[0])
        b = int(parts[2])

        # Проверяем, что числа от 1 до 10 включительно
        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise Exception("throws Exception")

        # Оператор
        operator = parts[1]

        # Выполняем операцию в зависимости от оператора
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a // b  # Целочисленное деление
        else:
            raise Exception("throws Exception")

        # Выводим результат
        print(result)

    except Exception as e:
        print(e)

# Примеры работы программы
calculator("1 + 2")     # Ожидаемый вывод: 3
calculator("10 / 2")    # Ожидаемый вывод: 5
calculator("5 * 3")     # Ожидаемый вывод: 15
calculator("10 - 1")    # Ожидаемый вывод: 9
calculator("11 + 2")    # Ожидаемый вывод: throws Exception (так как 11 вне диапазона)
calculator("1")         # Ожидаемый вывод: throws Exception (потому что строка не соответствует формату)
calculator("1 + 2 + 3") # Ожидаемый вывод: throws Exception (формат не соответствует — слишком много операторов/чисел)