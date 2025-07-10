class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    
    
    for(string word : strs){
        string sorted_word = word;
        sort(sorted_word.begin(), sorted_word.end());
        groups[sorted_word].push_back(word);
    }
    
    vector<vector<string>> result;
    for(auto group : groups){
        result.push_back(group.second);
    }
    
    return result;

    }
};