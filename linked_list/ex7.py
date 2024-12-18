import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    heap = []
    
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Функція для створення зв'язаного списку з масиву
def createLinkedList(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Функція для друку списку
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Приклад 1
list1 = createLinkedList([1, 4, 5])
list2 = createLinkedList([1, 3, 4])
list3 = createLinkedList([2, 6])

lists = [list1, list2, list3]

merged_head = mergeKLists(lists)
print("Merged list:")
printList(merged_head)

# Приклад 2
lists2 = []
merged_head2 = mergeKLists(lists2)
print("Merged list:")
printList(merged_head2)

# Приклад 3
lists3 = [createLinkedList([])]
merged_head3 = mergeKLists(lists3)
print("Merged list:")
printList(merged_head3)
