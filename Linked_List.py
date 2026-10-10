class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Singly_Linked_list:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("Singly_Linked_list is empty")

        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()


sll = Singly_Linked_list()
sll.append(21)
sll.append(11)
sll.append(21)
sll.append(51)
sll.append(71)
sll.traverse()
