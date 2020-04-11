# Реализовать класс который можно использовать и как декоратор и как менеджер контекста. Пусть он тоже замеряет
# время выполнения. Проверить что работает быстрее - вызвать и обработать исключение или использовать условный оператор

import time
from datetime import datetime


class Timer:
    def __init__(self, a):
        self.a = a
        self.start = datetime.now()

    def __call__(self, *args, **kwargs):
        try:
            time.sleep(1)
        except Exception:
            print(Exception)
        self.elapsed_time = datetime.now() - self.start
        return self.elapsed_time

    def __enter__(self):
        return 'I`m __enter__ method'

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(1)
        self.a.clear()
        self.elapsed_time = datetime.now() - self.start
        return self.elapsed_time


tm = Timer([i**i for i in range(0, 10000)])
with tm as T:
    print(T)


@Timer
def my_function():
    a = [i ** i for i in range(0, 10000)]
    td = Timer(a)
    return td


manager_result = tm.elapsed_time
decorator_result = my_function()
print('manager time spent: {}'.format(manager_result), '\ndecorator time spent: {}'.format(decorator_result))

if decorator_result > manager_result:
    print('manager is faster')
elif decorator_result < manager_result:
    print('decorator is faster')
