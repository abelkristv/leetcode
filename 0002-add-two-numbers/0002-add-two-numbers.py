
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        num1 = 0
        num2 = 0
        i = 0

        while l1 != None:
            num1 += l1.val * 10 ** i
            i += 1
            l1 = l1.next

        i = 0

        while l2 != None:
            num2 += l2.val * 10 ** i
            i += 1
            l2 = l2.next
        
        sum = num1 + num2
        # print(sum)

        listToReturn = ListNode()
        current = listToReturn

        while sum != 0:
            angka = sum % 10
            sum = sum / 10
            # print(sum)
            current.val = angka
            if sum != 0:
                current.next = ListNode()
            current = current.next
            # print(listToReturn)
        
        return listToReturn