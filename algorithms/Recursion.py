# recursion



def countdown(n):
    print(n)
    if n == 1:
        return
    else:
        countdown(n - 1)


print(countdown(4))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibo_list(n):
    for i in range(n):
        print(fibonacci(i), end =" ")


print(fibo_list(5))


def hanoi_tower(n, left, middle, right):
    if n == 0:
        return
    hanoi_tower(n - 1, left, right, middle)
    print('{} move {} => {}'.format(n, left, right))
    hanoi_tower(n - 1, middle, left, right)


print(hanoi_tower(2, '1', '2', '3'))