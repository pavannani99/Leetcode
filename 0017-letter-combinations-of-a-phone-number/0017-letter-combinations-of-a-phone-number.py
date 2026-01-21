""""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2-.abc and 3->def
a b c
d e f
 
 2 3 4
  a b c =>adf
  d e f
  g h i =>adg,ade,adi
  def combinations(res,dictionary,digits,index,buffer):
    break condition
    if index==len(digits):
        break
    looping
    loop over the ditionary (getcombinaions)
    dictionary={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
"""







# dictionary={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
class Solution:
    def getCombinations(self,res,dictionary,digits,index,buffer):
        if index==len(digits):
            res.append(buffer)
            return res
        for char in dictionary[digits[index]]:
             self.getCombinations(res,dictionary,digits,index+1,buffer+char)

    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dictionary={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.getCombinations(res,dictionary,digits,0,"")
        return res

        