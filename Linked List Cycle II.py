############ BRUTE FORCE SOLUTION #####################


class Solution:
    def detectCycle(self, head):
        my_set = set()
        temp = head

        while temp is not None:
            if temp in my_set:
                return temp
            else:
                my_set.add(temp)
                temp = temp.next

        return None


# Time Complexity = O(N)
# Space Complexity = O(N)

#############   OPTIMAL SOLUTION   #######################


def detectCycle(self, head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow
    return None


# Time Complexity = O(N)
# Space Complexity = O(1)
