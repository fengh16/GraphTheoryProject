#ifndef MOVIEDATA_H
#define MOVIEDATA_H

#include <iostream>
#include <string>
#include <set>
#include <fstream>
#include <istream>
#include <ostream>
#include <sstream>
#include <algorithm>
#include <stdlib.h>
#include <Windows.h>

using namespace std;

typedef wstring MovieName;
typedef wstring MovieType;
typedef double MovieScore;

class UserData;

class MovieData
{
public:
	MovieData(MovieName name, MovieType type = L"", MovieScore score = 0, int _num = -1);
	~MovieData();
	
	bool operator < (const MovieData& r) const
	{
		return name < r.name;
	}

	bool operator > (const MovieData& r) const
	{
		return name > r.name;
	}
	
	bool operator == (MovieData& r)
	{
		return name == r.name;
	}

	bool operator != (MovieData& r)
	{
		return name != r.name;
	}

	bool operator == (wstring r)
	{
		return name == r;
	}

	bool operator != (wstring r)
	{
		return name != r;
	}

	void addType(MovieType t)
	{
		if(t.length()!=0)
			types.insert(t);
	}

	friend void init_user_data(string file_name);

private:
	MovieName name;
	set<MovieType> types;
	MovieScore score;
	int num;

	//set<UserData*> users;
};

void init_movie_data(string file_name);

wstring transport_string_to_wstring_UTF_8(string &m);

#endif // !MOVIEDATA_H
