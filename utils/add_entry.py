import os

from datetime import datetime

from .common import file_operation;

def add_entry(file_path):
    # current_date = datetime.now()
    # date = current_date.strftime("%Y-%m-%d")
    date = input("Enter a date in YYYY-MM-DD format: ")
    filename = f"{file_path}/{date}.txt"
    
    if os.path.exists(filename):
        overwrite = input("Already exist. Do you want to overwrite (O) or append (A)? ").lower()
        if overwrite == 'o':
            mode = 'w'
        elif overwrite == 'a':
            mode = 'a'
        else:
            print("Invalid option.")
            return
    else:
        mode = 'w'
    
    message = """Write your entry (tasks, notes, or thoughts):
Type 'END' on a new line to save and exit."""
    
    file_operation(filename, mode, message)
    