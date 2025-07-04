class Solution {
public:
    int climbStairs(int n) {
   int i=0;
   if(n<=2){
    return n;
   }
int first=1;
int second=2;
for(i=3;i<n+1;i++){
    int curretn=first+second;
    first=second;
    second=curretn;
}
return second;

///
// first entatde 3=1+2 
    }
};