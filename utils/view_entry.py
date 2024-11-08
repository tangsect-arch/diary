import os

from .common import get_date_input, file_operation
from utils.list_entries import list_entries;

def view_entry(file_path):
    print(list_entries(file_path))
    date = get_date_input()
    filename = f"{file_path}/{date}.txt"
    
    if os.path.exists(filename):
        contents = file_operation(filename, 'r', '')
        print(contents)
    else:
        print(f"No entry found.")