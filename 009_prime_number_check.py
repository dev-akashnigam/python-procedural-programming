import math

def is_prime(num):
    if num<=1:
        return False
    elif num==2:
        return True
    elif num%2==0:
        return False
    else:
        sqrt_number = math.isqrt(num)
        for i in range(3, sqrt_number+1, 2):
            if num%i==0:
                return False
        return True

def display_result(num):
    if is_prime(num):
        print(f"Number {num} is PRIME.")
    else:
        print(f"Number {num} is NOT PRIME.")

def main():
    print("Please enter a number: ")
    number = int(input())

    display_result(number)

main()