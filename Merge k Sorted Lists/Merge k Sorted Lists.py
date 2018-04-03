from datastructure import ListNode

class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return
        arrays = []
        for _ in lists:
            if not _:
                arrays += ListNode.toArray(_)
        if len(arrays) == 0:
            return
        arrays.sort()
        return ListNode.toList(arrays)
