/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL){
        return head;
    }
    struct ListNode* ptr = head;
    struct ListNode* pptr = NULL;
    while (ptr->next != NULL){
        pptr = ptr;
        ptr = ptr->next;
        if (pptr->val == ptr->val){
            pptr->next = ptr->next;
            ptr=pptr;
        }
    }
    return head;
}