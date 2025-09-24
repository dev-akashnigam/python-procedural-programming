def print_solid_square(row_count):
    col_count = row_count
    for row in range(1, row_count+1, 1):
        for col in range(1, col_count+1, 1):
            print("*", end=" ")
        print()

def main():
    print("Please enter the number of rows required in the solid square pattern: ")
    rows = int(input())

    print_solid_square(rows)

main()