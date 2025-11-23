from datetime import datetime
import os

class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    pass

def get_last_visitor():
    pass

def add_visitor(visitor_name):
    # --- Duplicate visitor logic added here ---
    last_name, last_time = get_last_visitor()

    if last_name == visitor_name:
        raise DuplicateVisitorError(f"{visitor_name} already visited.")
    # ------------------------------------------

    pass

def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
