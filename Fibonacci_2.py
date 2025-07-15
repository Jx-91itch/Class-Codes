def fibonnaci_of(n):
    if n in {0,1}:
        return n
    return fibonnaci_of(n-1) + fibonnaci_of(n-2)

print ([fibonnaci_of(n) for n in range(15)])