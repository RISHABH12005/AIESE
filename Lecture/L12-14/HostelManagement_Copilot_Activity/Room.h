#ifndef ROOM_H
#define ROOM_H
#include <vector>
#include "Student.h"
using namespace std;

struct Room {
    int roomNo;
    bool occupied;
    int studentId;
};

bool isRoomAvailable(const vector<Room>& rooms, int roomNo);
bool allocateRoom(vector<Room>& rooms, Student& student, int roomNo);
#endif
