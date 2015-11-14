def wordPattern(pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        pattern_list = list(pattern)
        str_list = str.split()
        pattern_token_list=[]
        str_token_list = []
        
        if len(pattern_list) != len(str_list):
            return False
        
        for elem in pattern:
            if elem not in pattern_token_list:
                pattern_token_list.append(elem)
                indices = [i for i, x in enumerate(pattern_list) if x == elem]
                if str_list[indices[0]] in str_token_list:
                    return False
                str_token_list.append(str_list[indices[0]])
                for index in indices:
                    if str_list[index] != str_list[indices[0]]:
                        return False
        
        return True

print wordPattern("abba", "dog cat cat dog")
print wordPattern("abbc", "dog cat cat dog")
print wordPattern("abbc", "dog cat cat fish")