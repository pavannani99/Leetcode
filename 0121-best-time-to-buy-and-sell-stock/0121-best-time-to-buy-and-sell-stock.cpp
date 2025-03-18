class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minim=prices[0];
        int maxpro=0;
        int n=prices.size();
        for(int i=0;i<n;i++){
            int cost=prices[i]-minim;
            maxpro=max(maxpro,cost);
            minim=min(minim,prices[i]);
        }
        return maxpro;
        
    }
};