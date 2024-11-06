from random import choice

# 1. Lambda-function
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


# 2. Замыкание
def get_advice_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for item in data_set:
                f.write(f'{item}\n')
    return write_everything


write = get_advice_writer('example.txt')
write('Это строка', ['A', 'это', 'число', 'уже', 5, 'в', 'списке'])


# 3. Metod __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
