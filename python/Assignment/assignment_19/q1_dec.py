# 1. Develop a memoization decorator that caches the results of function 
#    calls and returns the cached result when the same inputs occur again. 
#    This can greatly improve the performance of recursive or 
#    computationally intensive functions.

def memoize(func):
    cache = {}   

    def wrapper(n):
        if(n in cache): 
            print('available in cache...')        
            return cache[n]                      # return cached result
        result = func(n)                         # call the function
        cache[n] = result                        # store result in cache
        print('not available...')
        return result

    return wrapper

@memoize
def fib(n):
    f = []
    a, b = 0, 1
    for i in range(n):
        f.append(a)
        a, b = b, a + b
        
    return f

res = fib(10)
print(res)
print('--------------------------')
res = fib(10)
print(res)


# def fibonacci(n):
#     if(n <= 1):
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))