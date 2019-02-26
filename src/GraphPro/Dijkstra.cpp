#include <string>
#include <fstream>

std::string int2string(int i)
{
	std::string ans;
	while (true)
	{
		ans = (char)(i % 10 + '0') + ans;
		i = i / 10;
		if (!i)
		{
			break;
		}
	}
	return ans;
}

void Dij(std::istream &inputStream, std::ostream &outputStream)
{
	int vNo, eNo, *vData, *eData, *xData;
	inputStream >> vNo >> eNo;
	vData = new int[vNo + 1];
	eData = new int[eNo];
	xData = new int[eNo];
	for (int i = 0; i <= vNo; i++)
	{
		inputStream >> vData[i];
	}
	for (int i = 0; i < eNo; i++)
	{
		inputStream >> eData[i];
	}
	for (int i = 0; i < eNo; i++)
	{
		inputStream >> xData[i];
	}
	int testNo, *testDataF, *testDataD;
	inputStream >> testNo;
	testDataF = new int[testNo];
	testDataD = new int[testNo];
	for (int i = 0; i < testNo; i++)
	{
		inputStream >> testDataF[i] >> testDataD[i];
	}

	// Deal with data inputed and make a matrix;
	int **intMatrix = new int*[vNo];
	for (int i = 0; i < vNo; i++)
	{
		intMatrix[i] = new int[vNo];
		for (int j = 0; j < vNo; j++)
		{
			intMatrix[i][j] = -1;
		}
		for (int j = vData[i]; j < vData[i + 1]; j++)
		{
			intMatrix[i][eData[j]] = xData[j];
		}
	}

	for (int j = 0; j < testNo; j++)
	{
		// Calculate the path accordingly;
		bool *added = new bool[vNo];
		int *lastNode = new int[vNo];
		int *nowLen = new int[vNo];
		// Deal with the starting node first;
		int nowNode = testDataF[j];
		int tar = testDataD[j];
		for (int i = 0; i < vNo; i++)
		{
			added[i] = false;
			lastNode[i] = nowNode;
			nowLen[i] = intMatrix[nowNode][i];
		}
		while (true)
		{
			std::string ans;
			// Choose the shortest Node from the start;
			int nowMin = INT_MAX;
			int shortestNode = -1;
			for (int i = 0; i < vNo; i++)
			{
				if (nowLen[i] >= 0 && nowLen[i] < nowMin && !added[i])
				{
					nowNode = i;
					nowMin = nowLen[i];
				}
			}
			// If the chosen node is the target node, just return the ans;
			if (nowNode == tar)
			{
				// Output the ans and an endl;
				// Use string to record;
				ans = int2string(tar);
				do
				{
					nowNode = lastNode[nowNode];
					ans = int2string(nowNode) + " -> " + ans;
				} while (nowNode != testDataF[j]);
				outputStream << "[" << ans << " " << nowLen[tar] << "]" << std::endl;
				break;
			}
			if (nowMin == INT_MAX)
			{
				outputStream << "NO PATH" << std::endl;
				break;
			}
			// Record that the node have been visited;
			added[nowNode] = true;
			for (int i = 0; i < vNo; i++)
			{
				if (!added[i] && intMatrix[nowNode][i] >= 0)
				{
					if (nowLen[i] < 0 || (nowLen[i] > nowLen[nowNode] + intMatrix[nowNode][i]))
					{
						lastNode[i] = nowNode;
						nowLen[i] = nowLen[nowNode] + intMatrix[nowNode][i];
					}
				}
			}
		}
		delete added;
		delete lastNode;
	}
}