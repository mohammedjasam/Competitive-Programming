// QuadSelection.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <iostream>
//#include <vector>
#include <map>

using namespace std;

int main()
{
	int N, M;

	scanf("%d%d", &N, &M);

	map<int, int> count;
	int max = 0;

	for (int i = 1; i < N + 1; i++)
	{
		for (int j = 1; j < M + 1; j++)
		{
			if (count.find(i+j) == count.end())
			{
				count[i + j] = 1;
			}
			else
			{
				count[i + j]++;
			}

			if (count[i + j] > max)
			{
				max = count[i + j];
			}
		}
	}

	for (const auto &p : count)
	{
		if (p.second == max)
		{
			cout << p.first<<endl;
		}
	}

	//system("pause");
    return 0;
}
