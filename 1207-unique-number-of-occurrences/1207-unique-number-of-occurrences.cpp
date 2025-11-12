class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int>mp;
        for (int x : arr) mp[x]++;
         unordered_set<int> s;
        for (auto p : mp) {
            if (s.count(p.second)) return false; 
            s.insert(p.second);
        }
        return true;
    }
};