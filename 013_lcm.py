def find_lcm(first_number, second_number):
    if first_number > second_number:
        larger_number = first_number
        smaller_number = second_number
    else:
        larger_number = second_number
        smaller_number = first_number
    
    multiple = 1
    while True:
        if (larger_number*multiple)%smaller_number==0:
            lcm = larger_number*multiple
            break
        multiple+=1
    return lcm

def display_result(first_number, second_number):
    print(f"LCM of {first_number} and {second_number} = {find_lcm(first_number, second_number)}")

def main():
    print("Please enter the first number: ")
    first_num = int(input())

    print("Please enter the second number: ")
    second_num = int(input())

    display_result(first_num, second_num)

main()