import os

def list_entries(file_path):
    print("\nList of all diary entries:")
    entries = [f for f in os.listdir(file_path) if f.endswith(".txt")]
    
    if entries:
        for entry in entries:
            print(entry.replace(".txt", ""))
    else:
        print("No entries found.")