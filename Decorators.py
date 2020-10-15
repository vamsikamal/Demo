# Decorator is a kind of function
# Takes a function as argument and extend the functionality
def decor(func):
    def inner(name):
        if name == 'Rohit':
            print('Good evening', name)
        else:
            func(name)
    return inner

@decor
def wish(name):
    print('Good morning', name)


wish('Vamsi')
wish('Kamal')
wish('Rohit')
