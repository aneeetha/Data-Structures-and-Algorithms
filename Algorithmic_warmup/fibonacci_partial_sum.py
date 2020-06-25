import sys

def fibonacci_partial_sum(start, end):
    sum = 0
    pre = 0
    cur = 1
    if start == 1 or end == 1:
        sum=1
    for i in range(2, end + 1):
        pre, cur = cur, pre + cur
        if i >= start:
            sum += cur
    return (sum % 10)


if __name__ == '__main__':
    input = sys.stdin.read();
    start, end = map(int, input.split())
    print(fibonacci_partial_sum(start, end))