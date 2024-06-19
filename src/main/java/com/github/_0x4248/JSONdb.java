/* JSONdb
 * Create databases using JSON files
 * Github: https://www.github.com/0x4248/JSONdb
 * Licence: GNU General Public License v3.0
 * By: 0x4248
*/

package com.github._0x4248;

import java.io.*;
import java.util.*;
import com.google.gson.*;

public class JSONdb {
    public static boolean traceLog = false;
    private String contentName;
    private JsonObject content;
    private boolean autosave;
    private Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public JSONdb(String databaseName, boolean autosave, boolean traceLog) {
        this.contentName = databaseName;
        this.autosave = autosave;
        JSONdb.traceLog = traceLog;
        loadDatabase();
    }

    private void loadDatabase() {
        try {
            Logger.log("Loading database: " + contentName);
            BufferedReader reader = new BufferedReader(new FileReader(contentName));
            this.content = gson.fromJson(reader, JsonObject.class);
            reader.close();
            Logger.log("Database loaded successfully with " + content.getAsJsonObject("meta").getAsJsonObject("columns").entrySet().size() + " columns");
        } catch (FileNotFoundException e) {
            Logger.warn("Database was not found and will need to be initialized before use");
        } catch (IOException e) {
            Logger.error("Error reading the database file: " + e.getMessage());
        }
    }

    private void saveDatabase() {
        try {
            Logger.log("Saving database: " + contentName);
            BufferedWriter writer = new BufferedWriter(new FileWriter(contentName));
            Logger.log("Dumping content to file");
            writer.write(gson.toJson(content));
            writer.close();
            Logger.log("Database saved successfully");
        } catch (IOException e) {
            Logger.error("Error writing the database file: " + e.getMessage());
        }
    }

    public void init(String name, String description) {
        Logger.log("Preparing initialization of database");
        this.content = new JsonObject();
        JsonObject meta = new JsonObject();
        meta.addProperty("name", name);
        meta.addProperty("description", description);
        meta.add("columns", new JsonObject());
        this.content.add("meta", meta);
        this.content.add("data", new JsonObject());
        if (autosave) {
            saveDatabase();
        }
    }

    public int createColumn(String name, String type, String description) {
        JsonObject columns = content.getAsJsonObject("meta").getAsJsonObject("columns");
        int columnId = columns.entrySet().size();
        JsonObject column = new JsonObject();
        column.addProperty("name", name);
        column.addProperty("type", type);
        column.addProperty("description", description);
        columns.add(String.valueOf(columnId), column);
        content.getAsJsonObject("data").add(String.valueOf(columnId), new JsonArray());
        if (autosave) {
            saveDatabase();
        }
        return columnId;
    }

    public void insert(int columnId, Object data) {
        Logger.log("Inserting data into column " + columnId);
        String columnIdStr = String.valueOf(columnId);
        JsonObject column = content.getAsJsonObject("meta").getAsJsonObject("columns").getAsJsonObject(columnIdStr);
        String type = column.get("type").getAsString();
        JsonArray columnData = content.getAsJsonObject("data").getAsJsonArray(columnIdStr);
        try {
            switch (type) {
                case "INTEGER":
                    columnData.add(Integer.parseInt(data.toString()));
                    break;
                case "STRING":
                    columnData.add(data.toString());
                    break;
                case "FLOAT":
                    columnData.add(Float.parseFloat(data.toString()));
                    break;
                case "BOOLEAN":
                    columnData.add(Boolean.parseBoolean(data.toString()));
                    break;
                default:
                    Logger.error("Unknown column type");
            }
            Logger.log("Data inserted successfully");
            if (autosave) {
                saveDatabase();
            }
        } catch (NumberFormatException e) {
            Logger.error("Invalid data type");
        }
    }

    public void insertItems(int columnId, List<?> data) {
        Logger.log("Inserting data into column " + columnId);
        String columnIdStr = String.valueOf(columnId);
        JsonObject column = content.getAsJsonObject("meta").getAsJsonObject("columns").getAsJsonObject(columnIdStr);
        String type = column.get("type").getAsString();
        JsonArray columnData = content.getAsJsonObject("data").getAsJsonArray(columnIdStr);
        try {
            for (Object item : data) {
                switch (type) {
                    case "INTEGER":
                        columnData.add(Integer.parseInt(item.toString()));
                        break;
                    case "STRING":
                        columnData.add(item.toString());
                        break;
                    case "FLOAT":
                        columnData.add(Float.parseFloat(item.toString()));
                        break;
                    case "BOOLEAN":
                        columnData.add(Boolean.parseBoolean(item.toString()));
                        break;
                    default:
                        Logger.error("Unknown column type");
                        return;
                }
            }
            if (autosave) {
                saveDatabase();
            }
        } catch (NumberFormatException e) {
            Logger.error("Invalid data type");
        }
    }

    public void delete(int columnId, int itemId) {
        Logger.log("Deleting item " + itemId + " from column " + columnId);
        JsonArray columnData = content.getAsJsonObject("data").getAsJsonArray(String.valueOf(columnId));
        columnData.remove(itemId);
        Logger.log("Item deleted successfully");
        if (autosave) {
            saveDatabase();
        }
    }

    public void clear(int columnId) {
        Logger.log("Clearing column " + columnId);
        content.getAsJsonObject("data").add(String.valueOf(columnId), new JsonArray());
        Logger.log("Column cleared successfully");
        if (autosave) {
            saveDatabase();
        }
    }

    public JsonArray get(int columnId) {
        Logger.log("Getting column " + columnId);
        return content.getAsJsonObject("data").getAsJsonArray(String.valueOf(columnId));
    }

    public JsonElement getItem(int columnId, int itemId) {
        Logger.log("Getting item " + itemId + " from column " + columnId);
        return content.getAsJsonObject("data").getAsJsonArray(String.valueOf(columnId)).get(itemId);
    }

    public JsonObject getMeta() {
        Logger.log("Getting meta data");
        return content.getAsJsonObject("meta");
    }

    public JsonObject getData() {
        Logger.log("Getting data");
        return content.getAsJsonObject("data");
    }
}