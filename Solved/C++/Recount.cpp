// Recount.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<iostream>
#include<string>
#include<map>

using namespace std;
//using namespace StringFloatMap;

string findWinner(map<string, int> someMap, int max)
{
	int count = 0;
	string maxName = "";


	for (const auto& kv : someMap)
	{
		if (kv.second == max)
		{
			count++;
			if (count == 1)
			{
				maxName = kv.first;
			}
		}


	}
	if (count == 1)
	{
		return maxName;
	}
	return "Runoff!";

}



int main()
{
	map<string, int> elections;
	string name;
	do
	{
		getline(cin, name);
		if (name != "***")
		{
			if (elections.count(name) == 1)
			{
				elections[name]++;
			}
			else
			{
				elections[name] = 1;
			}
		}

	} while (name != "***");

	int max = 0;
	map<string, int> winner;

	for (const auto& kv : elections) {

		int votes = 0;
		string candidate;

		votes = kv.second;
		candidate = kv.first;

		if (votes > max)
		{
			max = votes;
			/*winner[candidate] = max;*/
		}

		//std::cout << kv.first << " has value " << kv.second << std::endl;
	}

	cout << findWinner(elections, max) << endl;



	//system("pause");
    return 0;
}
