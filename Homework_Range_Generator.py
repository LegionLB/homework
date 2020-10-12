def range(start, stop):
    while start<stop:
        yield start
        start +=1

a = range(1,5)
print(next(a))
print(next(a))
print(next(a))