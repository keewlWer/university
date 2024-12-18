class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next            
        fast = fast.next.next       
        
        if slow == fast:
            return True             
    
    return False                    

# Приклади використання:
# Приклад 1: head = [3, 2, 0, -4], pos = 1
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  

print(hasCycle(node1))  # Output: True

# Приклад 2: head = [1, 2], pos = 0
node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2
node2.next = node1  

print(hasCycle(node1))  # Output: True

# Приклад 3: head = [1], pos = -1
node1 = ListNode(1)

print(hasCycle(node1))  # Output: False
