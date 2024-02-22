from abc import ABC, abstractmethod


class Computer:
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer, ABC):
    def run(self):
        print("It's Running")


class Board(Computer, ABC):
    def write(self):
        print("It's writing")


class Desktop:
    def work(self, com):
        print("It's working")
        b.write()
        l.run()


c = Computer()
c.process()

l = Laptop()
l.run()

b = Board()
b.write()

d = Desktop()
d.work(l)
