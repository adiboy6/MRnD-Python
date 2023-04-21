def factorize(number):
    if (number == 1):
        return []
    if (number < 0):
        raise ValueError
    if (type(number).__name__ == 'float'):
        raise TypeError
    i, j, c, a, b = 2, -1, 0, [], [1]
    while (number):
        if (number % i == 0):
            if i not in a:
                c, j = 1, j + 1
                a.append(i)
                b.append(1)
            else:
                c = c + 1
                b[j] = c
            if (i == number):
                break
            number = number // i
            i = 2
            continue
        i = i + 1
    b.pop()
    return list(zip(a, b))

def get_hcf(first,second):
    if(first==[] or second==[]):
        return []
    l = []
    f = dict(first)
    s = dict(second)
    for x in f:
        if x in s:
            if f[x] < s[x]:
                l.append((x, f[x]))
            else:
                l.append((x, s[x]))
    return l

def get_lcm(first,second):
    if (first == [] and second != []):
        return second
    elif first != [] and second == []:
        return first
    elif first == [] and second == []:
        return []
    l = []
    if len(first)>len(second):
        f = dict(first)
        s = dict(second)
    else:
        s = dict(first)
        f = dict(second)
    for x in f:
        if x in s:
            if f[x] > s[x]:
                l.append((x, f[x]))
            else:
                l.append((x, s[x]))
            del s[x]
        else:
            l.append((x,f[x]))
    for x in s:
        l.append((x, s[x]))
    l.sort()
    return l

def multiply(first,second):
    if (first == [] and second != []):
        return second
    elif first != [] and second == []:
        return first
    elif first == [] and second == []:
        return []
    l = []
    if len(first)>len(second):
        f = dict(first)
        s = dict(second)
    else:
        s = dict(first)
        f = dict(second)
    for x in f:
        if x in s:
            l.append((x,f[x]+s[x]))
            del s[x]
        else:
            l.append((x,f[x]))
    for x in s:
        l.append((x, s[x]))
    l.sort()
    return l