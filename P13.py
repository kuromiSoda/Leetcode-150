class Solution:
    def romanToInt(self, s: str) -> int:
        temp=s
        d1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        d2={'IV':4,'IX':9,'XL':40, 'XC':90,'CD':400,'CM':900}

        num = 0

        d2Key=list(d2.keys())
        d1Key=list(d1.keys())

        for i in d2Key:
            if i in temp:
                num+=d2[i]
                temp=temp.replace(i,'',1)

        for i in range(len(temp)):
            num+=d1[temp[i]]
        
        return num
