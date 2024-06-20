# JSONdb
# Create databases using JSON files
# Github: https://www.github.com/0x4248/JSONdb
# Licence: GNU General Public License v3.0
# By: 0x4248

echo "Generating CSV file from demo.json"
python3 scripts/generate_demo.py
python3 scripts/export_toolkit/jsondb_csv.py demo.json demo.csv

echo "CSV file generated: demo.csv"
cat demo.csv

read -p "Do you want to clean up? (y/n): " clean
if [ "$clean" == "y" ]; then
    rm demo.json demo.csv
    echo "Cleaned up"
fi