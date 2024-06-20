# JSONdb
# Create databases using JSON files
# Github: https://www.github.com/0x4248/JSONdb
# Licence: GNU General Public License v3.0
# By: 0x4248

import json

traceLog = False

class logger:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    GREY = "\033[97m"
    RESET = "\033[0m"
    def log(message):
        if traceLog:
            print(f"[{logger.GREEN}JSONdb{logger.RESET}] {logger.CYAN}LOG:{logger.RESET} {logger.GREY}{message}{logger.RESET}")
    def warn(message):
        if traceLog:
            print(f"[{logger.GREEN}JSONdb{logger.RESET}] {logger.YELLOW}WARN:{logger.RESET} {logger.GREY}{message}{logger.RESET}")
    def error(message):
        if traceLog:
            print(f"[{logger.GREEN}JSONdb{logger.RESET}] {logger.RED}ERROR:{logger.RESET} {logger.GREY}{message}{logger.RESET}")
    

class JSONdb: 
    def __init__(self, databaseName, autosave=True ,autoload=True, traceLogs=False):
        self.contentName = databaseName
        self.content = None
        self.autosave = autosave
        self.autoload = autoload
        global traceLog
        traceLog = traceLogs
        self.loadDatabase()

    def loadDatabase(self):
        try:
            logger.log("Loading database: " + self.contentName)
            with open(self.contentName, "r") as f:
                self.content = json.load(f)
            logger.log("Database loaded successfully with " + str(len(self.content["meta"]["columns"])) + " columns")
        except FileNotFoundError:
            logger.warn("Database was not found and will need to be initialized before use")
    

    def saveDatabase(self):
        logger.log("Saving database: " + self.contentName)
        with open(self.contentName, "w") as f:
            logger.log(message="Dumping content to file")
            json.dump(self.content, f, indent=4)
        logger.log("Database saved successfully")

    def init(self, name, description=""):
        logger.log("Preparing initialization of database")
        self.content = {
            "meta": {
                "name": name,
                "description": description,
                "columns": {}
            },
            "data": {}
        }
        if self.autosave:
            self.saveDatabase()

    def createColumn(self, name, type="STRING", description=""):
        if self.autoload:
            self.loadDatabase()
        columnId = len(self.content["meta"]["columns"])
        self.content["meta"]["columns"][str(columnId)] = {
            "name": name,
            "type": type,
            "description": description
        }
        self.content["data"][str(columnId)] = []
        if self.autosave:
            self.saveDatabase()
        return columnId

    def insert(self, columnId, data):
        logger.log("Inserting data into column " + str(columnId))
        if self.autoload:
            self.loadDatabase()
        if self.content["meta"]["columns"][str(columnId)]["type"] == "INTEGER":
            try:
                data = int(data)
            except ValueError:
                logger.error("Invalid data type")
                return
        elif self.content["meta"]["columns"][str(columnId)]["type"] == "STRING":
            try:
                data = str(data)
            except ValueError:
                logger.error("Invalid data type")
                return
        elif self.content["meta"]["columns"][str(columnId)]["type"] == "FLOAT":
            try:
                data = float(data)
            except ValueError:
                logger.error("Invalid data type")
                return
        elif self.content["meta"]["columns"][str(columnId)]["type"] == "BOOLEAN":
            try:
                data = bool(data)
            except ValueError:
                logger.error("Invalid data type")
                return
        self.content["data"][str(columnId)].append(data)
        logger.log("Data inserted successfully")
        if self.autosave:
            self.saveDatabase()

    def insertItems(self, columnId, data):
        logger.log("Inserting data into column " + str(columnId))
        if self.autoload:
            self.loadDatabase()
        for i in range(len(data)):
            if self.content["meta"]["columns"][str(columnId)]["type"] == "INTEGER":
                try:
                    data[i] = int(data[i])
                except ValueError:
                    logger.error("Invalid data type")
                    return
            elif self.content["meta"]["columns"][str(columnId)]["type"] == "STRING":
                try:
                    data[i] = str(data[i])
                except ValueError:
                    logger.error("Invalid data type")
                    return
            elif self.content["meta"]["columns"][str(columnId)]["type"] == "FLOAT":
                try:
                    data[i] = float(data[i])
                except ValueError:
                    logger.error("Invalid data type")
                    return
            elif self.content["meta"]["columns"][str(columnId)]["type"] == "BOOLEAN":
                try:
                    data[i] = bool(data[i])
                except ValueError:
                    logger.error("Invalid data type")
                    return
        self.content["data"][str(columnId)] = data
        if self.autosave:
            self.saveDatabase()

    def delete(self, columnId, itemId):
        logger.log("Deleting item " + str(itemId) + " from column " + str(columnId))
        del self.content["data"][str(columnId)][itemId]
        logger.log("Item deleted successfully")
        if self.autosave:
            self.saveDatabase()

    def clear(self, columnId):
        logger.log("Clearing column " + str(columnId))
        self.content["data"][str(columnId)] = []
        logger.log("Column cleared successfully")
        if self.autosave:
            self.saveDatabase()

    def get(self, columnId):
        logger.log("Getting column " + str(columnId))
        if self.autoload:
            self.loadDatabase()
        return self.content["data"][str(columnId)]

    def getItem(self, columnId, itemId):
        logger.log("Getting item " + str(itemId) + " from column " + str(columnId))
        if self.autoload:
            self.loadDatabase()
        return self.content["data"][str(columnId)][itemId]

    def getMeta(self):
        logger.log("Getting meta data")
        if self.autoload:
            self.loadDatabase()
        return self.content["meta"]

    def getData(self):
        logger.log("Getting data")
        if self.autoload:
            self.loadDatabase()
        return self.content["data"]