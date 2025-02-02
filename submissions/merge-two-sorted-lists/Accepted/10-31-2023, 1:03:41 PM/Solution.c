// https://leetcode.com/problems/merge-two-sorted-lists

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){

    struct ListNode dummyHead;
    dummyHead.next = NULL;
    struct ListNode* tmp = &dummyHead;
    
    while (list1 != NULL && list2 != NULL){

        if(list1->val <= list2->val){
            tmp->next = list1;
            list1 = list1->next;
        } else{
            tmp->next = list2;
            list2 = list2->next;
        }

        tmp = tmp->next;

    }

    while (list1 != NULL) {
        tmp->next = list1;
        tmp = tmp->next;
        list1 = list1->next;
    }

    while (list2 != NULL){
        tmp->next = list2;
        tmp = tmp->next;
        list2 = list2->next;
    }
   
    return dummyHead.next;

}