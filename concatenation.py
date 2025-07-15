from tokenize import String

#reversed string
#palindromes
def concatenation(a):
    if len(a) == 0:
        return a
    else:
        return concatenation(a[1:])+ a[0]

a = input("Enter String:")
print("Reversed string: ", concatenation(a))
