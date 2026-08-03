import json
from typing import List, Dict, Any, Optional

USER_DATA_FILE = "users.json"


def load_users(filepath: str = USER_DATA_FILE) -> Optional[List[Dict[str, Any]]]:
    """
    Loads and returns user data from the specified JSON file.

    Returns:
        List of user dictionaries if successful, None otherwise.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: '{filepath}' file not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filepath}'. Check file format.")
    return None


def filter_users(users: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """
    Filters a list of user dictionaries by key and value.

    - Strings are compared case-insensitively.
    - Non-string types use exact equality.
    """
    if isinstance(value, str):
        target = value.lower()
        return [
            user for user in users
            if str(user.get(key, "")).lower() == target
        ]
    return [user for user in users if user.get(key) == value]


def display_results(results: List[Dict[str, Any]], key: str, value: Any) -> None:
    """Prints filtered user results to standard output."""
    if results:
        print(f"\n--- Users matching {key}: {value} ---")
        for user in results:
            print(user)
    else:
        print(f"\nNo users found with {key}: {value}")


def main() -> None:
    """Main execution loop for user filtering CLI."""
    users = load_users()
    if users is None:
        return

    print("Welcome to the User Filter.")
    filter_option = input("What would you like to filter by? ('name', 'age', or 'email'): ").strip().lower()

    if filter_option in ("name", "email"):
        search_val = input(f"Enter a {filter_option} to filter users: ").strip()
        filtered = filter_users(users, filter_option, search_val)
        display_results(filtered, filter_option, search_val)

    elif filter_option == "age":
        raw_age = input("Enter an age to filter users: ").strip()
        try:
            age_int = int(raw_age)
            filtered = filter_users(users, "age", age_int)
            display_results(filtered, "age", age_int)
        except ValueError:
            print("Error: Age must be a valid integer.")

    else:
        print(f"Filtering by '{filter_option}' is not supported. Please choose 'name', 'age', or 'email'.")


if __name__ == "__main__":
    main()