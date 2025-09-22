def get_reversed_number(num):
    original_number = num
    reversed_number = 0

    while original_number!=0:
        last_digit = original_number % 10
        reversed_number = reversed_number * 10 + last_digit

        original_number = original_number // 10
    return reversed_number

def display_result(num):
    print(f"Reverse of number {num} = {get_reversed_number(num)}")

def main():
    print("Please enter a number: ")
    num = int(input()) 

    display_result(num)

main()