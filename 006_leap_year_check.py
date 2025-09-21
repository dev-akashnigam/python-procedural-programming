def isLeapYear(year):
    if year%100 == 0:
        if year%400 == 0:
            return True
        else:
            return False
    else:
        if year%4 == 0:
            return True
        else:
            return False
        
def displayResult(year):
    if isLeapYear(year):
        print(f"Year: {year} is a leap year")
    else:
        print(f"Year: {year} is NOT leap year")

def main():
    print("Please enter the year: ")
    year = int(input())

    displayResult(year)

main()