import sys

def frac(weights, values):
    fract = []
    for i, j in zip(weights, values):
        fract.append(j / i)
    return fract

def merge_sort(fract, weights, values):
    if(len(fract)>1):
        m = len(fract)//2
        left = fract[:m]
        right = fract[m:]
        wl = weights[:m]
        wr = weights[m:]
        vl = values[:m]
        vr = values[m:]
        left, wl, vl = merge_sort(left, wl, vl)
        right, wr, vr = merge_sort(right, wr, vr)

        fract = []
        weights = []
        values = []
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                fract.append(left[0])
                weights.append(wl[0])
                values.append(vl[0])
                left.pop(0)
                wl.pop(0)
                vl.pop(0)
            else:
                fract.append(right[0])
                right.pop(0)
                weights.append(wr[0])
                values.append(vr[0])
                wr.pop(0)
                vr.pop(0)
        for i, j, k in zip(left, wl, vl):
            fract.append(i)
            weights.append(j)
            values.append(k)
        for i, j, k in zip(right, wr, vr):
            fract.append(i)
            weights.append(j)
            values.append(k)

    return list(fract), list(weights), list(values)

def get_optimal_value(capacity, weights, values):
    value = 0.
    fract = frac(weights, values)
    fract, weights,values = map(list, merge_sort(fract, weights, values))
    for i in range(len(weights)):
        if capacity == 0:
            break
        a = min(weights[i], capacity)
        value += a * fract[i]
        weights[i] -= a
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
