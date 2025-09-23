def find_digits_in_number(num):
    total_digits_in_number = 0
    while num!=0:
        num = num // 10
        total_digits_in_number += 1
    return total_digits_in_number

def isArmstrong(num):
    num_copy = num
    total_digits_in_number = find_digits_in_number(num)
    sum = 0
    while num!=0:
        last_digit_of_number = num % 10
        sum = sum + (last_digit_of_number ** total_digits_in_number)

        num = num // 10
    return sum==num_copy

def display_result(num):
    if isArmstrong(num):
        print(f"Number {num} is ARMSTRONG NUMBER.")
    else:
        print(f"Number {num} is NOT ARMSTRONG NUMBER.")

def main():
    print("Please enter a number: ")
    number = int(input())

    display_result(number)

main()