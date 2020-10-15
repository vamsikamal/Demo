def mygen():
    yield 'sunday'
    yield 'monday'
    yield 'tuesday'

g = mygen()
print(g)
print(type(g))
print(next(g))
print(next(g))