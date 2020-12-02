def collatz(number):
    if number % 2 == 0:

        print(number // 2)
        return number // 2
    else:

        print(3 * number + 1)
        return 3 * number + 1

try:
    num = int(input("Enter integer value:"))
    result = collatz(num)
    while (result != 1):
        result = collatz(result)
except ValueError:
    print("Pls enter Integer values only")
