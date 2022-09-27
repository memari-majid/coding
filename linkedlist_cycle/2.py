class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def intersect1(head1, head2):
    while head1:
        while head2:
            if head1 == head2:
                return head1
            head2 = head2.next
        head1 = head1.next


def intersect2(headA, headB):
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

