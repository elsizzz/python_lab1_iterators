# task4.py

class CyclicRangeIterator:
    def __init__(self, start, stop, step=1):
        self.range_iter = iter(range(start, stop, step))
        self.start = start
        self.stop = stop
        self.step = step
        self.current_iter = self.range_iter
        self.first_iteration = True

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.current_iter)
        except StopIteration:
            # Перезапускаем итератор
            self.current_iter = iter(range(self.start, self.stop, self.step))
            return next(self.current_iter)

# Проверка
if __name__ == "__main__":
    cyclic_range = CyclicRangeIterator(1, 5)
    for i, val in enumerate(cyclic_range):
        print(val, end=" ")
        if i >= 15:
            break  # Чтобы не уйти в бесконечный вывод
    print()