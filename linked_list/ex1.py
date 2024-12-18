class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2

    return dummy.next

# Приклади використання
# Створення тестових списків вручну
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

result = merge_two_sorted_lists(list1, list2)
# Виведення результату
output = []
while result:
    output.append(result.val)
    result = result.next
print(output)  # [1, 1, 2, 3, 4, 4]
