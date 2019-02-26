#include "UserData.h"

#include <vector>

set<UserData> all_users;
int graph[1419][1419];
extern set<MovieData> all_movie;
wstring names[1419];
double scores[1419];

UserData::UserData(UserName _name, MovieData *movie_data): name(_name)
{
	movies.clear();
	if (movie_data != nullptr)
		movies.insert(movie_data);
}

UserData::~UserData()
{
}

string gettext(int i)
{
	std::string p = "";
	do
	{
		p = (char)('0' + i % 10) + p;
		i = i / 10;
	} while (i);
	return p;
}

void init_user_data(string file_name)
{
	std::locale::global(std::locale(""));
	std::wcout.imbue(std::locale(""));
	for (auto movie : all_movie)
	{
		names[movie.num] = movie.name;
		scores[movie.num] = movie.score;
	}
	cout << "开始读取用户信息文件" << endl;
	all_users.clear();
	fstream file_in(file_name);
	string line_string;
	wstring line;
	wstring line_piece;
	UserName user_name = L"";
	MovieName movie_name = L"";
	//int num = 0;
	MovieData *temp_movie;
	UserData *temp_user;
	int movie_1, movie_2;
	bool new_movie_flag;
	while (getline(file_in, line_string))
	{
		line = transport_string_to_wstring_UTF_8(line_string);
		wstringstream line_in(line);
		getline(line_in, movie_name, L',');
		getline(line_in, user_name);
		set<UserData>::iterator search_result = all_users.find(user_name);
		set<MovieData>::iterator search_movie_result = all_movie.find(movie_name);
		if (search_result == all_users.end() && search_movie_result != all_movie.end())
		{
			//set中无用户并且电影存在
			temp_movie = const_cast<MovieData*>(&*search_movie_result);
			all_users.insert(UserData(user_name, temp_movie));
			//num++;
		}
		else if(search_movie_result != all_movie.end())
		{
			//set中已有此用户并且电影存在
			temp_user = const_cast<UserData*>(&*search_result);
			temp_movie = const_cast<MovieData*>(&*search_movie_result);
			movie_2 = temp_movie->num;
			new_movie_flag = true;
			for (auto i = temp_user->movies.begin(); i != temp_user->movies.end(); i++)
			{
				movie_1 = ((MovieData*)*i)->num;
				if (movie_1 == movie_2)
				{
					new_movie_flag = false;
				}
			}
			if (new_movie_flag == true)	//这个电影是该用户没看过的新电影
			{
				for (auto i = temp_user->movies.begin(); i != temp_user->movies.end(); i++)
				{
					movie_1 = ((MovieData*)*i)->num;
					graph[movie_1][movie_2]++;
					graph[movie_2][movie_1]++;
				}
				temp_user->addMovie(temp_movie);
			}
		}
	}
	cout << "用户信息文件读取完成" << endl;
	wofstream out("out.tsv");
	out << L"ori\t";
	vector<int> source, tar, val;
	for (int i = 0; i < 1419; i++)
	{
		out << names[i] << L"\t";
		if (out.bad())
		{
			out.clear();
			out << i << L"\t";
		}
	}
	out << L"\nscore\t";
	for (int i = 0; i < 1419; i++)
	{
		out << scores[i] << L"\t";
		for (int j = 0; j < 1419; j++)
		{
			if (graph[i][j])
			{
				source.push_back(i);
				tar.push_back(j);
				val.push_back(graph[i][j]);
			}
		}
	}
	out.close();
	ofstream k("value.tsv");
	k << "source\ttarget\tvalue\n";
	for (int i = 0; i < source.size(); i++)
	{
		k << gettext(source[i]) << "\t" << gettext(tar[i]) << "\t" << gettext(val[i]) << "\n";
	}

}//共118072个用户
