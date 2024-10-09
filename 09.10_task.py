"""
Dienas uzdevumi - mainīgo apstrāde
"""
# Importēju bibliotēku

import datetime

# 1. uzdevums
NAME = input("What is your name? ")
print(f"Nice to meet you, {NAME}! ")

AGE = int(input(f"{NAME}, could you please tell me what age you are? "))
print(f"Your age, {AGE}, is great!")

YEARS_TO_100 = 100 - AGE
print(f"In {YEARS_TO_100} years you will be 100 years old!")

# Izdos pašreizējo gadu
CURRENT_YEAR = datetime.datetime.now().year
YEARS_TO_100 = CURRENT_YEAR + YEARS_TO_100
print(f"{NAME}, you will reach 100 birthdays in {YEARS_TO_100}")

print("-----------------")

# 2.uzdevums

ISTABAS_PLATUMS = float(input("Lūdzu ievadi istabas platumu: "))
ISTABAS_AUGSTUMS = float(input("Lūdzu ievadi istabas augstumu: "))
ISTABAS_GARUMS = float(input("Lūdzu ievadi istabas garumu: "))

TELPAS_TILPUMS = ISTABAS_PLATUMS * ISTABAS_AUGSTUMS * ISTABAS_GARUMS
print(f"Telpas tilpums ir {TELPAS_TILPUMS}!")

print("-----------------")

# 3.uzdevums

CELSIJS = float(input("Lūdzu ievadi temperatūru pēc Celsija: "))
print(f"Gaisa temperatūra pēc celsija ir {CELSIJS}!")

FARANHEITS = 32 + CELSIJS * (9 / 5)
FARANHEITS_ROUNDED = round(FARANHEITS, 2)
print(f"Gaisa temperatūra pēc faranheita ir {FARANHEITS_ROUNDED}")
