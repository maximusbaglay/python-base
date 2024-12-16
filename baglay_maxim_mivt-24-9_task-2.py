# Задача 2. Кэширование запросов
# Контекст
# Вы разрабатываете программу для кэширования запросов к внешнему API. Часто повторяющиеся запросы занимают много времени, поэтому вы решаете создать класс LRU Cache (Least Recently Used Cache), который будет хранить ограниченное количество запросов и автоматически удалять самые старые при достижении лимита. Это позволит значительно ускорить повторяющиеся запросы, так как данные будут браться из кэша, а не отправляться повторно.

# Задача
# 1. Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита, удаляет самые давние (самые старые) использованные элементы.
# 2. Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.

# @property
# def cache(self): # этот метод должен возвращать самый старый элемент
#     ...
# @cache.setter
# def cache(self, new_elem): # этот метод должен добавлять новый элемент
#     ...

# Советы
# Не забывайте обновлять порядок использованных элементов. В итоге должны удаляться давно использованные элементы, а не давно добавленные, так как давно добавленный элемент может быть популярен, и его удаление не поможет ускорить новые запросы.

from collections import OrderedDict

# 1.1. Создание класса LRUCache.
class LRUCache: 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order = OrderedDict()

# 1.1. Использование декораторов property и setter.
    @property
    def cache(self) -> OrderedDict:
        return next(iter(self.order.items()))
    
    @cache.setter
    def cache(self, new_elem):
        if new_elem[0] in self.order:
            self.order.pop(new_elem[0])
        elif len(self.order) >= self.capacity:
            self.order.popitem(last=False)
        self.order[new_elem[0]] = new_elem[1]
    
    def print_cache(self):
        print("LRU Cache:")
        if self.order:
            for key, value in self.order.items(): 
                print(f'{key} : {value}') 
        else:
            print("Кэш пуст")
     
    def get(self, key: str) -> str:
        if key in self.order:
            return self.order[key]
        return None

# Создаём экземпляр класса
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# Выводим текущий кэш
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2")) # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновлённый кэш
cache.print_cache()