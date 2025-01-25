/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

    struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *slow = head, *fast;
    
    while (slow != NULL && slow->next != NULL) {
        if (slow->val == slow->next->val) {
            fast = slow->next;
            slow->next = fast->next;
            free(fast); // Remove duplicate node
        } else {
            slow = slow->next; // Move to the next node
        }
    }
    
    return head;
}


