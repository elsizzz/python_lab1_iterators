# task1.py

def custom_any(lst):
    for item in lst:
        if isinstance(item, (int, float)) and item > 0:
            return True
    return False

def custom_all(lst):
    for item in lst:
        if not isinstance(item, (int, float)):
            return False
    return True

def main():
    # Ввод списка
    input_str = input("Введите элементы списка через пробел: ")
    lst = []
    for item in input_str.split():
        try:
            if '.' in item:
                lst.append(float(item))
            else:
                lst.append(int(item))
        except ValueError:
            lst.append(item)

    # 1. custom_any
    print("custom_any (есть ли положительное число):", custom_any(lst))

    # 2. Встроенная all (все ли элементы — числа)
    print("all (все ли элементы числа):", all(isinstance(x, (int, float)) for x in lst))

    # 3. Сортировка sorted
    try:
        sorted_lst = sorted(lst)
    except TypeError:
        sorted_lst = sorted(lst, key=str)
    print("Отсортированный список:", sorted_lst)

if __name__ == "__main__":
    main()