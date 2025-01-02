class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> countMap;
        vector<int>hey;
          for (int num : nums) {
        countMap[num]++;
        if (countMap[num] > nums.size() / 2) {
            return num;
        }
    }

    throw runtime_error("No majority element found!");
}
 
    
};