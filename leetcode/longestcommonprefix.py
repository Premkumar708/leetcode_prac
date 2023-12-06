class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        # declare a common_prefix to return the value
        common_prefix=""
        # declare char to track each character
        char = ""
        # loop through 1st index
        for i in range(len(s[0])):
            char = s[0][i]
            # compare each index
            for j in range(len(s)):
                #if the string is out of bounce,return prefix
                if len(s[j]) <= i:
                    return common_prefix
                else:
                    # if the char does not match with letter then return prefix
                    if char != s[j][i]:
                        return common_prefix    
                # if not add the char to common_prefix 
            common_prefix += char
        return common_prefix 