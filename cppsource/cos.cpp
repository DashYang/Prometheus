#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;
#define TOPIC_NUM 400
#define DOC_NUM 200
double topics[DOC_NUM][TOPIC_NUM + 1];

double get_length(int x , int y ,int topic_num)
{
    int i;
    double fenzi = 0.0;
    for(i = 0 ; i < topic_num ; i ++)
        fenzi += topics[x][i] * topics[y][i];
	double fenmu1 = 0.0,fenmu2 = 0.0;
	for(i = 0 ; i < topic_num ; i ++)
	{
		fenmu1 += topics[x][i] * topics[x][i];
		fenmu2 += topics[y][i] * topics[y][i];
	}
    return fenzi/sqrt(fenmu1*fenmu2);
}

int ctoi(char* str)
{
	int len = strlen(str);
	int ans = 0;
	for(int i = 0; i < len ; i++)
		ans = ans * 10 + str[i]-'0';
	return ans;
}

int main(int argc,char *argv[])
{
	int i ,j;
	int summary_num , weibo_num , topic_num;
	int doc_num;

	summary_num = ctoi(argv[1]);
	weibo_num = ctoi(argv[2]);
	topic_num = ctoi(argv[3]);

	doc_num = summary_num + weibo_num;

	cout << "summary_num:" << summary_num <<" weibo_num:"<< weibo_num <<endl;
	cout << "topic_num " << topic_num << endl;

    for(i = 0 ; i < doc_num; i ++)
	{
		for(j = 0 ; j < topic_num ; j ++)
		{
			scanf("%lf",&topics[i][j]);
			cout << topics[i][j] << " ";
		}
		cout << endl;
	}
	
	for(i = summary_num ; i < doc_num ;i ++)
	{
		int ax = i ,ay = doc_num/2;
		double max_value = 0.0;
		for(j = 0 ; j < summary_num ; j ++)
		{
			
			double tmpvalue = 0.5 * get_length(i , j,topic_num) + 0.5 *get_length(j , i,topic_num);
			if(tmpvalue > max_value)
			{
				ay = j;
				max_value = tmpvalue;
			}
		}
		printf("%d %d %lf\n",ax+1 , ay+1 , max_value);
	}
    return 0;
}

