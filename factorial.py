from math import factorial

n = int(input("Enter a number: "))
factorial= 1
if n>=1:
    for i in range(1,n+1): # for(int i=1; i<10, I
        factorial= factorial*i
print ("Factorial number is", factorial)