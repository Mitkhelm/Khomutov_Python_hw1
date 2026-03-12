fizz_buzz = int(input("Введите число: "))

def check(fizz_buzz):
    for x in range(1, fizz_buzz + 1):
        if ((x % 3 == 0) and (x % 5 == 0)):
            print(f"FizzBuzz")
        elif x % 5 == 0:
            print(f"Buzz")
        elif x % 3 == 0:
            print(f"Fizz")
        else:
            print(x)
check(fizz_buzz)