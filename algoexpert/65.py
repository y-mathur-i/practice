from turtle import left, right


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head: Node) -> Node:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
    




head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

res = reverse_list(head)
while res:
    print(res.val)
    res = res.next
