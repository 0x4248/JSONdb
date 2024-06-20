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
import xml.etree.ElementTree as ET

def main():
    parser = argparse.ArgumentParser(description="Convert JSONdb database to XML")
    parser.add_argument("database", help="JSONdb database file")
    parser.add_argument("output", help="Output XML file")
    args = parser.parse_args()

    db = JSONdb(args.database)
    root = ET.Element(db.getMeta()["name"])

    root = ET.Element("database")

    columns = db.getMeta()["columns"]
    column_names = [columns[col]["name"] for col in columns]

    data = db.getData()

    num_columns = len(column_names)
    for row_idx in range(len(data['0'])):
        row = ET.SubElement(root, "row")
        for col_idx in range(num_columns):
            col = ET.SubElement(row, column_names[col_idx])
            try:
                col.text = str(data[str(col_idx)][row_idx])
            except IndexError:
                col.text = ""

    tree = ET.ElementTree(root)
    tree.write(args.output, encoding="utf-8", xml_declaration=True, method="xml")


    print("Database converted to XML")

if __name__ == "__main__":
    main()