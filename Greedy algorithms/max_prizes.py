import sys

def optimal_summands(n):
    summands = []
    if n <= 2:
        summands.append(n)
    else:
        i = 1
        while(n):
            if i <= n:
                summands.append(i)
                n -= i
            else:
                n += summands.pop()
                summands.append(n)
                break
            i+=1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
