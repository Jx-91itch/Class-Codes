#def Fibonacci(idx):
#    if idx <= 1:
#        return idx
#    else:
#        return Fibonacci(idx-1)+ Fibonacci(idx-2)

#print(Fibonacci(8))

#def fibonacci(idx):
#    seq =[0,1]
#    for i in range(idx):
#        seq.append(seq[-1]+ seq[-2])
#    return seq[-2]

#print(fibonacci(10))

def fibonacci(n):
    seq =[0,1]
    for i in range(2,n+1):
        seq.append(seq[-1]+ seq[-2])
    return seq[n]

print(fibonacci(10))