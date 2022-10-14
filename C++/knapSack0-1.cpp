// 0-1 Knapsack Problem in DP
// You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
// Note that we have only one quantity of each item.
// In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items
// respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that
// sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or
// dont pick it (0-1 property).
// Input:
// N = 3
// W = 4
// values[] = {1,2,3}
// weight[] = {4,5,1}
// Output: 3
// #Coding Ninjas Medium Problem
#include <bits/stdc++.h>
using namespace std;

// Bottom Up More Space Optimized Tabulation DP Approach
// Time Complexity : O(N*W)
// Space Complexity : O(W)
// Auxiliary Space Complexity : O(1) [due to no recursive stack space]
int maxProfitBUSOM(vector<int> &val, vector<int> &wt, int maxWt, int n)
{
    vector<int> prev(maxWt + 1, 0);
    for (int W = wt[0]; W <= maxWt; W++)
        prev[W] = val[0];
    for (int ind = 1; ind < n; ind++)
    {
        for (int W = maxWt; W >= 0; W--)
        {
            int notTake = 0 + prev[W];
            int take = (-1e9);
            if (wt[ind] <= W)
                take = val[ind] + prev[W - wt[ind]];
            prev[W] = max(take, notTake);
        }
    }
    return prev[maxWt];
}

// Bottom Up Space Optimized Tabulation DP Approach
// Time Complexity : O(N*W)
// Space Complexity : O(W) + O(W) = O(2W)
// Auxiliary Space Complexity : O(1) [due to no recursive stack space]
int maxProfitBUSO(vector<int> &val, vector<int> &wt, int maxWt, int n)
{
    vector<int> prev(maxWt + 1, 0), curr(maxWt + 1, 0);
    for (int W = wt[0]; W <= maxWt; W++)
        prev[W] = val[0];
    for (int ind = 1; ind < n; ind++)
    {
        for (int W = 0; W <= maxWt; W++)
        {
            int notTake = 0 + prev[W];
            int take = (-1e9);
            if (wt[ind] <= W)
                take = val[ind] + prev[W - wt[ind]];
            curr[W] = max(take, notTake);
        }
        prev = curr;
    }
    return prev[maxWt];
}

// Bottom Up Tabulation DP Approach
// Time Complexity : O(N*W)
// Space Complexity : O(N*W)
// Auxiliary Space Complexity : O(1) [due to no recursive stack space]
int maxProfitBU(vector<int> &val, vector<int> &wt, int maxWt, int n)
{
    vector<vector<int>> dp(n, vector<int>(maxWt + 1, 0));
    for (int W = wt[0]; W <= maxWt; W++)
        dp[0][W] = val[0];
    for (int ind = 1; ind < n; ind++)
    {
        for (int W = 0; W <= maxWt; W++)
        {
            int notTake = 0 + dp[ind - 1][W];
            int take = (-1e9);
            if (wt[ind] <= W)
                take = val[ind] + dp[ind - 1][W - wt[ind]];
            dp[ind][W] = max(take, notTake);
        }
    }
    return dp[n - 1][maxWt];
}

// Top Down Memoization DP Approach
// Time Complexity : O(N*W)
// Space Complexity : O(N*W)
// Auxiliary Space Complexity : O(N) [due to recursive stack space]
int mPTf(int ind, int W, vector<int> &val, vector<int> &wt, vector<vector<int>> &dp)
{
    if (ind == 0)
    {
        if (wt[ind] <= W)
            return val[ind];
        return 0;
    }
    if (dp[ind][W] != -1)
        return dp[ind][W];
    // Not take
    int notTake = 0 + mPTf(ind - 1, W, val, wt, dp);
    // Take
    int take = (-1e9);
    if (wt[ind] <= W)
        take = val[ind] + mPTf(ind - 1, W - wt[ind], val, wt, dp);
    return dp[ind][W] = max(take, notTake);
}
int maxProfitTD(vector<int> &values, vector<int> &weights, int W, int n)
{
    vector<vector<int>> dp(n, vector<int>(W + 1, -1));
    return mPTf(n - 1, W, values, weights, dp);
}

// Recursive Approach
// Time Complexity : O(2^N)
// Space Complexity : O(1)
// Auxiliary Space Complexity : O(N) [due to recursive stack space]
int mPRf(int ind, int W, vector<int> &val, vector<int> &wt)
{
    if (ind == 0)
    {
        if (wt[ind] <= W)
            return val[ind];
        return 0;
    }
    // Not take
    int notTake = 0 + mPRf(ind - 1, W, val, wt);
    // Take
    int take = (-1e9);
    if (wt[ind] <= W)
        take = val[ind] + mPRf(ind - 1, W - wt[ind], val, wt);
    return max(take, notTake);
}
int maxProfitRec(vector<int> &values, vector<int> &weights, int W, int n)
{
    return mPRf(n - 1, W, values, weights);
}

// Main method
int main()
{
    int n, W;
    cin >> n;
    vector<int> values(n), weights(n);
    for (int i = 0; i < n; i++)
        cin >> values[i] >> weights[i];
    cin >> W;
    cout << maxProfitBUSOM(values, weights, W, n) << endl;
    return 0;
}