first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

second_result = (len(f) == len(s) for f, s in zip(first, second))


print(list(first_result))
print(list(second_result))

