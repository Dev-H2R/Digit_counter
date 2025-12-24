def count_digits(number):
    count = 0
    if number == 0:
        return 1
    number = abs(number)
    while number > 0:
        count += 1
        number //= 10   

    return count

num = int(input("Enter a number: "))
result = count_digits(num)
print("Number of digits:", result)
