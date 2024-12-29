class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int>count(k);
        count[0]=1;
        int res=0,prefix=0;
        for(int num:nums){
     prefix=(prefix+num%k+k)%k;
       res+=count[prefix]++;
        }
        return res;
    }
};