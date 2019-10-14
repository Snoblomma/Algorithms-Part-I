# Sort random real numbers in ascending order
import random

class Experiment:

    def __init__ (self, n):
        a = []
        for i in range(n):
            a.append(random.uniform(0, 1))
        print(a)
        print(sorted(a))


if __name__ == '__main__':
    Experiment(10)