class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleNumber(head: ListNode) -> ListNode:
    num = 0
    place = 1
    current = head
    while current:
        num = num + current.val * place
        place *= 10
        current = current.next
    
    num *= 2
    
    dummy_head = ListNode(0)
    current = dummy_head
    if num == 0:
        return ListNode(0)
    
    while num > 0:
        current.next = ListNode(num % 10)
        current = current.next
        num //= 10
    
    return dummy_head.next

# Функція для друку списку
def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Приклад 1
head = ListNode(1)
head.next = ListNode(8)
head.next.next = ListNode(9)

print("Initial list:")
printList(head)

doubled_head = doubleNumber(head)
print("Doubled list:")
printList(doubled_head)

# Приклад 2
head2 = ListNode(9)
head2.next = ListNode(9)
head2.next.next = ListNode(9)

print("Initial list:")
printList(head2)

doubled_head2 = doubleNumber(head2)
print("Doubled list:")
printList(doubled_head2)
