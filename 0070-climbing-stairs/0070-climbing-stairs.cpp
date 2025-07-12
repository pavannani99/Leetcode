class Solution {
public:
    int climbStairs(int n) {
        if(n<2) return n;
        int fs=1;
        int sc=2;
        for(int i=3;i<n+1;i++){
              int curr=fs+sc;
              fs=sc;
              sc=curr;
        }
        return sc;
    }
};