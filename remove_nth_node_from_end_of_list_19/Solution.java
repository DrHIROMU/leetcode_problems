package remove_nth_node_from_end_of_list_19;

public class Solution {
    public static void main(String[] args){

    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode nStepPrev = head;
        ListNode current = head;
        ListNode tail = head.next;
        int prevSteps = 0;

        for(int i=1; i<=n; i++){
            if(prevSteps < n){
                prevSteps++;
            }else{
                nStepPrev = nStepPrev.next;
            }

            if (tail.next == null){

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
