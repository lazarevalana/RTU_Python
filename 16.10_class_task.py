# 1.uzdevums - Lietotājs ievada vārdu - tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu

your_name = input("Lūdzu ievadi savu vārdu: ")

reversed_name = your_name[::-1].capitalize()
first_letter = your_name[0].upper()
print(f"{reversed_name}, pamatīgs juceklis vai ne {first_letter}?")

# print("-----------------")

# 2.uzdevums - Lietotājs ievada tekstu, tiek izvadītas tikai zvaigznītes burtu vietā
random_text = input("1. spēlētājs - lūdzu ievadi tekstu: ")

new_random_text = ""
for char in random_text:
    if char == " ":
        new_random_text += " "
    else:
        new_random_text += "*"
print(new_random_text)

random_letter = input("2. spēlētājs - lūdzu ievadi simbolu: ")

revealed_text = ""
for char in random_text:
    if char == random_letter:
        revealed_text += char
    elif char == " ":
        revealed_text += " "
    else:
        revealed_text += "*"

print(revealed_text)

# print("-----------------")
