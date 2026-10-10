############ BRUTE FORCE SOLUTION #####################


class Solution:
    def hasCycle(self, head):
        my_set = set()
        temp = head

        while temp is not None:
            if temp in my_set:
                return True
            else:
                my_set.add(temp)
                temp = temp.next

        return False


# Time Complexity = O(N)
# Space Complexity = O(N)

#############   OPTIMAL SOLUTION   #######################


class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Time Complexity = O(N)
# Space Complexity = O(1)
