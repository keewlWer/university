class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next


# Створимо список [4, 5, 1, 9]
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

node = head.next  

deleteNode(node)

current = head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
