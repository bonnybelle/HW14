# Использовать contextmanager и реализовать функцию, которая будет работать как менеджер контекста.
# И сможет замерять время выполнения блока.
import time
from datetime import datetime
from contextlib import contextmanager


@contextmanager
def my_function():
    print('start')
    start = datetime.now()
    yield
    finish = datetime.now() - start
    print(finish, '\nfinish')


with my_function():
    a = [i**i for i in range(1, 10)]
    b = a[::-1]
    time.sleep(0.1)
    print(a, b)
