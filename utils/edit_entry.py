import os

from .common import get_date_input, file_operation
from utils.list_entries import list_entries;

message = """What would you like to do?")
1. Append new information
2. Overwrite entire entry"""

def edit_entry(file_path):
    print(list_entries(file_path))
    date = get_date_input()
    filename = f"{file_path}/{date}.txt"
    print(message)
    if os.path.exists(filename):        
        choice = input("Choose an option (1 or 2): ")
        if choice == '1':
            mode = 'a'
        elif  choice == '2':
            mode = 'w'
        else:
            print("Invalid choice. No changes made.")
            return 
            
        file_operation(filename, mode, "Write your new entry (Type 'END' to finish):")
    else:
        print(f"No entry found for {date}.")