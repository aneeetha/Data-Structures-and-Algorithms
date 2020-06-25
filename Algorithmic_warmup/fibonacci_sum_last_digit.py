import sys

def fibonacci_sum(n):
    if n <= 1:
        return n
    sum = 1
    pre = 0
    cur = 1
    for i in range(2, n+1):
        pre, cur = cur, pre + cur
        sum += cur
    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))