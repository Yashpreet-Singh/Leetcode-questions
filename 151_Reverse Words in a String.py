class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join(s.strip().split()[::-1])

        res=[]
        curr =''
        for l in s + ' ': #to get last word before end of string , for strings: " i am blue"
            if l != ' ':
                curr += l
            elif len(curr):
                res.append(curr)
                curr=''

        final_ans= ''
        for j in range(len(res)-1,-1,-1):
            final_ans+=res[j]+' '

        return final_ans.strip()
