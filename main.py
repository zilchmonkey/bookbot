import sys
from stats import sorted_report

def get_book_text(path):

    with open(path) as f:
        content = f.read()

    return content

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        sorted_report(sys.argv[1])
main()