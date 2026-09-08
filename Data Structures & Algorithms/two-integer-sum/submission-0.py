class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given:
        #      nums = [x, y, z]
        #      target = n
        # task : return nums[i] + nums[j] == target, i != j 
        # return the smaller index first
        
        # hashmap = {}

        # for i in nums:
        #   let difference = target - nums[i]
        #   if diffrence in hashmap:
        #         return [i, diffrence]
        #   else:
        #         hashmap.add(i)
        # return 
        
        hashmap = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in hashmap:
                return [hashmap[difference], i]

            hashmap[num] = i