/* JSONdb
 * Create databases using JSON files
 * Github: https://www.github.com/0x4248/JSONdb
 * Licence: GNU General Public License v3.0
 * By: 0x4248
*/

package com.github._0x4248;

import java.util.Arrays;

public class Demo {
    public static void main(String[] args) {
        JSONdb db = new JSONdb("products.json", true, true);
        db.init("Products", "A demo database for products");
        db.createColumn("product", "STRING", "The name of the product");
        db.createColumn("price", "FLOAT", "The price of the product");
        db.createColumn("stock", "INTEGER", "The stock of the product");
        db.insert(0, "Apple");
        db.insert(1, 1.99);
        db.insert(2, 100);
        db.insert(0, "Banana");
        db.insert(1, 0.99);
        db.insert(2, 200);
        db.insert(0, "Orange");
        db.insert(1, 2.99);
        db.insert(2, 50);
        db.insertItems(0, Arrays.asList("Pineapple", "Grapes", "Watermelon"));
        db.insertItems(1, Arrays.asList(3.99, 4.99, 5.99));
        db.insertItems(2, Arrays.asList(25, 10, 5));
        System.out.println(db.get(0));
        System.out.println(db.get(1));
        System.out.println(db.get(2));
        System.out.println(db.getItem(0, 0));
        System.out.println(db.getItem(1, 0));
        System.out.println(db.getItem(2, 0));
        System.out.println(db.getMeta());
        System.out.println(db.getData());
    }
}
