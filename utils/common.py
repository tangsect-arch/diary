import os
from datetime import datetime

def get_date_input():
    while True:
        date_input = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            
def read_file(file_details, mode, message):
    with open(file_details, mode) as file:
        contents = file.read()
        return contents
    
def write_file(file_details, mode, message):
    print(message)
    line = input()
    if line.lower() == 'end':
        with open(file_details, mode) as file:
            while True:
                file.write(line + "\n")
    else:
        return "Input cannot be empty"
    
def file_operation(file_details, mode, message):
    print(message)
    with open(file_details, mode) as file:
        if mode=='r':
            contents = file.read()
            return contents
        else:
            while True:
                line = input()
                if line.lower() == 'end':
                    break
                file.write(line + "\n")
            
