# task10.py
from datetime import datetime, timedelta

class Movie:
    def __init__(self, title, schedule_periods):
        """
        :param title: Название фильма
        :param schedule_periods: список кортежей (начало, конец) периода показа
        """
        self.title = title
        self.schedule_periods = schedule_periods

    def schedule(self):
        """Генератор, возвращающий даты показа фильма."""
        for start_date, end_date in self.schedule_periods:
            current = start_date
            while current <= end_date:
                yield current
                current += timedelta(days=1)

# Проверка
if __name__ == "__main__":
    periods = [
        (datetime(2024, 1, 1), datetime(2024, 1, 7)),
        (datetime(2024, 1, 15), datetime(2024, 2, 7))
    ]
    movie = Movie("Интерстеллар", periods)
    print(f"Даты показа фильма '{movie.title}':")
    for i, date in enumerate(movie.schedule()):
        print(date.strftime("%Y-%m-%d"), end=" ")
        if i >= 20:  # Ограничим вывод для примера
            break
    print()