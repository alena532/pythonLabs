import math

from Serializer.Factory import factory
from lab2 import Factory




def print_hi(name):
    factory=Factory('text.json')
    factory=factory.create_serializer('json')
    x=factory.dumps(5)
    c=factory.loads(x)
    c()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
