# current一開始指向較小的node
# 每回合都會比較list1與list2 head較小的node, 讓current.next指向它, 該list的head指向下一個node
# 當其中一個list指向None, current指向另一個list的head

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        list1_head = list1.next if list1.val <= list2.val else list1
        list2_head = list2.next if list2.val < list1.val else list2
        result = list1 if list1.val <= list2.val else list2
        current = result

        while list1_head != None or list2_head != None:
            if list1_head == None:
                current.next = list2_head
                break

            if list2_head == None:
                current.next = list1_head
                break

            if list1_head.val <= list2_head.val:
                current.next = list1_head
                list1_head = list1_head.next
            else:
                current.next = list2_head
                list2_head = list2_head.next

            current = current.next        
        return result
    
def create_link_list(list) -> Optional[ListNode]:
    if not list:
        return None
    head = ListNode(list[0])
    current = head
    for val in list[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def main():
    s = Solution()
    list1 = [2,3]
    list2 = [1,4,5]
    result = s.mergeTwoLists(create_link_list(list1), create_link_list(list2))

    current = result
    while current != None:
        print(current.val)
        current = current.next

if __name__ == '__main__':
    main()