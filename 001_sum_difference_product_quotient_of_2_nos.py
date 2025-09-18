def printResults(numX, numY):
    sum = numX + numY
    diff = numX - numY
    product = numX * numY
    quotient = numX / numY

    print(f"Sum = {sum}")
    print(f"Difference = {diff}")
    print(f"Product = {product}")
    print(f"Quotient = {quotient}")

def main():
    print("Please enter first number: ")
    first_num = int(input())

    print("Please enter second number: ")
    second_num = int(input())

    printResults(first_num, second_num)

main()


