def recursive_countdown(n):
    print(n)
    if(n==0):
        return

    else:
        recursive_countdown(n-1)

n = int(input("Enter your number: "))
recursive_countdown(n)

