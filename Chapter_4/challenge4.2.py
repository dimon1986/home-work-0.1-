# Анализатор текста
# Демонстрирует работу функции len() и оператора in
# всё просто
msg = input('Введите текст: ')
print('\nДлина введенного вами текста составляет:', len(msg))
new_msg = ''

for letter in msg[::-1]:
    new_msg += letter
    print('Создана новая строка:', new_msg)
input('\n\nНажмите Enter, что бы выйти...')