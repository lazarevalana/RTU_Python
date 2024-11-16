"""This Python script downloads an Excel file from Google Drive and analyzes food data.
Users can filter items by country, view the most and least expensive foods, calculate average price
and sort items by price. Code uses gdown library for downloading file and pandas for data processing.
Python version: 3.9"""

# Importing libraries
import gdown  # gdown is used to download files from Google Drive
import pandas as pd

# Defining variables (full URL - https://drive.google.com/file/d/1Ylj9xYrEp2v5S-iyCTgoVMTNGHjo8kAE/view?usp=drive_link)
file_id = "1Ylj9xYrEp2v5S-iyCTgoVMTNGHjo8kAE"
file_name = "food_analysis.xlsx"
url = f"https://drive.google.com/uc?export=download&id={file_id}"


def download_file(file_name):  # Function to download Excel file from Google Drive
    try:
        gdown.download(url, file_name, quiet=True)
        print(f"File downloaded successfully and saved as {file_name}")
    except Exception as e:
        print(f"Error occurred: {e}")


def load_data(file_name):  # Function to load data as pandas DataFrame
    df = pd.read_excel(file_name)
    print(
        "\nWhat type of food would you like to see?, possible options",
        df["country"].unique(),
    )

    while (
        True
    ):  # keep prompting user until valid country is entered (no spelling mistakes)
        country = input("Enter a country from the list: ").strip()
        filtered_df = filter_by_country(df, country)
        if not filtered_df.empty:
            return filtered_df
        print(
            f"Sorry, no data found for '{country}'. Please double-check the spelling and try again."
        )


def filter_by_country(
    df, country
):  # Function to filter data by country kitched (America, Asian, Mexican and Italian)
    filtered_data = df[df["country"].str.lower() == country.lower()]
    return filtered_data


def get_most_expensive_food(df):  # Function to get the most expensive food
    most_expensive_product = df[df["price"] == df["price"].max()]
    most_expensive_product = most_expensive_product[["food_name", "price"]]
    return most_expensive_product


def get_cheapest_food(df):  # Function to get the cheapest food
    cheapest_product = df[df["price"] == df["price"].min()]
    cheapest_product = cheapest_product[["food_name", "price"]]
    return cheapest_product


def calculate_average_price(df):  # Function to calculate average price of food
    average_price = df["price"].mean()
    return average_price


def sort_by_price(df, ascending=True):  # Function to sort food by price - ascending
    sorted_data = df.sort_values(by="price", ascending=ascending)
    return sorted_data


def ask_user_preferences(df):  # Function to ask user what they want to see
    while True:
        print("\nWhat would you like to see?")
        print("1. See the food with the highest price")
        print("2. See the food with the lowest price")
        print("3. See the average price")
        print("4. Sort by price")
        print("5. Exit")

        choice = input(
            "Enter the number of your choice: "
        )  # ask user for choice, user must enter a number

        if choice == "1":
            most_expensive = get_most_expensive_food(df)
            print("\nMost Expensive Food:")
            print(most_expensive.to_string(index=False))
        elif choice == "2":
            cheapest = get_cheapest_food(df)
            print("\nCheapest Food:")
            print(cheapest.to_string(index=False))
        elif choice == "3":
            avg_price = calculate_average_price(df)
            print(f"\nAverage Price: {avg_price}")
        elif choice == "4":
            sorted_data = sort_by_price(df, ascending=True)
            print("\nSorted by Price (Ascending):", sorted_data.to_string(index=False))
        elif choice == "5":
            print("Exiting program, goodbye!")
            break
        else:
            print(
                "Invalid choice, please try again."
            )  # if user enters a number that is not in the list

        continue_choice = input(
            "\nDo you want to continue? (Y/N): "
        ).lower()  # ask user if they want to continue
        if continue_choice != "Y".lower():
            print("Exiting program, goodbye!")
            break

download_file(file_name)  # download file
df = load_data(file_name)  # load data
ask_user_preferences(df)  # ask user what they want to see
