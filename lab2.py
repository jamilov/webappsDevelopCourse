import random
import string

class MyClass:
    dictionary = {}

    def __init__(self, d):
        self.dictionary = d

    def addListByKey(self, inputKey, inputList):
        for key, value in self.dictionary:
            if key == inputKey:
                print(f"Ключ {inputKey} уже существует!")
                return
        self.dictionary[inputKey] = inputList
        return

    def print(self):
        k = 0
        for key in self.dictionary.keys():
            print(f"Ключ: {key}, список значений: {self.dictionary.get(key)}")
            k += 1
        print(f"Количество элементов в словаре: {k}")


    def fillWithTestData(self):
        keyLength = 5
        value = []
        for j in range(5):
            value = []
            key = ''.join(random.choices(string.ascii_lowercase, k=keyLength))
            for i in range(10):
                value.append(random.randint(-10, 10))
            self.dictionary[key] = value



    def process(self, inputKey):
        quantity = 0
        for key, value in self.dictionary.items():
            if key == inputKey:
                for i in value:
                    if i < 0:
                        quantity += 1
        return quantity


if __name__ == '__main__':
    test = {}
    objects = []
    for i in range(3):
        objects.append(MyClass(test))
        MyClass.fillWithTestData(objects[i])
        print(f"Словарь {i}")
        MyClass.print(objects[i])
        test = {}
        anyKey = random.choice(list(objects[i].dictionary.keys()))
        print(f"Ключ: {anyKey}, кол-во отрицательных элементов: {MyClass.process(objects[i], anyKey)}")
        #test
