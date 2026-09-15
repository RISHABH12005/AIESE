#include <iostream>
#include <string>
using namespace std;

bool login(const string& username, const string& password) {
    const string query =
        "SELECT * FROM students WHERE username = ? AND password = ?";

    // Bind username and password as parameters through the database driver's
    // prepared-statement API instead of concatenating them into the SQL.
    cout << "Executing: " << query << endl;
    return !username.empty() && !password.empty();
}
