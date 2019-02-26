#ifndef USERDATA_H
#define USERDATA_H

#include <iostream>
#include <string>
#include <set>
#include "MovieData.h"

using namespace std;

typedef wstring UserName;

class UserData
{
public:
	UserData(UserName _name = L"", MovieData *_movie_data = nullptr);
	~UserData();
	
	bool operator < (const UserData& r) const
	{
		return name < r.name;
	}

	bool operator > (const UserData& r) const
	{
		return name > r.name;
	}
	
	bool operator == (UserData& r)
	{
		return name == r.name;
	}

	bool operator == (UserName& r)
	{
		return name == r;
	}

	bool operator != (UserData& r)
	{
		return name != r.name;
	}

	bool operator != (UserName& r)
	{
		return name != r;
	}

	bool operator == (wstring r)
	{
		return name == r;
	}

	bool operator != (wstring r)
	{
		return name != r;
	}

	void addMovie(MovieData* m)
	{
		movies.insert(m);
	}

	friend void init_user_data(string file_name);

private:
	UserName name;
	set<MovieData*> movies;
};

void init_user_data(string file_name);

#endif // !USERDATA_H
