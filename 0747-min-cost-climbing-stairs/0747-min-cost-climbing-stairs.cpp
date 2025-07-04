class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // int prev=0;
        //
        int n=cost.size();
        vector<int>dp(n+1,0);
        
for(int i=2;i<=n;i++){
int fs=dp[i-1]+cost[i-1];
int fc=dp[i-2]+cost[i-2];
dp[i]=min(fs,fc);
}
return dp[n];
    }
};