def isEven(num):
    return num%2 == 0

def displayResult(num):
    if isEven(num):
        print(f"Number: {num} is even.")
    else:
        print(f"Number: {num} is odd.")

def main():
    print("Please enter a number: ")
    num = int(input())

    displayResult(num)

main()