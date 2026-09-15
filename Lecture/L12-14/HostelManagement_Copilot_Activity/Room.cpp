#include "Room.h"

// INTENTIONAL BUG: returns true for an occupied room.
bool isRoomAvailable(const vector<Room>& rooms, int roomNo) {
    for (const auto& room : rooms) {
        if (room.roomNo == roomNo) {
            return room.occupied; // BUG: should be !room.occupied
        }
    }
    return false;
}

bool allocateRoom(vector<Room>& rooms, Student& student, int roomNo) {
    if (isRoomAvailable(rooms, roomNo)) {
        for (auto& room : rooms) {
            if (room.roomNo == roomNo) {
                room.occupied = true;
                room.studentId = student.id;
                student.roomNo = roomNo;
                return true;
            }
        }
    }
    return false;
}
