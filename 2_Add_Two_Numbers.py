# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        HEAD = ListNode()
        current = HEAD
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            current.next = ListNode(val=total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return HEAD.next


def num_to_node(num):
    nodelist = ListNode()
    node = nodelist

    while num != 0:
        node.val = num % 10
        num //= 10
        if num:
            node.next = ListNode()
            node = node.next
        else:
            node.next = None

    return nodelist


def print_node(node):
    print("[", end="")
    while node:
        print(node.val, end="")
        node = node.next
    print("]")


def test(n1, n2):
    l1 = num_to_node(n1)
    l2 = num_to_node(n2)

    print_node(l1)
    print_node(l2)

    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    print_node(res)


if __name__ == "__main__":
    import sys

    test(int(sys.argv[1]), int(sys.argv[2]))
