import os

from .common import file_operation;

def search_entries(file_path):
    keyword = input("Enter keyword to search: ")
    print(f"\nSearching for '{keyword}'")
    found = False
    
    for filename in os.listdir(file_path):
        if filename.endswith(".txt"):
            contents = file_operation(f"{file_path}/{filename}", 'r', '')
            if keyword.lower() in contents.lower():
                print(f"Found in {filename}")
                print(contents)
                found = True
            
    if not found:
        print(f"No entries found containing '{keyword}'.")