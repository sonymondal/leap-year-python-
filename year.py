# check leap year

year = int(input("Enter A Year: "))

if year % 400 == 0 or year % 4 == 0:
    print("%d is a Leap Year."%year)
else:
    print("%d is not a Leap Year."%year)


# check prime numbers

number = int(input("Enter a number: "))

if number ==  2  or number % 2 == 1:
    print("%d is a prime number."%number)
else:
    print("%d is not a prime number."%number)


# check lcm  of numbers
firstNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter another number: "))

def calculateLCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm 
results = calculateLCM(firstNumber, secondNumber)
print("The L.C.M of %d & %d is %d" %(firstNumber, secondNumber,results))


# check gcd or hcf  of numbers 

firstNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter another number: "))

def calculateHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x 
    
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf
results = calculateHCF(firstNumber, secondNumber)
print("The H.C.F of %d & %d is %d" %(firstNumber, secondNumber, results))
