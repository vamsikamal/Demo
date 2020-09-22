from abc import *
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def erase(self):
        pass

class circle(Shape):
    def draw(self):
        print('circle')
    def erase(self):
        print('circle delted')

class rectangle(Shape):
    def draw(self):
        print('Rectangle')
    def erase(self):
        print('Rectangle delted')

c = circle()
c.draw()
c.erase()

r= rectangle()
r.draw()
r.erase()