import os

from utils.add_entry import add_entry
from utils.view_entry import view_entry
from utils.edit_entry import edit_entry
from utils.search_entries import search_entries
from utils.list_entries import list_entries

main_string = """\n\nWelcome to your Personal Diary!
Choose an option:
1. Add new entry
2. View entry
3. Edit entry
4. Search entries
5. List all entries
6. Exit\n"""

file_path = "Diary"
if not os.path.exists(file_path):
    os.makedirs(file_path)


def quit_application():
    print("Goodbye!")
    quit()


def main():
    while True:
        print(main_string)
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_entry(file_path)
        elif choice == "2":
            view_entry(file_path)
        elif choice == "3":
            edit_entry(file_path)
        elif choice == "4":
            search_entries(file_path)
        elif choice == "5":
            list_entries(file_path)
        elif choice == "6":
            quit_application()
        else:
            print("Invalid choice. Please choose a valid option.")

        user_input = input("Do you want to try again? (y/n): ").lower()

        if user_input != "y":
            quit_application()


if __name__ == "__main__":
    main()
