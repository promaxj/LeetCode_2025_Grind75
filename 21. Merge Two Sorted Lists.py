from typing import Optional

# 定義單向鏈結串列的節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 建立虛擬節點以簡化邊界條件處理
        dummy = ListNode(-1)
        current = dummy

        # 當兩個串列都還有節點時，進行比較並合併
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # 將 list1 節點連接至合併串列
                list1 = list1.next    # 移動 list1 指標
            else:
                current.next = list2  # 將 list2 節點連接至合併串列
                list2 = list2.next    # 移動 list2 指標
            current = current.next    # 移動合併串列的指標

        # 當其中一個串列遍歷完，直接連接剩下的節點
        if list1:
            current.next = list1
        else:
            current.next = list2

        # 返回虛擬節點後的第一個節點
        return dummy.next

# 輔助函式：將 Python 陣列轉換成鏈結串列
def list_to_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 輔助函式：將鏈結串列轉換回 Python 陣列，方便檢查結果
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# 建立 Solution 類別的實例
solution = Solution()

# 原始的陣列資料
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# 先將陣列轉換成鏈結串列
l1 = list_to_linked_list(list1)
l2 = list_to_linked_list(list2)

# 呼叫 mergeTwoLists 方法並接收返回結果
merged_list = solution.mergeTwoLists(l1, l2)

# 將合併後的鏈結串列轉換成陣列並輸出結果
print("合併後的鏈結串列:", linked_list_to_list(merged_list))
