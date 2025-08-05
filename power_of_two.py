def powerOfTwo(num):
    if(num<1):
        return False
    elif(num == 1):
        return True
    else:
        while(num%2 == 0):
            num = num/2

        if(num == 1):
            return True
        else:
            return False
            
number = int(input("Enter a number: "))

if powerOfTwo(number):
    print(f"{number} is a power of 2.")
else:
    print(f"{number} is not a power of 2.")