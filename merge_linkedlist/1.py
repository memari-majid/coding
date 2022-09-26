class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def iterative(l1, l2):
    head = curr = ListNode(0)
    while l1 and l2:
        if l1.value < l2.value:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    # attach the non-null list
    curr.next = l1 or l2
    return head.next


if __name__ == '__main__':
    # LinkedList 1 Node
    L1_N1 = ListNode()
    L1_N1.value = 1
    L1_N2 = ListNode()
    L1_N2.value = 2
    L1_N3 = ListNode()
    L1_N3.value = 3
    # Next
    L1_N1.next = L1_N2
    L1_N2.next = L1_N3

    # LinkedList 2 Node
    L2_N1 = ListNode()
    L2_N1.value = 4
    L2_N2 = ListNode()
    L2_N2.value = 5
    L2_N3 = ListNode()
    L2_N3.value = 6
    # Next
    L2_N1.next = L2_N2
    L2_N2.next = L2_N3

    iterative(L1_N1, L2_N1)
