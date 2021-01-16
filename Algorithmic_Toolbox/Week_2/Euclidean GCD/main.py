def euclidGCD(a,b):
    low= min(a,b)
    high= max(a,b)
    if low == 0:
        return high
    else:
        t_= high % low
        return euclidGCD(t_ , low)

print(euclidGCD(357, 234))