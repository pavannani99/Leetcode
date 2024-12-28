class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_set<int>hello;
        vector<int>duplicates;
        for(int num:nums){
            if(hello.count(num)){
                duplicates.push_back(num);
            }
                hello.insert(num);
            
        }
        return duplicates;
    }
};