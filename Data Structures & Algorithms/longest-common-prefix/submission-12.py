class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    # loop of array is the first string
    # check each string in the list afterwards
    # condtions : the current interation is equal to len of the string
    # 2nd condtion : to check if the current value of current string is the same as first string in array
    
        first_string = strs[0]
        for first_string_index in range(len(first_string)):
            for current_string in strs:
                if len(current_string) == first_string_index or current_string[first_string_index]!= first_string[first_string_index]:
                    return first_string[:first_string_index]
        return strs[0]
