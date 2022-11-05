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

# # python3.10 -i generator_functions.py 
# >>> gen_range(10)
# <generator object gen_range at 0x7f7aea8cff40>
# >>> 
# KeyboardInterrupt
# >>> generator = gen_range(10)
# >>> list(generator)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> fib = gen_fib()
# >>> [next(fi
# fib       filter(   finally:  
# >>> [next(fib) for _ in range(50)] [-1]
# 12586269025