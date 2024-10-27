# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30


def add_mult(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    result = (numbers[0] + numbers[1]) * numbers[2]
    return result


a = float(input("Ievdadiet pirmo ciparu: "))
b = float(input("Ievdadiet otro ciparu: "))
c = float(input("Ievdadiet trešo ciparu: "))

print(f"Rezultāts ir: {add_mult(a, b, c)}")

# 2. Palindroms
# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira      sula") -> True


print("-----------------")


# 2. Palindroms
# let's create a function that returns only letters from the text
def only_letters(text: str) -> str:
    # we can use list comprehension to create a list of letters
    # we can use isalpha() method to check if the character is a letter
    # we can use lower() method to convert the letter to lower case
    # return "".join([letter.lower() for letter in text if letter.isalpha()])
    # we can use regular lists
    letters = []
    for letter in text:
        if letter.isalpha():
            letters.append(letter)
    # i have a list but I need a string with no spaces
    # I can use join method of the string to join the list of letters
    # in order for join to work
    #  I need to provide a string that will be used to join the list
    # also list should contain only strings
    return "".join(letters).lower()


def is_palindrome(text: str) -> bool:
    # list = []
    # for item in text:
    # #rev_item = item[::-1]
    #     if item != ' ':
    #         list.append(item.capitalize())
    # we can normalize the text by removing spaces and converting to lower case
    normalized_text = only_letters(text)
    normalized_text = normalized_text.lower()
    # above we did two operations in one line first we removed spaces and then converted to lower case
    reversed_text = normalized_text[::-1]
    # if normalized_text == reversed_text:
    #     result = True
    # else:
    #     result = False
    # # print(result)
    return normalized_text == reversed_text


is_palindrome("Alus ari ira      sula")
result = is_palindrome("Alus ari ira      sula")

print("Result", result)
print(is_palindrome("abracabra dfee"))  # False
panama = "A man, a plan, a canal – Panama"
print(is_palindrome(panama))  # True

# let's try with Latvian
print(is_palindrome("Āri irā!    ...."))  # True

print("-----------------")

# 3. uzdevums

def get_city_year(p0: int, perc: float, delta: int, p: int) -> int:
    years = 0
    growth_rate = perc / 100  # pārvērš procentus decimāl skaitlī

    while p0 < p:
        new_population = p0 + p0 * growth_rate + delta  # nākamā gada iedzīvotāju skaitu

        years += 1

        if new_population <= p0:  # p nevar sasniegt
            return -1

        p0 = new_population

    return years


# Testa piemēri
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))
