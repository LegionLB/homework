class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            result = self.start
            self.start += 1
            return result

        raise StopIteration


a = Range(1,5)
print(next(a))
print(next(a))
print(next(a))