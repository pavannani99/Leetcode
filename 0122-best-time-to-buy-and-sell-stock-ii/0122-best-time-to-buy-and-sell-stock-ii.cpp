class Solution {
public:
    int maxProfit(vector<int>& prices) {
       //if before one is large then move if it small //
        int maxval=prices.back();
        int res=0;
        
        for(int i=prices.size()-2;i>=0;i--){
         // if(maxval>prices[i]){ 
         //   maxval=(maxval-prices[i]); 
             if (prices[i] < maxval) {
                 res += maxval - prices[i];;
                maxval=prices[i];
            } else {
                // Update maxval if the current price is greater
                maxval = prices[i];
            
          
            }
           
        }
        
        return res;
    }
};