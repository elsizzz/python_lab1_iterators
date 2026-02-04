# task9.py
import random
from string import ascii_lowercase, ascii_uppercase

def password_generator(N):
    """
    Генератор, который бесконечно генерирует случайные пароли длиной N.
    
    Args:
        N (int): Длина пароля
    
    Yields:
        str: Случайный пароль длиной N символов
    """
    # Формируем строку доступных символов
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    
    # Бесконечный цикл генерации паролей
    while True:
        # Генерируем пароль из N случайных символов
        password = ''.join(random.choice(chars) for _ in range(N))
        yield password

def main():
    """Основная функция для демонстрации работы генератора."""
    print("Генератор случайных паролей")
    
    # Длина пароля согласно варианту (N=12)
    N = 12
    
    # Создаем генератор
    gen = password_generator(N)
    
    # Выводим первые 5 паролей
    print(f"Первые 5 паролей длиной {N} символов:")
    
    for i in range(1, 6):
        password = next(gen)
        print(f"{i}. {password}")
    
    # Демонстрация бесконечности генератора
    print("\n")
    print("Демонстрация бесконечной работы генератора:")
    print("(следующие 3 пароля)")
    
    for i in range(6, 9):
        password = next(gen)
        print(f"{i}. {password}")

def test_generator():
    """Тестовая функция для проверки работы генератора."""
    print("\n")
    print("Тестирование генератора:")
    
    N = 12
    gen = password_generator(N)
    
    # Проверяем несколько паролей
    passwords = [next(gen) for _ in range(3)]
    
    print(f"1. Длина всех паролей равна {N}:", 
          all(len(p) == N for p in passwords))
    
    # Проверяем, что пароли разные (с большой вероятностью)
    print(f"2. Все пароли разные:", len(set(passwords)) == 3)
    
    # Проверяем, что используются только допустимые символы
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    chars_set = set(chars)
    all_valid = all(set(p).issubset(chars_set) for p in passwords)
    print(f"3. Все символы из допустимого набора:", all_valid)

if __name__ == "__main__":
    main()
    test_generator()
    
    # Дополнительная демонстрация: генерация по запросу
    print("\n")
    print("Генерация паролей по запросу:")
    print("(нажмите Enter для следующего пароля, 'q' для выхода)")
    
    N = 12
    gen = password_generator(N)
    
    counter = 1
    while True:
        user_input = input(f"Пароль {counter} (Enter/q): ").strip().lower()
        if user_input == 'q':
            break
        
        password = next(gen)
        print(f"  {password}")
        counter += 1
