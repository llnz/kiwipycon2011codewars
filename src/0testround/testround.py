'''
find P(F(x)) where
seed number 17

F(n) is nth number of fibonacci series [1,1,2,3]
P(n) is nth prime number [2,3,5,7]
'''

from math import sqrt

seed = 17

fibcache = []
def fib(n):
    fibl = [1, 1]
    for idx in xrange(2, n+1):
        fibl.append(fibl[idx-2] + fibl[idx-1])

    return fibl[n -1]

def is_prime(n):
    for d in range(2, int(sqrt(n)+ 1)):
        if (n/d)* d == n:
            return False
    return True




if __name__ == '__main__':
    print 'seed', seed
    fibn = fib(seed)
    print 'fib', fibn
    pc = 0
    for n in range(2, 20000):
        if is_prime(n):
            pc += 1
            if pc == fibn:
                print 'P(F(n)) ==', n
                break

