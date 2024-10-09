"""
This is a first practical task
"""
# Izdrukājiet savu vārdu 5 reizes
# Aprēķiniet cik sekundes būs šogad (366 dienas šogad!)
# Kas notiks ja mēģināsiet reizināt savu vārdu ar kādu pozitīvu skaitli, piem. 7 ?
# Izdrukājiet "Banana" bet izmantojot tikai "Ba" un "na"

# 1. Izdrukājiet savu vārdu 5 reizes
print("Lana " * 5)

# vai arī definēt kā variable

NAME = "Lana"

print(f"{NAME} " * 5)

# 2. Aprēķiniet cik sekundes būs šogad (366 dienas šogad!)

DAYS = 366  # dienu skaits gadā

# Aprēķinām kopējās sekundes (dienas * stundu skaits * minūšu skaits stundā * sekunžu skaits minūtē)
SECONDS = DAYS * 24 * 60 * 60

print(f"Šogad ir {SECONDS} sekundes")

# 3. Kas notiks ja mēģināsiet reizināt savu vārdu ar kādu pozitīvu skaitli, piem. 7 ?
print("Lana " * 7)  # Izprintēs vārdu 7X

# 4. Izdrukājiet "Banana" bet izmantojot tikai "Ba" un "na"

# variables
BA = "Ba"
NA = "na"

BANANA = BA + (NA * 2)
print("BANANA")
