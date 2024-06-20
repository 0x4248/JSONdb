# JSONdb
# Create databases using JSON files
# Github: https://www.github.com/0x4248/JSONdb
# Licence: GNU General Public License v3.0
# By: 0x4248

try:
    from JSONdb import JSONdb
except ImportError:
    print("JSONdb module not found. Please install JSONdb module before running this script.")

import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Convert JSONdb database to plain JSON file")
    parser.add_argument("database", help="JSONdb database file")
    parser.add_argument("output", help="Output file")
    args = parser.parse_args()
    
    db = JSONdb(args.database)
    data = db.getData()

    columns = db.getMeta()["columns"]
    column_names = [columns[col]["name"] for col in columns]
    data = {column_names[col]: data[str(col)] for col in range(len(column_names))}

    with open(args.output, "w") as f:
        json.dump(data, f, indent=4)
if __name__ == "__main__":
    main()