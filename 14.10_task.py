# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru

body_temperature = float(input("Please enter your body temperature: "))

if body_temperature < 35:
    print(
        f"Are you cold, given that your body temperature is {body_temperature} degrees?"
    )
elif 35 <= body_temperature <= 37:
    print(f"Your body temperature {body_temperature} is great!")
else:
    print(
        f"Your body temperature is {body_temperature}. It appears that you have fever!"
    )

print("-----------------")

# 2. uzdevums noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu

monthly_salary = float(input("Please enter your monthly salary: "))
work_experience = float(input("How many years you have been employed? "))

if work_experience > 2:
    eligible_years = int(
        work_experience - 2
    )  # during the first two years, we are not earning bonuses.
    bonus = monthly_salary * eligible_years * 0.15
    print(f"You are eligible for a yearly bonus! Your bonus is {bonus:.2f}!")
else:
    print("Sorry, but you are not eligible for the bonus")

print("-----------------")

# 3. uzdevums noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā (<= mazaks vai vienads)

number1 = float(input("Please enter first number: "))
number2 = float(input("Please enter second number: "))
number3 = float(input("Please enter third number: "))

if number1 <= number2 and number1 <= number3:
    print(
        f"Number order are {number1}, {min(number2, number3)}, {max(number2, number3)}"
    )
elif number2 <= number1 and number2 <= number3:
    print(
        f"Number order are {number2}, {min(number1, number3)}, {max(number1, number3)}"
    )
else:
    print(
        f"Number order are {number3}, {min(number1, number2)}, {max(number1, number2)}"
    )
