# Given the head of a linked list, 
# rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        if head.next == None:
            return head

        prev = None
        cur = head
        tail = None
        lenOfList = self.getLenOfList(head)
        k = k % lenOfList

        for i in range(k):
            while(True):
                if cur.next:
                    prev = cur
                    cur = cur.next
                else:
                    cur.next = head
                    head = cur
                    prev.next = None
                    prev = None
                    break

        self.printAllElements(head)
        return head

    def getLenOfList(self, head):  
        cur = head
        length = 0      
        while(cur != None):
            cur = cur.next
            length += 1
        return length
    
    def getListHead(self, arr):
        head = None
        next = None
        for i in range(len(arr)-1, -1, -1):       
            node = ListNode(arr[i], next)  
            next = node
            if i == 0:
                head = node
        return head
    
    def printAllElements(self, head):
        cur = head
        while(cur != None):            
            print(cur.val)
            cur = cur.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

s = Solution()
head = s.getListHead([2,1,3])
s.rotateRight(head,200000000)