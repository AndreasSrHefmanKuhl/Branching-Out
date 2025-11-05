import json

def filter_users_by_name(name):
    """
    Filters users based on an exact, case-insensitive match of their 'name'.
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Error: 'users.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from 'users.json'. Check file format.")
        return

    filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]

    if filtered_users:
        print("\n--- Users matching name: {} ---".format(name))
        for user in filtered_users:
            print(user)
    else:
        print("\nNo users found with the name: {}".format(name))

def filter_users_by_age(age):
    """
    Filters users based on an exact match of their 'age'.
    """
    try:
        age_int = int(age)
    except ValueError:
        print("Error: Age must be a valid number.")
        return

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Error: 'users.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from 'users.json'. Check file format.")
        return

    # Check that user["age"] exists and is an integer before comparison
    filtered_users = [user for user in users if user.get("age") == age_int]

    if filtered_users:
        print("\n--- Users matching age: {} ---".format(age_int))
        for user in filtered_users:
            print(user)
    else:
        print("\nNo users found with the age: {}".format(age_int))

if __name__ == "__main__":
    print("Welcome to the User Filter.")

    filter_option = input("What would you like to filter by? ('name' or 'age'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search) # Call the new function
    else:
        print("Filtering by '{}' is not a supported option. Please choose 'name' or 'age'.".format(filter_option))