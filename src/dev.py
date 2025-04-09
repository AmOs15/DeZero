import numpy as np
from core import Variable

def step1():
    data = np.array([1.0, 2.0, 3.0])
    x = Variable(data)
    print(x.data)

def main():
    step1()

if __name__ == "__main__":
    main()
