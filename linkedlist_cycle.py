class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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


first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

first.next = second
second.next = third
third.next = fourth
#fourth.next = first

print(has_cycle1(first))