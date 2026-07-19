class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for string in strs:
            values = [0] * 26
            for v in string:
                values[ord(v) - ord("a")] +=1
            group[tuple(values)].append(string)
        return list(group.values())


        