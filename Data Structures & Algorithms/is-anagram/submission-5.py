class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if the lengths are different = False 

        if len(s) != len(t): 
            return False 
        
        # if that passes 

        # dictionaries are equal to each other then True, if not False 
        # HashMap = Key, value 
        
        dict_for_s = {}
        
        dict_for_t = {}

        # racecar 
        # r = 2 , c = 2,a = 2,  e = 1,
        # carrace, 
        # r = 2, c = 2, a = 2, e = 1  

        for letter in s:
            dict_for_s[letter] = dict_for_s.get(letter, 0) + 1
        
        for letter in t: 
            dict_for_t[letter] = dict_for_t.get(letter, 0) + 1 

        if dict_for_s == dict_for_t: 
            return True
        else: 
            return False

        