import random

class iteratorA:
    def __init__(self):
        self.state = 0
    def __iter__(self):
        return self
    def __next__(self):
        current = self.state
        self.state = 1 - self.state
        return current

class iteratorB:
    def __init__(self):
        self.state = 0
    def __iter__(self):
        return self
    def __next__(self):
        directions = ["N", "E", "S", "W"]
        return random.choice(directions)

class iteratorC:
    def __init__(self):
        self.state = 0
    def __iter__(self):
        return self
    def __next__(self):
        current = self.state
        self.state = self.state + 1
        if self.state == 7: self.state = 0
        return current

it = iteratorA()
print(next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it))

it = iteratorB()
print(next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it))

it = iteratorC()
print(next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it), next(it))