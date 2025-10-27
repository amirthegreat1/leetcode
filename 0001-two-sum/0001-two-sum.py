class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indx={}
        for i , n in enumerate(nums):
            indx[n] =  i
        for i , n in enumerate(nums):
            diff = target - n
            if diff in indx and indx[diff]!=i:
                return[indx[diff] , i]   