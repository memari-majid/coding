class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle1(head: ListNode) -> bool:
    visited = set()
    while head is not None:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False


def has_cycle2(head: ListNode) -> bool:
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

