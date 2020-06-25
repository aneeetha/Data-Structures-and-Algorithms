from sys import stdin

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    sum = 1
    pre = 0
    cur = 1
    for i in range(2, n + 1):
        pre, cur = cur, pre + cur
        sum += cur*cur
    return (sum % 10)

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
