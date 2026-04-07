from abc import ABC
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class lion(animal):
    def move(self):
        print("i can roar")
class dog(animal):
    def move(self):
        print("i can bark")
class snake(animal):
    def move(self):
        print("i can crawl")
r = human()
r.move()
k = snake()
k.move()
r = dog()
r.move()
k = lion()
k.move()