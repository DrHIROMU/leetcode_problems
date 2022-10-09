package remove_nth_node_from_end_of_list_19;

public class Solution {
    public static void main(String[] args){

    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode nthNodeFromEnd = head;
        ListNode prevNthNodeFromEnd = null;
        ListNode current = head;
        int stepsFromEnd = 0;

        if(head.next == null && n==1){
            return null;
        }

        while(true){
            current = current.next;

            if(stepsFromEnd < n){
                stepsFromEnd++;
            }

            if(stepsFromEnd == n){
                prevNthNodeFromEnd = nthNodeFromEnd;
                nthNodeFromEnd = nthNodeFromEnd.next;
            }

            if(current.next == null){
                if(nthNodeFromEnd == head){
                    head = head.next;
                }else {
                    prevNthNodeFromEnd.next = nthNodeFromEnd.next;
                }
                break;
            }
        }
        return head;
    }

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
