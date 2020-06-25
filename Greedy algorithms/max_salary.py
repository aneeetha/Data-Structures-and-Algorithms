import sys

def cmp(a, b):
    i = str(a)
    j = str(b)
    if int(i[0]) > int(j[0]):
        return 1
    elif int(i[0]) == int(j[0]):
        k=1
        l=1
        if len(i) > len(j):
            while(l < len(j)):
                if int(i[k]) > int(j[l]):
                    return 1
                elif int(i[k]) == int(j[l]):
                    if
                else:
                    return 0
            k += 1
    elif int(i[0]) == int(j[0]):
        k = 1
        l = 1
        m = min(len(i), len(j))
        while()

def sort(a):
    for i in range(len(a)-1):
        for j in range(1, len(a)):
            if a[i] > a[j] and cmp(a[i],a[j]):
                a[i], a[j] = a[j], a[i]
    return a

def largest_number(a):
    a = sort(a)
    res = ""
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))