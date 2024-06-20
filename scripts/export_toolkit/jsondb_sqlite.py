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
import sqlite3

def main():
    parser = argparse.ArgumentParser(description="Convert JSONdb database to sqlite3 database")
    parser.add_argument("database", help="JSONdb database file")
    parser.add_argument("output", help="Output file")
    args = parser.parse_args()
    
    db = JSONdb(args.database)
    conn = sqlite3.connect(args.output)
    c = conn.cursor()
    
    meta = db.getMeta()
    tableName = meta["name"]

    columns = []
    column_names = []
    for column in meta["columns"]:
        col = meta["columns"][column]
        columnType = col["type"]
        columnName = col["name"]
        column_names.append(columnName)
        
        if columnType == "STRING":
            columnType = "TEXT"
        elif columnType == "FLOAT":
            columnType = "REAL"
        elif columnType == "INTEGER":
            columnType = "INTEGER"
        
        columns.append(f"{columnName} {columnType}")
    
    c.execute(f"CREATE TABLE IF NOT EXISTS {tableName} ({', '.join(columns)})")

    data = db.getData()

    num_columns = len(column_names)
    for row_idx in range(len(data['0'])):
        values = []
        for col_idx in range(num_columns):
            value = data[str(col_idx)][row_idx]
            if isinstance(value, str):
                value = f"'{value}'"
            values.append(value)
        
        query = f"INSERT INTO {tableName} ({', '.join(column_names)}) VALUES ({', '.join(map(str, values))})"
        print(query)
        c.execute(query)

    conn.commit()
    conn.close()
    print(f"Database converted to sqlite3: {args.output}")

if __name__ == "__main__":
    main()
