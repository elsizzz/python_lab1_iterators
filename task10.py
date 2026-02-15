# task10_loadtest.py
from datetime import datetime, timedelta
import time

class Movie:
    def __init__(self, title, schedule_periods):
        self.title = title
        self.schedule_periods = schedule_periods

    def schedule(self):
        for start_date, end_date in self.schedule_periods:
            current = start_date
            while current <= end_date:
                yield current
                current += timedelta(days=1)

def load_test_yield():
    """Тест производительности с yield и выводом дат"""
    print("ТЕСТ 1: Генератор с yield (с выводом дат)")
    
    # Создаем периоды с большим количеством дней
    periods = [
        (datetime(2020, 1, 1), datetime(2020, 1, 10)),  # 10 дней для примера
        (datetime(2020, 2, 1), datetime(2020, 2, 5)),   # 5 дней
    ]
    
    movie = Movie("Нагрузочный тест", periods)
    start_time = time.time()
    
    count = 0
    # Перебираем и ВЫВОДИМ все даты
    for date in movie.schedule():
        count += 1
        # Выводим дату в формате ГГГГ-ММ-ДД
        print(f"  {count:3d}. {date.strftime('%Y-%m-%d')}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"\nРезультаты:")
    print(f"  Всего дат: {count}")
    print(f"  Время выполнения: {elapsed_time:.4f} секунд")
    print(f"  Скорость: {count/elapsed_time:.0f} дат/сек")

if __name__ == "__main__":
    print("НАГРУЗОЧНОЕ ТЕСТИРОВАНИЕ ГЕНЕРАТОРА\n")
    load_test_yield()