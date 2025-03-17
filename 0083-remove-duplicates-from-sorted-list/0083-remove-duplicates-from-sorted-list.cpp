class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) return head; // Return head if list is empty

        ListNode* p = head;
        while (p != nullptr && p->next != nullptr) {
            if (p->val == p->next->val) {
                p->next = p->next->next; // Skip the duplicate node
            } else {
                p = p->next; // Move to next node only if no duplicate
            }
        }
        
        return head;
    }
};
