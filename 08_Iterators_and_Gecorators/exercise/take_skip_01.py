# 1.Take Skip
class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.produced = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.produced < self.count:
            produced_next = self.produced
            self.produced += 1
            return self.step * produced_next
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
