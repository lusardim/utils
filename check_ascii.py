import argparse
import os.path
from pathlib import Path
from typing import Optional


def process_dir(directory: str, filter: Optional[str] = "*"):
    root_dir = Path(directory)
    for each_file in root_dir.glob(f"**/{filter}"):
        printed_filename = False
        if each_file.is_file():
            with open(each_file, encoding="ascii", errors='replace') as f:
                for num, line in enumerate(f, 1):
                    if '\ufffd' in line:
                        if not printed_filename:
                            print(f"{each_file} has non ascii characters")
                            printed_filename = True
                        print(f"{num}: {line}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Non Ascii detector",
                                     description="This utility checks for a list of non ascii chars in a directory",
                                     epilog="Example check_ascii -f '*.html' . will verify all html files")
    parser.add_argument("-f", help="filter", type=str)
    parser.add_argument("directory", help="Path of the root directory to scan")

    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        print("Invalid directory")
        exit(1)
    process_dir(args.directory, args.f)
