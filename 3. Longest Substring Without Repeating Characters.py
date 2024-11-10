class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            # right - left + 1 目前的不重複字串數
            # max_length 是記錄到最大的不重複字串數
            max_length = max(max_length, right - left + 1)
        return max_length
    
# 建立 Solution 類別的實例
solution = Solution()

s ="pwwkew"

# 呼叫 twoSum 方法並接收返回結果
result = solution.lengthOfLongestSubstring(s)

# 輸出結果
print("最長的不重複字元是: ", result)