#include <iostream>
#include <fstream>
#include <map>
#include <deque>
#include <vector>

#include <cstring>
#include <algorithm>

using namespace std;
#define coutfpre(n,f) (setiosflags(ios::fixed)<<setprecision(n)<<f)
#define zero(n) memset(n,0,sizeof(n))
#define m1set(n) memset(n,-1,sizeof(n))
#define min(m,n) ((m<n)?m:n)
#define max(m,n) ((m>n)?m:n)


//#define FILE_TEST

/*
    Problem
    You are given a tree (a simple connected graph with no cycles).
    Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of nodes.
    As an example, the following tree with  nodes can be cut at most  time to create an even forest.
*/

int countAllChildren(vector <int> *v , int *childrens , int offset)
{
    int totalSize = 0;
    if(v[offset].size() == 0)
        childrens[offset] = 1;
    else if(0 == childrens[offset])
    {
        for(int i = 0; i < v[offset].size() ; i++)
        {
            totalSize += countAllChildren(v,childrens,v[offset][i]);
        }
    }
    childrens[offset] = totalSize + 1;
    return childrens[offset];
}

bool solve(istream &in,ostream &out)
{
    int N,M;
    int returnValue = 0;
    in >> N >> M;
    int childrens[N];
    zero(childrens);
    vector <int> childrenVector[N];

    for(int i = 0; i < M ; i++)
    {
        int edge1,edge2;
        in >> edge1 >> edge2;
        edge1 --;
        edge2 --;
        childrenVector[edge2].push_back(edge1);
    }

    countAllChildren(childrenVector,childrens,0);
    for(int i = 1; i < N; i++)
    {
        if((childrens[i])%2 == 0)
        {
            returnValue++;
        }
    }

    out<<returnValue<<endl;
    return true;
}



int main()
{
    bool bSolved;
    #ifdef FILE_TEST
        ifstream in("in.txt");
        ofstream out("out.txt");
        if(!in)
        {
            cout<<"file in error\n";
            return 0;
        }
        if(!out)
        {
            cout<<"file out error\n";
            in.close();
            return 0;
        }
        bSolved = solve(in,out);
        in.close();
        out.close();
    #else
        bSolved = solve(cin,cout);
    #endif

    #ifdef FILE_TEST
        if(!bSolved)
            cout << "not solved\n" <<endl;
        else
            cout << "solved\n" <<endl;
        getchar();
    #endif

    return bSolved;
}