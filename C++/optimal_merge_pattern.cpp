// Optimal Merge Pattern : Given n number of sorted files, the task is to find the minimum computations done to reach the Optimal Merge Pattern.

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> a;
    for (int i = 0; i < n; i++)
    {
        int ele;
        cin >> ele;
        a.push_back(ele);
    }
    priority_queue<int, vector<int>, greater<int> > minheap;
    for (int i = 0; i < n; i++)
    {
        minheap.push(a[i]);
    }
    int ans = 0;
    while (minheap.size() > 1)
    {
        int e1 = minheap.top();
        minheap.pop();
        int e2 = minheap.top();
        minheap.pop();
        ans += e1 + e2;
        minheap.push(e1 + e2);
    }
    cout << ans << endl;
    return 0;
}