class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        top_item = count.most_common(1)

        return top_item[0][0]
        