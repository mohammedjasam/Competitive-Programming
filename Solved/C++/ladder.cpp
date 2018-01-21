// QuadSelection.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cmath>
#define PI 3.14159265
using namespace std;


int main()
{
	int height, angle;

	scanf_s("%d%d", &height, &angle);
  
  // using x/ sin(x) = y/ sin(y)
	double cangle = 90 - angle;

	double x = sin(cangle * PI / 180);
	double v = sin(angle*PI / 180);

	double side = ((x * height) / v); // finding the base first

	int result = ceil(sqrt(height*height + side*side)); // finding the hypo

	printf("%d", result);
	//system("pause");
    return 0;
}
