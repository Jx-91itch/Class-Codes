def power(base,exp):
    print("Method call")
    print("exp = :", exp)
    print("base = :", base)
    if(exp == 1):
        print(" Base case. No further recursion. No more method calls")
        return (base)
    if(exp != 1):
        print("General case")
        return (base* power(base,exp-1))

base=int(input("Enter base: "))
exp=int(input("Enter exponential value:"))
print("Result :", power(base,exp))