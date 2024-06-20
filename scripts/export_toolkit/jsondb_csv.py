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

def main():
    parser = argparse.ArgumentParser(description="Convert JSONdb database to CSV")
    parser.add_argument("database", help="JSONdb database file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    db = JSONdb(args.database)
    with open(args.output, "w") as f:
        columns = db.content["meta"]["columns"]
        columnNames = [columns[column]["name"] for column in columns]
        f.write(",".join(columnNames) + "\n")

        data = db.content["data"]
        numRows = len(data["0"])
        for i in range(numRows):
            row = []
            for column in data:
                if i < len(data[column]):
                    row.append(data[column][i])
                else:
                    row.append("")
            f.write(",".join(map(str, row)) + "\n")
            
    print("Database converted to CSV")

if __name__ == "__main__":
    main()