# 1.uzdevums - Izdrukāt virknīti 1,2,3,4,Fizz,6,Buzz,8,.....34,FizzBuzz,36,....līdz  97,Buzz, 99,Fizz

try:
    string_of_number = int(
        input("Please enter the number that you would like to check: ")
    )
    n = string_of_number

    for i in range(1, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 7 == 0:
            print("Buzz")
        else:
            print(i)
except ValueError:
    print("Sorry you did not enter an integer")


print("-----------------")

# 2.uzdevums ievadiet eglītes augstumu un izdrukājiet ar zvaigznīti

tree_height = int(input("Please specify the tree's height: "))

for i in range(1, tree_height + 1):
    print("*" * i)

print("-----------------")

# 3.uzdevums atrodiet vai ievadītais veselais pozitīvais skaitlis ir pirmskaitlis

#positive_integer = int(input("Please enter any number that you would like to check: "))
#if positive_integer >= 1: #pārbauda vai skaitlis ir pozitīvs
