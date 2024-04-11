def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
    if n <= 1:
        return n
    if fibs[n] == 0:
        fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
    return fibs[n]

def fib_bottom_up(n):
    fibs = [0] * (n + 1)
    fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]




def fib_bottom_up_better(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
