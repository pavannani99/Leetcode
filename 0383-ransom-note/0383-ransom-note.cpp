class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        
        vector<char>needed;
        for(int i=0;i<ransomNote.length();i++){
            needed.push_back(ransomNote[i]);
        }
          for (int j = 0; j < magazine.length(); j++) {
            for (int k = 0; k < needed.size(); k++) {
                if (needed[k] == magazine[j]) {
                    needed.erase(needed.begin() + k);
                    break; 
                }
            }
        }

        
        return needed.empty();
    }
};