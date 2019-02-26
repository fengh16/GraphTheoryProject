#include <iostream>
#include "IO.h"
#include "Algorithm.h"

int main()
{
	init_movie_data("movie.csv");
	init_user_data("user.csv");
	//connected_branch();
	prim();
	return 0;
}