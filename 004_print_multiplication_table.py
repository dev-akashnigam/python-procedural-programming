def printTable(num):
    for i in range(1, 11, 1):
        print(f"{num} X {i} = {num*i}")

def main():
    print("Please enter a number: ")
    num = int(input())

    printTable(num)

main()