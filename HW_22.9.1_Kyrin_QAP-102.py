numbers = input('Введите числа через пробел: ')
user_num = input('Введите любое число: ')
lst_of_numbers = None


def is_int(num1, num2):
    try:
        global lst_of_numbers, user_num
        lst_of_numbers = list(map(int, num1.split()))
        user_num = int(num2)
    except ValueError as error:
        print(error)
        print("Необходимо вводить числа")
    else:
        return lst_of_numbers, user_num


is_int(numbers, user_num)
# Проверяем,что ввидены числа


def sort_array(lst_num):
    for i in range(len(lst_num)):
        for j in range(len(lst_num) - i - 1):
            if lst_num[j] > lst_num[j + 1]:
                lst_num[j], lst_num[j + 1] = lst_num[j + 1], lst_num[j]

    return lst_num

#Сортируем полученный список
array = sort_array(lst_of_numbers)
#Проверка нахождения числа в последовательности
element = user_num
while element:
    if element not in range(min(array) + 1, max(array)):
        print('Некорректное число')
        element = int(input('Введите число в рамках последовательности: '))
    else:
        break
array.append(element)


def binary_search(array, element, left, right):
    if left > right:
        return left, right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle, middle-1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


a = (binary_search(array, element, 0, len(array)-1))

print(a)
