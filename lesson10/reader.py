import os
import sys
import csv
import json
import pickle
from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, dest_path):
        pass

    def apply_changes(self, changes):
        for change in changes:
            try:
                col, row, value = change.split(",", 2)
                col = int(col.strip())
                row = int(row.strip())
                value = value.strip()

                while row >= len(self.data):
                    self.data.append([])
                while col >= len(self.data[row]):
                    self.data[row].append("")

                self.data[row][col] = value

            except Exception as e:
                print(f"Invalid change format '{change}': {e}")


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.data = [row for row in reader]

    def write(self, dest_path):
        with open(dest_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def write(self, dest_path):
        with open(dest_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)


class PickleHandler(FileHandler):
    def read(self):
        with open(self.filepath, 'rb') as f:
            self.data = pickle.load(f)

    def write(self, dest_path):
        with open(dest_path, 'wb') as f:
            pickle.dump(self.data, f)


def get_handler(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.csv':
        return CSVHandler(filepath)
    elif ext == '.json':
        return JSONHandler(filepath)
    elif ext == '.pickle':
        return PickleHandler(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def list_files_in_directory(filepath):
    directory = os.path.dirname(filepath) or "."
    print(f"Listing files in {directory}:")
    for f in os.listdir(directory):
        print("  ", f)


def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <source> <destination> [changes...]")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.isfile(src):
        print(f"Source file '{src}' does not exist or is not a file.")
        list_files_in_directory(src)
        sys.exit(1)

    try:
        handler = get_handler(src)
        handler.read()
        print("\n Original File Content:")
        for row in handler.data:
            print(row)

        handler.apply_changes(changes)

        print("\n Modified File Content:")
        for row in handler.data:
            print(row)

        handler_dst = get_handler(dst)
        handler_dst.data = handler.data
        handler_dst.write(dst)
        print(f"\n💾 File saved to {dst}")

    except Exception as e:
        print(f" Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()