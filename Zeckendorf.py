# Python program for Zeckendorf's theorem. It finds
# representation of n as sum of non-neighbouring
# Fibonacci Numbers.

# Returns the greatest Fibonacci Numberr smaller than
# or equal to n.
def nearestSmallerEqFib(n):

    # Corner cases
    if (n == 0 or n == 1):
        return n

    # Finds the greatest Fibonacci Number smaller
    # than n.
    f1,f2,f3 = 0,1,1
    while (f3 <= n):
        f1 = f2;
        f2 = f3;
        f3 = f1+f2;
    return f2;


# Prints Fibonacci Representation of n using
# greedy algorithm
def printFibRepresntation(n):
    fib_series = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    Fib_base_binary = [0]*12
    while (n>0):

        # Find the greates Fibonacci Number smaller
        # than or equal to n
        f = nearestSmallerEqFib(n);

        # Print the found fibonacci number
        x=fib_series.index(f)
        Fib_base_binary[x] = 1


        # Reduce n
        n = n-f
    Fib_base_binary.reverse()
    # print(Fib_base_binary)
    return Fib_base_binary

# Driver code test above functions
if __name__== "__main__":
    # n = int(input("enter the number "))
        printFibRepresntation(n)
