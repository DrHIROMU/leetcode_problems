package medium.add_two_numbers_2;

import medium.ListNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List vals1 = Arrays.asList(new Integer[]{0});
        List vals2 = Arrays.asList(new Integer[]{7,3});
        ListNode list1 = new ListNode(vals1);
        ListNode list2 = new ListNode(vals2);

//        list1.showAllVals();
        Solution solution = new Solution();
        ListNode list = solution.addTwoNumbers(list1, list2);
        list.showAllVals();
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode list = new ListNode();
        ListNode curNode = list;

        int carry = 0;
        ListNode currentNode1 = l1;
        ListNode currentNode2 = l2;
        do{
            int val1 = currentNode1!=null? currentNode1.val:0;
            int val2 = currentNode2!=null? currentNode2.val:0;
            int sum = (val1 + val2) + carry;
            curNode.val=sum % 10 ;

            if(sum >= 10){
                carry = sum/10;
            }else{
                carry = 0;
            }
            if((currentNode1 != null && currentNode1.next != null)
                    || (currentNode2 != null && currentNode2.next != null)
                    || carry >0){
                curNode.next = new ListNode();
                curNode = curNode.next;
            }
            currentNode1 = currentNode1!=null? currentNode1.next:null;
            currentNode2 = currentNode2!=null? currentNode2.next:null;
        }while (currentNode1 != null || currentNode2 != null || carry != 0);


        return list;
    }


}
