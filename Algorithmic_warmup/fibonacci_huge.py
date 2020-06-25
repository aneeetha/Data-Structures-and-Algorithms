def pisano_period(m):
    previous = 0
    current = 1

    for i in range(m * m):
        previous, current = current, (previous + current)%m
        if previous == 0 and current == 1:
            return i+1

def fibo_huge(n, m):
    if (n < 2):
        return n
    n %= pisano_period(m)
    pre = 0
    cur = 1
    for i in range(2, n + 1):
        pre, cur = cur, pre + cur
    return cur % m


n, m = map(int, input().split())
print(fibo_huge(n, m))

