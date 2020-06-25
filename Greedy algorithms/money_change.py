import sys

def get_change(m):
    c = m // 10
    m %= 10
    c += m // 5
    c += m % 5
    """while(m>=10):
         c += 1
         m-=10
    while(m>=5):
         c += 1
         m-=5
    while(m>=1):
         c +=1
         m-=1"""
    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
