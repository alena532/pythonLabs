from Serializer.Factory import factory
from lab2 import Factory

class A:
    def h(self):
        print("In class A")


class Person(A):
    def func(self):
        print('Hello')



def print_hi(name):
    a=Person()
    ab=Factory("str")
    pars=ab.create_serializer('json')
    x=pars.dumps(a)
    e=pars.loads(x)
    e.h()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
