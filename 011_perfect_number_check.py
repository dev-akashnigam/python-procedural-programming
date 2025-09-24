def is_perfect(num):
    half_of_number = num // 2
    sum_of_divisors = 0

    for i in range(1, half_of_number+1, 1):
        if num%i==0:
            sum_of_divisors += i
    return sum_of_divisors==num

def display_result(num):
    if is_perfect(num):
        print(f"Number: {num} is a PERFECT NUMBER.")
    else:
        print(f"Number: {num} is NOT PERFECT NUMBER.")
        
def main():
    print("Please enter a number: ")
    number = int(input())

    display_result(number)

main()