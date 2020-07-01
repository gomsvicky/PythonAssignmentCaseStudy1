num =int(input("Enter a number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, " is not a prime number")
            break
    else:
        print(num, " is prime number")
    print("Generated prime number till ", num)
    for i in range(2, num):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

else:
    print("Value should be grater than 1")
