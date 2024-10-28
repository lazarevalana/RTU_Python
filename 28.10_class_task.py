# 1a. Uzrakstīt funkciju: get_char_count(text), kas saņem string un izvada vārdnīcu ar atsevišķu burtu lietojumu skaitu.

def get_char_count(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.setdefault(char, 0) + 1

    return char_count


print(get_char_count("hubba bubba"))


# 1b. Uzrakstīt funkciju: get_digit_dict(num), kas saņem veselu skaitli kā parametru(var būt ļoti liels funkcija  izvada ciparu izmantojumu skaitlī vārdnīcas formā)

def get_digit_dict(num):
    num_str = str(num)
    digit_count = {str(i): 0 for i in range(10)}

    for digit in num_str:
        digit_count[digit] += 1

    return digit_count


print(get_digit_dict(599637003))

# 2. 2. Vārdnīcu labotājs
def replace_dict_value(d, bad_val, good_val):
    for key in d:
        if d[key] == bad_val:  # ja vardnīcas vērtība ir bad_val
            d[key] = good_val  # tad aizstāj ar good_val
    return d


result = replace_dict_value({"a": 5, "b": 6, "c": 5}, 5, 10)
print(result)

# Kopas 2.uzdevums

def get_common_elements(seq1, seq2, seq3):
    common_elements = set(seq1) & set(seq2) & set(seq3)
    return tuple(common_elements)


print(get_common_elements("abc", ["a", "b"], ("b", "c")))
