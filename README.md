# JSONdb

Create databases using JSON files

## Installation

### Python

git clone this repository and run the following command in the root directory:

```bash
pip install .
```

### Java

Download the jar file from the releases page and add it to your project or build the jar file from the source code.

```bash
mvn clean package
```

You can also use the makefile to build the jar file:

```bash
make build-jar
```

## Usage

The general usage of the library is the same for both Python and Java. The only difference is the syntax.

### Creating and accessing a database

```python
from JSONdb import JSONdb

db = JSONdb("database.json")
```

This creates a JSONdb object with the specified file. If the file does not exist, it will be created on the first write operation.

#### Autosave

By default, the database is saved after every write operation. You can disable this by setting the autosave parameter to False:

```python
db = JSONdb("database.json", autosave=False)
```

You can manually save the database with the following command:

```python
db.saveDatabase()
```

### Initializing a table

If the database is empty then you can initialize a table with the following command:

```python
db.init("NAME", "DESCRIPTION"]
```

This outputs the following JSON structure:

```json
{
    "meta": {
        "name": "NAME",
        "description": "DESCRIPTION",
        "columns": {}
    },
    "data": {}
}
```

In this demo lets use a more concrete example:

```python
db.init("Products", "A demo database for products")
```

```json
{
    "meta": {
        "name": "Products",
        "description": "A demo database for products",
        "columns": {}
    },
    "data": {}
}
```

### Adding columns to a table

You can add columns to a table with the following command:

```python
db.createColumn("NAME", "DATATYPE", "DESCRIPTION")
```

For example:

```python
db.createColumn("name", "STRING", "The name of the product")
```

This outputs the following JSON structure:

```json
{
    "meta": {
        "name": "Products",
        "description": "A demo database for products",
        "columns": {
            "0": {
                "name": "product",
                "type": "STRING",
                "description": "The name of the product"
            }
        }
    },
    "data": {
        "0": []
    }
}
```

Note how JSONdb has automatically assigned an ID to the column. This is because the column ID is used to reference the data in the table.

#### Data types

In order for JSONdb to work properly, you must use the following data types:
- STRING
- INTEGER
- FLOAT
- BOOLEAN

### Adding data to a table

You can add data to a table with the following command:

```python
db.insertItems(0, ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon"])
```

This outputs the following JSON structure:

```json
{
    "meta": {
        "name": "Products",
        "description": "A demo database for products",
        "columns": {
            "0": {
                "name": "product",
                "type": "STRING",
                "description": "The name of the product"
            }
        }
    },
    "data": {
        "0": ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon"]
    }
}
```

### Querying data

#### Fetching a column

You can fetch a column with the following command:

```python
db.get(0)
```

This outputs the following JSON structure:

```json
["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon"]
```

#### Fetching a single item

You can fetch a single item with the following command:

```python
db.getItem(0, 2)
```

This outputs the following JSON structure:

```json
"Orange"
```

#### Metadata

You can fetch the metadata of a table with the following command:

```python
db.meta()
```

This outputs the following JSON structure:

```json
{
    "name": "Products",
    "description": "A demo database for products",
    "columns": {
        "0": {
            "name": "product",
            "type": "STRING",
            "description": "The name of the product"
        }
    }
}
```

### Get all data

You can get all the data in a table with the following command:

```python
db.data()
```

This outputs the following JSON structure:

```json
{
    "0": ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon"]
}
```

### Deleting a column

You can delete a column with the following command:

```python
db.clear(0)
```

This will remove all the data in the column.

### Deleting a item

You can delete a item with the following command:

```python
db.delete(0, 2)
```

This will remove the item at the specified index. In this case, it will remove "Orange".

## Licence

This project is licenced under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details.