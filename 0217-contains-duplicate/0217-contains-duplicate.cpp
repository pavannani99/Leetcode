class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int>mp;
        for(int i=0;i<nums.size();i++){
           if(mp.count(nums[i])>=1){
            return true;
           }
           mp[nums[i]]=i;
        }
           return false;
    }
};