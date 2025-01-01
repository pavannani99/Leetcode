class Solution {
public:
    bool isValid(string s) {
      stack<int>spam;
      for(char c:s){
        if(c=='('){
        spam.push(')');
        }
        else if(c=='{'){
        spam.push('}');
        }
        else if(c=='['){
        spam.push(']');
        }
        else {
           if(spam.empty() || spam.top() != c) {
                    return false;
           }
        spam.pop();
      }
      }
      return spam.empty();
    }
};