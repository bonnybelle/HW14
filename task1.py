# Реализовать свой класс исключения. Добавить метод записи в файл. Вызвать своё исключение и записать ошибку в файл.


class MyException(Exception):
    def __init__(self, first, last, path):
        self.first = first
        self.last = last
        self.path = path

    def checking(self):
        try:
            return self.first <= self.last
        except Exception as e:
            self.writing(str(e))
            return e

    def writing(self, txt):
        with open(self.path, 'w') as file:
            file.write(txt)


path = 'C:\\Users\\bonny\\PycharmProjects\\FirstPrj\\advanced\\HW14\\task1_result.txt'
me1 = MyException(0, 9, path)
me2 = MyException('abc', -9, path)
print('me1: ', me1.checking(),
      '\nme2: ', me2.checking())
