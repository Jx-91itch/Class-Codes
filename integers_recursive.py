def integers_recursive(num1: int, num2: int):
    if num1 == 0 or num2 == 0:
        return 0
    elif   num2==1:
        return num1
    else:
        return num1+(num1*(num2-1))


num1= int(input("Enter Number 1: "))
num2= int(input("Enter Number 2: "))
ans= integers_recursive(num1,num2)
print(ans)