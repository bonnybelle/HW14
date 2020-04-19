# Реализовать свой класс исключения. Добавить метод записи в файл. Вызвать своё исключение и записать ошибку в файл.


class MyException(Exception):
    def __init__(self, message):
        self.path = 'C:\\Users\\bonny\\PycharmProjects\\FirstPrj\\advanced\\HW14\\task1_result.txt'

    def raising(self):
        try:
            raise MyException('this`s an exception')
        except MyException as e:
            self.writing(str(e))

    def writing(self, txt):
        with open(self.path, 'w') as file:
            file.write(txt)


print(MyException)
