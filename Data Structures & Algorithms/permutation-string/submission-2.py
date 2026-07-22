class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1) 
        l2 = len(s2) 
        if l1 > l2: 
            return False 
        freq = {} 
        uniq_chars = 0 
        matches = 0 
        for char in s1: 
            if char not in freq: 
                uniq_chars += 1 
                freq[char] = 1
            else: 
                freq[char] += 1 
        print(freq) 
        for index, char in enumerate(s2): 
            # update new character 
            if char in freq: 
                freq[char] -= 1
                # check for updated matches 
                if freq[char] == 0: 
                    matches += 1 
                elif freq[char] == -1: 
                    matches -= 1 
            print(freq) 
            # move sliding window (remove old char)
            if index < l1-1: 
                continue 
            elif index == l1-1: 
                if matches == uniq_chars: 
                    return True 
                continue 
            oldchar = s2[index - l1] 
            if oldchar in freq: 
                freq[oldchar] += 1 
                # check for updated matches 
                if freq[oldchar] == 0: 
                    matches += 1 
                elif freq[oldchar] == 1: 
                    matches -= 1 
        
            if matches == uniq_chars: 
                return True 
            print(index, matches, freq) 
        return False 
            
        
