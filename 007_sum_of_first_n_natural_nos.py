def calc_sum(num):
    sum = 0
    for i in range(1, num+1, 1):
        sum += i
    return sum

def print_result(num):
    print(f"Sum of first {num} natural numbers = {calc_sum(num)}")

def main():
    print("Please enter the natural number till where sum is required: ")
    nat_num = int(input())

    print_result(nat_num)

main()
    