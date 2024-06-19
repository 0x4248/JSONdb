/* JSONdb
 * Create databases using JSON files
 * Github: https://www.github.com/0x4248/JSONdb
 * Licence: GNU General Public License v3.0
 * By: 0x4248
*/

package com.github._0x4248;

public class Logger {
    private static final String RED = "\033[91m";
    private static final String GREEN = "\033[92m";
    private static final String YELLOW = "\033[93m";
    private static final String CYAN = "\033[96m";
    private static final String GREY = "\033[97m";
    private static final String RESET = "\033[0m";

    static void log(String message) {
        if (JSONdb.traceLog) {
            System.out.println("[" + GREEN + "JSONdb" + RESET + "] " + CYAN + "LOG:" + RESET + " " + GREY + message + RESET);
        }
    }

    static void warn(String message) {
        if (JSONdb.traceLog) {
            System.out.println("[" + GREEN + "JSONdb" + RESET + "] " + YELLOW + "WARN:" + RESET + " " + GREY + message + RESET);
        }
    }

    static void error(String message) {
        if (JSONdb.traceLog) {
            System.out.println("[" + GREEN + "JSONdb" + RESET + "] " + RED + "ERROR:" + RESET + " " + GREY + message + RESET);
        }
    }
}