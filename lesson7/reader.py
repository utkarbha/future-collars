import sys
import os
import csv

def print_usage_and_exit():
    print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
    sys.exit(1)

def show_directory_files(src_path):
    directory = os.path.dirname(os.path.abspath(src_path)) or "."
    print(f"'{src_path}' is not a valid file. Available files in '{directory}':")
    for filename in os.listdir(directory):
        print(f"- {filename}")

def apply_changes(data, changes):
    for change in changes:
        try:
            col_str, row_str, value = change.split(",", 2)
            col, row = int(col_str), int(row_str)

            if row < 0 or row >= len(data):
                print(f"Skipping change '{change}': row {row} out of bounds.")
                continue
            if col < 0 or col >= len(data[row]):
                print(f"Skipping change '{change}': column {col} out of bounds.")
                continue

            data[row][col] = value
        except ValueError:
            print(f"Skipping invalid change format: '{change}'. Expected format 'X,Y,value'.")

def print_csv_data(data):
    for row in data:
        print(",".join(row))

def main():
    if len(sys.argv) < 3:
        print_usage_and_exit()

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.isfile(src):
        show_directory_files(src)
        sys.exit(1)

    try:
        with open(src, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = [row for row in reader]
    except Exception as e:
        print(f"Error reading from '{src}': {e}")
        sys.exit(1)

    apply_changes(data, changes)

    print("Modified CSV content:")
    print_csv_data(data)

    try:
        with open(dst, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"\nModified CSV saved to '{dst}'")
    except Exception as e:
        print(f"Error writing to '{dst}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()