# 1.a Vidējā vērtība, uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).

random_number = input("Lūdzu ievadi vairākus skaitļus: ")

try:
    numbers = [float(num) for num in random_number.split()]
    average_numbers = sum(numbers) / len(numbers)

    print(f"Vidējais skaitlis ir: {average_numbers}")
except ValueError:
    print("Lūdzu ievadi derīgus skaitļus.")

print("-----------------")

# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus, iziešana ir ievadot "q"

numbers = []

while True:
    random_number = input(
        'Lūdzu ievadi vairākus skaitļus, ja gribi iziet, raksti "q": '
    )

    if random_number.lower() == "q":
        break

    try:
        entered_numbers = [float(num) for num in random_number.split()]
        numbers.extend(entered_numbers)

        average_numbers = sum(numbers) / len(numbers)

        print(f"Vidējā vērtība: {average_numbers}")
        print(f"Visi ievadītie skaitļi: {numbers}")
    except ValueError:
        print("Lūdzu ievadi derīgus skaitļus.")

print("-----------------")

# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.

numbers = []

while True:
    random_number = input(
        'Lūdzu ievadi vairākus skaitļus, ja gribi iziet, raksti "q": '
    )

    if random_number.lower() == "q":
        break

    try:
        entered_numbers = [float(num) for num in random_number.split()]
        numbers.extend(entered_numbers)

        average_numbers = sum(numbers) / len(numbers)

        sorted_numbers = sorted(numbers)
        TOP3 = sorted_numbers[-3:]
        BOTTOM3 = sorted_numbers[:3]

        # Izvadām vidējo vērtību, TOP3 un BOTTOM3
        print(f"Vidējā vērtība: {average_numbers}")
        print(f"TOP 3 skaitļi: {TOP3}")
        print(f"BOTTOM 3 skaitļi: {BOTTOM3}")
    except ValueError:
        print("Lūdzu ievadi derīgus skaitļus.")

print("-----------------")

# 2. Kubu tabula

start_number = int(input("Ievadi sākuma skaitli: "))
end_number = int(input("Ievadi beigu skaitli: "))

cubs = []

for num in range(start_number, end_number + 1):
    cube = num**3
    cubs.append(cube)
    print(f"{num} kubā: {cube}")

print(f"Visi kubi: {cubs}")


# 3.
#sentence = input("Ievadi teikumu: ")
