# Реализовать класс который можно использовать и как декоратор и как менеджер контекста. Пусть он тоже замеряет
# время выполнения. Проверить что работает быстрее - вызвать и обработать исключение или использовать условный оператор

import time
from datetime import datetime


class Timer:
    def __init__(self, a):
        self.a = a
        self.start = datetime.now()

    def __call__(self, *args, **kwargs):
        time.sleep(1)
        self.elapsed_time = datetime.now() - self.start
        return self.elapsed_time

    def __enter__(self):
        return 'I`m __enter__ method'

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(1)
        self.elapsed_time = datetime.now() - self.start
        return self.elapsed_time


def exception_result(a, b):
    try:
        a / b
    except ZeroDivisionError:
        return ZeroDivisionError


def condition_result(a, b):
    if b is not 0:
        return a/b
    else:
        return 'division by zero'


# print(exception_result(1, 0))
# print(condition_result(1, 0))


tm_for_exception = Timer(exception_result(1, 0))
with tm_for_exception as T:
    print(T)

tm_for_condition = Timer(condition_result(1, 0))
with tm_for_condition as T:
    print(T)


@Timer
def td_for_exception():
    td = Timer(exception_result)
    return td


@Timer
def td_for_condition():
    td = Timer(condition_result)
    return td


manager_exception_result = tm_for_exception.elapsed_time
manager_condition_result = tm_for_condition.elapsed_time

decorator_exception_result = td_for_exception()
decorator_condition_result = td_for_condition()

print('\nmanager time spent for exception: {}'.format(manager_exception_result),
      '\nmanager time spent for condition: {}'.format(manager_condition_result),
      '\ndecorator time spent for exception: {}'.format(decorator_exception_result),
      '\ndecorator time spent for condition: {}\n'.format(decorator_condition_result))

if manager_exception_result > manager_condition_result:
    print('using manager: condition is faster')
elif manager_exception_result < manager_condition_result:
    print('using manager: exception is faster')
else:
    print('using manager: same speed')

if decorator_exception_result > decorator_condition_result:
    print('using decorator: condition is faster')
elif decorator_exception_result < decorator_condition_result:
    print('using decorator: exception is faster')
else:
    print('using decorator: same speed')
