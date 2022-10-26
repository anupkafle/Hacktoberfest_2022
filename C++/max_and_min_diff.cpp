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
    sort(a.begin(), a.end());
    long long mx = 0, mn = 0;
    for (int i = 0; i < n / 2; i++)
    {
        mx += (a[i + n / 2] - a[i]);
        mn += (a[2 * i + 1] - a[2 * i]);
    }
    cout << mx << " " << mn << endl;
    return 0;
}