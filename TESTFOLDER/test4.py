import random

food = ['beef', 'brocoli', 'chicken']


class test1:
    def __init__(self, name12):
        self.name2 = name12

    @classmethod
    def name1(cls):
        return cls(food)

    def name(self, food):
        #return f"cool {self.name2}"
        return test1(random.choice(food))

x1 = test1(['python', 'rules'])
x2 = test1.name1()
print(x2.name2)