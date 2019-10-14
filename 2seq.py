user_str = input('''Введите элементы списка через любой односимвольный разделитель 
                 (разделителем будет выбран первый символ не являющийся числом или буквой): ''')
# разделитель по умолчанию
sep = ','
# проверим, может пользователь использует другой разделитель
for element in user_str:
    if not element.isalnum():
        sep = element
        print(f'Определен символ-разделитель: {sep}')
        break
# разберем строку по кусочкам и запишем в список
user_list = [int(i) for i in user_str.split(sep)]
# из списка сделаем множество, чтобы убрать повторяющиеся элементы
user_set = set(user_list)
# тепеь у нас есть сет все варианты которые вводил пользователь
# соберем из них список уникальных
# для этого делаем пустой список
result_list = []
# и пробегаемся по всем элементам сета
for element in user_set:
    # если количество вхождений равно 1 то добавим в итоговый список
    if user_list.count(element) == 1:
        result_list.append(element)
# выводим результат
print(result_list)
