class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_set<int>haha;
        int i=0;
        for(int num:nums){
        if(haha.count(num)==0){
        haha.insert(num);
        
        nums[i++]=num;
        }
        }
        return i;
        
    }
};