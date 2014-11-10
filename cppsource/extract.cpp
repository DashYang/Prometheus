#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

vector<string> use_dic;

/*
void init_dic() 
{
	use_dic.clear();
	use_dic.push_back("p");
	use_dic.push_back("c");
	use_dic.push_back("b");
	use_dic.push_back("uj");
	use_dic.push_back("m");
	use_dic.push_back("un");
	use_dic.push_back("r");
}
*/

void init_dic() 
{
	use_dic.clear();
	use_dic.push_back("n");
	use_dic.push_back("v");
}

bool iStop(string word)
{
	int index = word.find('/');
	if(index == -1)
		return false;
	int i;
	string speech = word.substr(index+1,word.size());
	for(i = 0 ;i < use_dic.size() ;i ++)
	{
		if(use_dic[i] == speech)
		{
			return false;
		}
	}
	return true;
}

bool isNotStop(string word)
{
	int index = word.find('/');
	if(index == -1)
		return false;
	int i;
	string speech = word.substr(index+1,word.size());
	for(i = 0 ;i < use_dic.size() ;i ++)
	{
		if(use_dic[i] == speech)
		{
			return true;
		}
	}
	return false;
}

int main()
{
	string word;
	init_dic();
	while(cin >> word)
	{
		if(isNotStop(word))
			cout << word << " ";
	}
	cout << endl;
	return 0;
}
