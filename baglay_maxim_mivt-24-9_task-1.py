# Задача 1. Стек
# 1.1. Стек - это абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

# Напишите класс, который реализует Стек и его возможности (достаточно будет добавления и удаления элемента).

# 1.2. После этого напишите ещё один класс “Менеджер задач”. В менеджере задач можно выполнить команду “новая задача”, в которую передаётся сама задача (str) и её приоритет (int). Сам менеджер работает на основе Стэка (не наследование!). При выводе менеджера в консоль все задачи должны быть отсортированы по приоритету: чем меньше число, тем выше задача.

# Вот пример основной программы:

# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать дз", 2)
# print(manager)

# Результат:
# 1 отдохнуть;
# 2 поесть; сдать дз;
# 4 сделать уборку; помыть посуду.
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами

# 1.1. Объявление базового класса Стек.
class Stack:   

# Создаём функцию, используем метод _init_ и переменную в виде списка.
    def __init__(self):
        self.items = []
    
# Добавление в стек элемента item.
    def push(self, item):
        self.items.append(item)
        self.items.sort(key=lambda x: x[1])

# Удаление из стека по принципу LIFO.
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

# 1.2. Объявление базового класса Менеджер задач.
class TaskManager:
    def __init__(self):
        self.stack = Stack()

# Функция новой задачи.
    def new_task(self, item, priority):
        self.stack.push((item, priority))

# Функция сортировки приоритетности.
    def __str__(self):
        result = ""
        for item, priority in self.stack.items:
            result += f"{priority} {item}\n"
        return result

# Функция удаления дубликатов.
# PS: Нашёл и перепробовал несколько вариантов удаления дубликатов, но дубликаты не удаляются.
    # def remove_items(self):
    #     self.stack.items = list(set(self.stack.items))
    #     self.stack.items.sort(key=lambda x: x[1])

# Основная программа.
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# manager.remove_items()

# print(manager)