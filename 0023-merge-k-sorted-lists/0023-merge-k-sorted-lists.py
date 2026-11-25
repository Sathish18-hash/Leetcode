# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx, head))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            _, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next