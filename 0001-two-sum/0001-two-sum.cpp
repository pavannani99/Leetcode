class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    //   int   n=nums.size();
    //     for(int i=0;i<n;i++){
    //      for(int j=i+1;j<n;j++){
    //         if(nums[i]+nums[j]==target){
    //             return {i,j};
    //         }
    //      }
    //     }
    //      return {};
    unordered_map<int,int>mp;
    for(int i=0;i<nums.size();i++){
int x=nums[i];
int y=target-nums[i];
if(mp.count(y)){
    return {i,mp[y]};
}


mp[nums[i]]=i;





    }
return {};
        }
    
};