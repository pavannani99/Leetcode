class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int> hey;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry) {
            int sum = carry;
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            hey.push_back(sum % 10);
            carry = sum / 10;
        }

        // Convert vector to list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        for (int value : hey) {
            current->next = new ListNode(value);
            current = current->next;
        }

        return dummy->next;
    }
};
