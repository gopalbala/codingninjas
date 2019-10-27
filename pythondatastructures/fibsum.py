def fib(n):
    n1 = 0
    n2 = 1
    i = 0
    n3 = 0
    s = 0
    while i < n:
        n3 = n1 + n2
        # print(n3)
        n1 = n2
        n2 = n3
        if n3 % 2 == 0 and n3 <= n:
            s += n3
        i += 1

    print(s)


n = int(input())
fib(n)
