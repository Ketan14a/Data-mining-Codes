#include <iostream>
#include  <cstdlib>
#include <time.h>

using namespace std;

class Mynumber
{
	int IP[100];
	float Temp[100];
	float OP[100];
	int max,min;

public:

	void getRandomNums()
	{
		int num,i;
		srand(time(NULL));

		for(i=0;i<100;i++)
		{

			num = rand();
			IP[i] = num;
		}
	}

	void doMinMax()
	{
		int i;
		min = IP[0];
		max = IP[0];

		for(i=1;i<100;i++)
		{
			if(IP[i]>max)
			{
				max = IP[i];
			}

			if(IP[i]<min)
			{
				min = IP[i];
			}
		}

		/* Mapping all numbers between 0 to 1 */

		for(i=0;i<100;i++)
		{
			Temp[i] = IP[i];
			OP[i] = (Temp[i] - min)/(max-min);
		}
	}

	void getOutput()
	{
		int i;

		for(i=0;i<100;i++)
		{
			cout<<IP[i]<<" maps to "<<OP[i]<<endl;
		}
	}
};



int main()
{
	Mynumber N;

	N.getRandomNums();
	N.doMinMax();
	N.getOutput();

	return 0;
}