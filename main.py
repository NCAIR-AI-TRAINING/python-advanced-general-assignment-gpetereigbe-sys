from datetime import datetime
import os

class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w"):
            pass

def get_last_visitor():
    if not os.path.exists(FILENAME):
        return None, None

    with open(FILENAME, "r") as f:
        lines = f.readlines()
        if not lines:
            return None, None

        last_line = lines[-1].strip()
        if " | " in last_line:
            name, time_str = last_line.split(" | ")
            return name, datetime.fromisoformat(time_str)

    return None, None

def add_visitor(visitor_name):
    last_name, last_time = get_last_visitor()

    # --- Duplicate visitor logic ---
    if last_name == visitor_name:
        raise DuplicateVisitorError(f"{visitor_name} already visited.")
    # --------------------------------

    now = datetime.now()

    # --- 5-minute rule ---
    if last_time and (now - last_time).total_seconds() < 5 * 60:
        raise EarlyEntryError(f"Cannot add {visitor_name}: last visit was within 5 minutes.")
    # ---------------------

    # Append visitor
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name} | {now.isoformat()}\n")

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
