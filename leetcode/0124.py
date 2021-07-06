# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq

class Node :
    def __init(self, data, next=None):
        self.data = data
        self.next = next
    def __it__(self, other) :
        return self.data < other.data
# def printList(node) :
#     while node :
#         print(node.data, end = ' -> ')
#         node = node.next
#     print("None")
class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    def mergeKLists(lists) :
        pq = [x for x in lists]
        hq.heapify(lists)

        head = None
        last = None
        while pq :
            min = hq.heappop(pq)

            if head in None :
                head = min
                last = min
            else
                last.next = min
                last = min
            if min.next :
                hq.heappush(pq, min.next)
        return head
