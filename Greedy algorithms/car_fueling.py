import sys


def compute_min_refills(distance, tank, stops):
    c = 0
    t = tank - stops[0]
    if(distance < tank):
        return 0
    for i in range(len(stops)):
       if(i==len(stops)-1):
           t -= (stops[i] - stops[i - 1])
           if((distance-stops[i]) > t):
               c += 1
               t = tank
           distance -= stops[i]
           if distance <= t:
               return c
           break
       if(i!=0):
            t -= (stops[i] - stops[i-1])
       if( (stops[i+1]-stops[i]) > t):
           c += 1
           t = tank
       if((stops[i+1] - stops[i]) > t):
           break

    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))