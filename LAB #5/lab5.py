def factorial(x):
    if( x==1 or x < 1 ):
        return 1
    else:
        return x*factorial(x-1)

absVal = lambda i,x : (pow(x,2*i))/factorial(2*i)

def exp_x(x,n):
    i = 0
    sum = 0
    while i < n :
        sign = (-1)**i
        sum += sign*absVal(i,x)
        i = i+1
    return sum

summation = 0
i = 0

def powerSum(n,r):
    """
        Recursive logic: Iterates from current_i up to n.
        In each step, r^current_i is added to the global summation.
        Sign handling: All terms are positive as per the formula G_n = 1 + r + r^2... [cite: 15]
        """
    global summation
    global i
    if(i > n):
        return
    summation += pow(r,i)
    i = i +1
    powerSum(n,r)


powerSum(3,1)
print(summation)