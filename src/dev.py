import numpy as np
from core import Variable, Square

def step1():
    data = np.array([1.0, 2.0, 3.0])
    x = Variable(data)
    print(x.data)

def step2():
    x = Variable(np.array(10))
    square = Square()
    y = square(x)
    print(type(y))
    print(y.data)

def main():
    step2()

if __name__ == "__main__":
    main()
