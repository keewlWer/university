class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

# head = [1, 1, 2]
head1 = ListNode(1, ListNode(1, ListNode(2)))
result1 = deleteDuplicates(head1)
output1 = []
while result1:
    output1.append(result1.val)
    result1 = result1.next
print(output1)  # [1, 2]

# [1, 1, 2, 3, 3]
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result2 = deleteDuplicates(head2)
output2 = []
while result2:
    output2.append(result2.val)
    result2 = result2.next
print(output2)  # [1, 2, 3]
