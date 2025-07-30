# Program to check if a given number is a palindrome (e.g., 121, 1331)
def is_palindrome(num):
    if num < 0:
        return False

    x = num
    revNum = 0
    while(x > 0):
        d = x % 10
        revNum = revNum * 10 + d
        x = x // 10

    return revNum == num

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")
