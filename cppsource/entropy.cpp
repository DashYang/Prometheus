#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
#define LIMIT 40

struct node{
	string key;
	double value;
	node(string key,double value)
	{
		this->key = key;
		this->value = value;
	}
};

map<string,int> mp;
vector<node> list;
vector<string> doc;
double getH(double x)
{
	return -(1.0* x * log2(x));
}

bool cmp(node a , node b)
{
	return a.value > b.value;
}

vector<string> split(string row,string seperator)
{
	vector<string> resultset;
	int last_seperator_pos = 0;
	int next_seperator_pos = row.find_first_of(seperator , last_seperator_pos);
	int cnt = 0;
	while(next_seperator_pos != std::string::npos)
	{
		//cout << last_seperator_pos << " " << next_seperator_pos << endl;
		int distance = next_seperator_pos - last_seperator_pos;
		string tmp = row.substr(last_seperator_pos, distance);
		if(tmp != "")
			resultset.push_back(tmp);
		last_seperator_pos = next_seperator_pos + 1;
		next_seperator_pos = row.find_first_of(seperator , last_seperator_pos);
	}
	if(last_seperator_pos <= row.size())
	{
		string tmp = row.substr(last_seperator_pos, row.size() - last_seperator_pos);
		if(tmp != "")
			resultset.push_back(tmp);
	}
	return resultset;
}

int main()
{
	string word,row;
	int total = 0,i,j;
	mp.clear();
	while(!cin.eof())
	{
//		cout << row << endl;
		getline(cin,row);
		vector<string> resultset = split(row," ");
		for( i = 0 ; i < resultset.size() ; i ++)
		{
			doc.push_back(resultset[i]);
			mp[resultset[i]] ++;
			total ++;
		}
		doc.push_back("\n");

	}
	map <string, int>::iterator m1_Iter;
	for ( m1_Iter = mp.begin( ); m1_Iter != mp.end( ); m1_Iter++ )
	{
		double p = 1.0 * m1_Iter->second/total;
//		cout << m1_Iter->first << " " << getH(p) <<endl;
		node tmp = node( m1_Iter->first , getH(p));
		list.push_back(tmp);
	}
	sort(list.begin(),list.end(),cmp);

	for(i = 0; i < doc.size(); i ++ )
	{
		for(j =0 ; j < list.size(); j ++)
		{
			if(doc[i] == list[j].key || doc[i] == "\n" ||
					doc[i] == "\t")
			{
				cout << " " << doc[i] ;
				break;
			}
		}
	}
	return 0;
}
