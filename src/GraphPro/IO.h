#ifndef IO_H
#define IO_H

#include <fstream>
#include "UserData.h"
#include "MovieData.h"
#include <set>

using namespace std;

enum Status { READERROR, READOK };

extern Status readData();

#endif // !IO_H
