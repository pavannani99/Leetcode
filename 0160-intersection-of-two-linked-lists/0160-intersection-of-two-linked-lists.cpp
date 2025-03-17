class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return nullptr;
        
        ListNode* temp1 = headA;
        ListNode* temp2 = headB;
        
        while (temp1 != temp2) {
            temp1 = (temp1 == nullptr) ? headB : temp1->next;
            temp2 = (temp2 == nullptr) ? headA : temp2->next;
        }
        
        return temp1; // Will be nullptr if no intersection, or the intersection node
    }
};
