class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1) 
        l2 = len(s2) 
        if l1 > l2: 
            return False 
        freq = [0] * 26 
        for char in s1: 
            freq[ord(char)-97] += 1 
        print(freq) 
        for index, char in enumerate(s2): 
            freq[ord(char)-97] -= 1
            # move sliding window (remove old char)
            if index < l1: 
                if all([x == 0 for x in freq]): 
                    return True 
                continue 
            oldchar = s2[index - l1] 
            freq[ord(oldchar)-97] += 1 
            print(index, freq) 
            if all([x == 0 for x in freq]): 
                return True 
        return False 
    
            
        
