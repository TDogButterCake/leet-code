# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy head to simplify result list creation
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

def get_first_uncommon_index(s):
    i = 0
    while True:
        if len(s[0]) == i:
            return i
        letter = s[0][i]
        for word in s[1:]:
            if len(word) == i:
                return i
            if word[i] != letter:
                return i
        i += 1

def get_common_prefix(strings):
    return strings[0][:get_first_uncommon_index(strings)]
