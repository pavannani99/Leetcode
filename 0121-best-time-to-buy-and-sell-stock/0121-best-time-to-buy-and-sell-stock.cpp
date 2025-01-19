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
// [7,1,5,3,6,4]
// 4
// ans=0
// 4-4>ans//wrong
// 6-4>ans //-2
// 3-4=1
// 5-4=1//2<1//1
// 7-4=3//3

