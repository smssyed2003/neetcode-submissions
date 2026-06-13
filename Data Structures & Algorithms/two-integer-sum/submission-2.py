class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
                    break
            if index:
                break
        return index