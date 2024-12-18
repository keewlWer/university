class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    if not head or not head.next:
        return
    
    # Знаходимо середину списку
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Розділяємо список на дві частини
    second = slow.next
    slow.next = None
    
    # Перевертаємо другу частину
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node
    
    # З’єднуємо обидві частини
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
      
  def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

  # Створимо список [1, 2, 3, 4]
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  
  # Друкуємо початковий список
  print("Initial list:")
  printList(head)
  
  # Викликаємо функцію reorderList
  reorderList(head)
  
  # Друкуємо перевпорядкований список
  print("Reordered list:")
  printList(head)
