class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s_count = {}
        for i in range(len(nums)):
            s_count[nums[i]] = s_count.get(nums[i], 0) + 1
        
        return sorted(s_count, key=s_count.get, reverse=True)[:k]