# generator is a different concept that I'm learning, this is similar to range method 
# And this can be used to calculate Fibonacci series faster then regular logics
def gen_range(stop, start=1, step=1):
    '''Generator function works similar to range() but first give stop value,then start value and stop value in order'''
    num = start
    while num <= stop:
        yield num
        num += step

def gen_fib():
    '''Calculates Fibonacci series with high efficiency'''
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
