# српшиваем сколько надо элементов
count_of_elements = int(input('Введите количество элементов списка: '))
# просим ввести элементы по одному
# по условию вводит только цифры
# так что переведем в int
users_list = [int(input(f'Введите {i+1} элемент:')) for i in range(count_of_elements)]
users_list.sort()
print(users_list)