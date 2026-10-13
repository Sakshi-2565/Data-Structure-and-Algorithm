# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None


class Solution:
    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head

        curr = head

        while curr.next is not None:
            front = curr.next

            if curr.data == front.data:
                curr.next = front.next

                if front.next is not None:
                    front.next.prev = curr
            else:
                curr = curr.next

        return head
