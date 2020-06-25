
def fibo(n):
    pre = 0
    cur = 1
    if n < 2:
        return n
    else:
        for i in range(2, n+1):
            pre, cur = cur, pre + cur
        return cur

n = int(input())
print(fibo(n))
