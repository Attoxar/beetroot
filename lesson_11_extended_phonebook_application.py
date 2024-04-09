import json
import os


with open("my_phonebook.json", "w") as f:
    f.write("")


def load_phonebook(my_phonebook):
    filename = f"{my_phonebook}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = f.read()
            if data:
                return json.load(f)
            else:
                return []
    else:
        raise FileNotFoundError("Phonebook data not found.")


def save_phonebook(my_phonebook, entries):
    filename = f"{my_phonebook}.json"
    with open(filename, "w") as f:
        json.dump(entries, f, indent=4)


def add_entry(entries):
    entry = {
        'first_name': input("Enter first name: "),
        'last_name': input("Enter last name: "),
        'telephone_number': input("Enter telephone number: "),
        'city': input("Enter city: "),
        'state': input("Enter state: ")
    }
    entries.append(entry)
    print("Entry added successfully.")


def search_by_first_name(entries):
    first_name = input("Enter first name to search: ")
    found_entries = [entry for entry in entries if entry['first_name'] == first_name]
    return found_entries


def search_by_last_name(entries):
    last_name = input("Enter last name to search: ")
    found_entries = [entry for entry in entries if entry['last_name'] == last_name]
    return found_entries


def search_by_full_name(entries):
    full_name = input("Enter full name to search: ")
    found_entries = [entry for entry in entries if f"{entry['first_name']} {entry['last_name']}" == full_name]
    return found_entries


def search_by_telephone_number(entries):
    telephone_number = input("Enter telephone number to search: ")
    found_entries = [entry for entry in entries if entry['telephone_number'] == telephone_number]
    return found_entries


def search_by_city_or_state(entries):
    city_or_state = input("Enter city or state to search: ")
    found_entries = [entry for entry in entries if entry['city'] == city_or_state or entry['state'] == city_or_state]
    return found_entries


def delete_entry(entries):
    telephone_number = input("Enter telephone number to delete: ")
    entries[:] = [entry for entry in entries if entry['telephone_number'] != telephone_number]
    print("Entry deleted successfully.")


def update_entry(entries):
    telephone_number = input("Enter telephone number to update: ")
    for entry in entries:
        if entry['telephone_number'] == telephone_number:
            entry.update({
                'first_name': input("Enter updated first name: "),
                'last_name': input("Enter updated last name: "),
                'city': input("Enter updated city: "),
                'state': input("Enter updated state: ")
            })
            print("Entry updated successfully.")
            return
    print("Entry with the given telephone number not found.")


def exit_program(my_phonebook, entries):
    save_phonebook(my_phonebook, entries)
    print("Phonebook data saved. Exiting program.")


def main(my_phonebook):
    entries = load_phonebook(my_phonebook)

    while True:
        print("\nPhonebook Options:")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete a record")
        print("8. Update a record")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            print(search_by_first_name(entries))
        elif choice == '3':
            print(search_by_last_name(entries))
        elif choice == '4':
            print(search_by_full_name(entries))
        elif choice == '5':
            print(search_by_telephone_number(entries))
        elif choice == '6':
            print(search_by_city_or_state(entries))
        elif choice == '7':
            delete_entry(entries)
        elif choice == '8':
            update_entry(entries)
        elif choice == '9':
            exit_program(my_phonebook, entries)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    my_phonebook = input("Enter the name of the phonebook: ")
    main(my_phonebook)
