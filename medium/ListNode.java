package medium;

import java.util.List;

public class ListNode {
    public int val;
    public ListNode next;

    public ListNode() {
    }

    public void setVal(int val){
        this.val = val;
    }
    public int getVal(){
        return val;
    }

    public ListNode getNext(){
        return this.next;
    }
    public ListNode(List<Integer> vals) {
        ListNode currentNode = this;
        for (int i = 0; i < vals.size(); i++) {
            Integer val = vals.get(i);
            currentNode.val = val;
            if (i != vals.size() - 1) {
                currentNode.next = new ListNode();
                currentNode = currentNode.next;
            }
        }
    }

    public void showAllVals() {
        ListNode currentNode = this;
        do {
            System.out.println(currentNode.val);
            currentNode = currentNode.next;
        } while (currentNode != null);
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
