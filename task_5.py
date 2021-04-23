"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class StackClass:
    def __init__(self):
        self.elems = []

    def ready(self):
        return self.elems

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.is_empty() or len(self.get_val()) >= 3:
            self.elems.append([])
            self.get_val().append(el)
        else:
            self.get_val().append(el)

    def pop_out(self):
        self.get_val().pop()
        if self.get_val() == []:
            del self.elems[len(self.elems) - 1]

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


SC_OBJ = StackClass()
for i in range(10):
    SC_OBJ.push_in(i)
# SC_OBJ.push_in(1)
SC_OBJ.pop_out()
# SC_OBJ.pop_out()
# SC_OBJ.pop_out()
# SC_OBJ.pop_out()

print(SC_OBJ.ready())
