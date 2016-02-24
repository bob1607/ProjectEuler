fiblist = []
def fib(x):
    a = 1
    b = 2
    total = 0
    fiblist = [a,b]
    final = 0

    while(total < x):
        total = a + b
        fiblist.append(total)
        if a < b:
            a = total
        else:
            b = total
        print(fiblist)
    for i in fiblist:
        if not i % 2:
            final = final + i
            print(final)
    print(final - fiblist.pop())
fib(4000000)
