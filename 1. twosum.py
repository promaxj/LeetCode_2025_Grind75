class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for key, value in enumerate(nums):
            difference = target - value
            if difference in num_to_index:
                return [num_to_index[difference], key]
            num_to_index[value] = key
        return []
    
# 建立 Solution 類別的實例
solution = Solution()

# 定義數字列表和目標值
nums = [2, 7, 11, 15]
target = 9

# 呼叫 twoSum 方法並接收返回結果
result = solution.twoSum(nums, target)

# 輸出結果
print("兩數的索引是:", result)
