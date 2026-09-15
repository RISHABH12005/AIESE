#include <iostream>
#include <vector>
#include "Room.h"
#include "Fee.h"
using namespace std;

int main() {
    vector<Room> rooms = {
        {101, false, -1},
        {102, true, 25},
        {103, false, -1}
    };

    Student student{101, "Aman", -1, 3000.0};

    cout << "Room 101 available: "
         << isRoomAvailable(rooms, 101) << endl;
    cout << "Room 102 available: "
         << isRoomAvailable(rooms, 102) << endl;
    cout << "Room allocation result: "
         << allocateRoom(rooms, student, 101) << endl;
    cout << "Hostel fee: "
         << calculateHostelFee(3000.0, 3) << endl;

    return 0;
}
