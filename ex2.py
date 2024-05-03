class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs_main_recursion(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    next_node = head.next

    head.next = swap_pairs_main_recursion(next_node.next)
    next_node.next = head
    return next_node


def swap_pairs_tail_recursion(head: ListNode, prev: ListNode = None) -> ListNode:
    if not head or not head.next:
        return head

    next_node = head.next

    head.next = swap_pairs_tail_recursion(next_node.next, head)
    next_node.next = head

    if prev is None:
        return next_node

    prev.next = next_node

    return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
new_head_main = swap_pairs_main_recursion(head)
new_head_tail = swap_pairs_tail_recursion(head)