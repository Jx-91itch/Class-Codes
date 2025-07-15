def prime_no(number:int):
    if number<=1:
        return False
    else:
        for k in range(2, number):
            if number % k == 0:
                return False
            else:
                return True

number= int(input("Enter the integer of your choice: "))

if(prime_no(number)):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")