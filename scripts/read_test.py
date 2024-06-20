# JSONdb
# Create databases using JSON files
# Github: https://www.github.com/0x4248/JSONdb
# Licence: GNU General Public License v3.0
# By: 0x4248

try:
    from JSONdb import JSONdb
except ImportError:
    print("JSONdb module not found. Please install JSONdb module before running this script.")

def main():
    db = JSONdb("demo.json", True, True, True)
    while True:
        print(db.getData())
        input()

if __name__ == "__main__":
    main()