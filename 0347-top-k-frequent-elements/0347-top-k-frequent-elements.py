class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_count={}
        numset = list(set(nums))
        for i , n in enumerate (numset):
            num_count[n] = nums.count(n)
        numset.sort(key=lambda x: num_count[x], reverse=True)
        
        return [numset[i] for i in range(k)]
