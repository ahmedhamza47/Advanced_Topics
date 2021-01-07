def start_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper()

@start_decorator  # this is a decorator. it starts with an @symbol
def printing():
    print('Hamza')


