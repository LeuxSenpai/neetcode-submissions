class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): #checking if string len are equal
            return False
        count={} #create a dic
        for char in s: #looping through each strong and add each letter
            count[char]=count.get(char,0)+1
        for char in t: 
            if char not in count: #dic already has values if there is a new value 
                return False
            count[char]-=1 #if values match we subtract it from dic
            if count[char]==0: #all values are equal means empty dic
                del count[char] #so we delte it
        return len(count)==0             