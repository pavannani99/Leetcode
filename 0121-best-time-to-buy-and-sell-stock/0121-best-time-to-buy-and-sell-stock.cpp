class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxval=prices.back();
        int ans=0;
        for(int i=prices.size()-1;i>=0;i--){
            if(maxval-prices[i]>ans) ans=(maxval-prices[i]);
            maxval=max(maxval,prices[i]);
        }
        return ans;
    }
};