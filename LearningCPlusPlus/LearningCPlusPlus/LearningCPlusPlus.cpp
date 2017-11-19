// LearningCPlusPlus.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<vector>
using namespace std;

template<typename T>
void printArray(T array, int start, int stop)
{
	if (start < stop)
	{
		for (int i = start; i<stop;i++)
		{
			cout << array[i];
		}
	}
	else
	{
		for (int i = start - 1; i >= stop; --i)
		{
			cout << array[i];
		}
	}
	cout << endl;
}

template<typename T>
void inputArray(T &array, int n)
{
	for (int i = 0; i < n; i++)
	{
		cin >> array[i];
	}
	
}

int main()
{
	int n;
	int line[100];

	cin >> n;
	inputArray(line, n);
	//printArray(line, n , 0);
	int killedTill = -1;
	int inspect = n - 1, alive = 1;
	int i = n - 1;
	while(i >= 0)
	{
		if (line[i] != 0) 
		{
			i -= line[i];
			if (i < killedTill && i>0)
				alive++;
		}
		else
		{
			--i;
			++alive;
		}
		
	}

	cout << "Result is: "<<alive<<endl;

	system("pause");

	return 0;
}

