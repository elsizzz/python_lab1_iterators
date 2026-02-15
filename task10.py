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
    """Тест производительности с yield"""
    print("Генератор с yield")
    
    # Создаем периоды с большим количеством дней
    periods = [
        (datetime(2020, 1, 1), datetime(2025, 12, 31)),  # ~2190 дней
        (datetime(2026, 1, 1), datetime(2030, 12, 31)),  # ~1825 дней
        (datetime(2031, 1, 1), datetime(2035, 12, 31)),  # ~1825 дней
    ]
    
    movie = Movie("Нагрузочный тест", periods)
    start_time = time.time()
    
    count = 0
    # Перебираем все даты
    for date in movie.schedule():
        count += 1
        if count % 500 == 0:  # Показываем прогресс каждые 500 дат
            print(f"  Обработано {count} дат...")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"\nРезультаты:")
    print(f"  Всего дат: {count}")
    print(f"  Время выполнения: {elapsed_time:.4f} секунд")
    print(f"  Скорость: {count/elapsed_time:.0f} дат/сек")

if __name__ == "__main__":
    print("НАГРУЗОЧНОЕ ТЕСТИРОВАНИЕ ГЕНЕРАТОРА\n")
    load_test_yield()