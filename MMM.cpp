#include <iostream>
using namespace std;


class Mynumber
{
	float a[10];
	float mean,median;
	int i;

public:

	void getNums()
	{
		cout<<"Enter 10 numbers:-"<<endl;

		for(i=0;i<10;i++)
		{
			cin>>a[i];
		}
	}

	void getMean()
	{
		float sum = 0;

		for(i=0;i<10;i++)
		{
			sum = sum + a[i];
		}

		mean = sum/10;

		cout<<"The Mean is "<<mean<<endl;
	}

	void getMedian()
	{
		float temp;
		int j;

		for(i=0;i<10;i++)
		{
			for(j=i+1;j<10;j++)
			{
				if(a[i]>a[j])
				{
					temp = a[j];
					a[j] = a[i];
					a[i] = temp;
				}
			}
		}

		median = (a[4]+a[5])/2.0;

		cout<<"The median is "<<median<<endl;
	}

	void getMode()
	{
		float count[10];
		float check[10];
		int maxOccurance=1;
		int j,Mdegree=0;

		for(i=0;i<10;i++)
		{
			count[i] = 1;
			check[i] = -10000;
		}

		for(i=0;i<10;i++)
		{
			if(check[i]==-10000)
			{
			for(j=0;j<10;j++)
			{
				if(i!=j && a[i]==a[j])
				{
					count[i]++;
					check[i] = check[j] = a[i];
				}
			}
		   }
		   else
		   {
		   	continue;
		   }
		}

		for(i=0;i<10;i++)
		{
			if(count[i] > maxOccurance)
			{
				maxOccurance = count[i];
			}
		}
		
		for(i=0;i<10;i++)
		{
			if(count[i]==maxOccurance)
			{
				cout<<"The mode is "<<a[i]<<endl;;
				Mdegree++;
			}
		}

		
		if(Mdegree==1)
		{
			cout<<"The data feeded is Uni-model in nature.";
		}
		else if(Mdegree==2)
		{
			cout<<"The data feeded is Bi-model in nature.";
		}
		else
		{
			cout<<"The data feeded is Multi-model in nature.";
		}
	}
};

int main()
{
	Mynumber N;

	N.getNums();
	N.getMean();
	N.getMedian();
	N.getMode();

	return 0;
}