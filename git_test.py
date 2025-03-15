print('Сәлем әлем!')
# ngg

ljkiyutfjhvnbnvv = 7


# gyuggguyg
# huihiyii
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    ':': operator.truediv
}

def calculate_expression(expr):
    for op in ops:
        if op in expr:
            left, right = expr.split(op, 1)
            try:
                return ops[op](float(left.strip()), float(right.strip()))
            except (ValueError, ZeroDivisionError):
                raise ValueError(f"Некорректное выражение: {expr}")
    return float(expr)

numbers = []

print("Введите числа: ")
print("Нажмите 'F', чтобы завершить ввод и увидеть результат.")

while True:
    user_input = input("> ").strip()
    if user_input.upper() == 'F':
        break

    try:
        number = calculate_expression(user_input)
        numbers.append(number)
    except Exception as e:
        print(f"Ошибка: {e}. Попробуйте снова.")

if numbers:
    print(f"Минимальное число: {min(numbers)}")
    print(f"Максимальное число: {max(numbers)}")
else:
    print("Вы не ввели ни одного числа.")