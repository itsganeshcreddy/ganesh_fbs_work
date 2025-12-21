# 1. We want to generate Fibonacci numbers up to a certain limit. 
#    Instead of computing and storing the entire sequence in memory, 
#    create generator to yield Fibonacci numbers one by one, 
#    conserving memory and allowing for easy iteration. 

def fib_gen(limit):
    a, b = 0, 1
    while(a <= limit):
        yield a
        a, b = b, a + b

# limit = 50
# for n in fib_gen(limit):
#     print(n)

res = fib_gen(50)
print(next(res))  

for i in res:
    print(i)      