class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        vector<int> values;

        // Store values from the linked list in a vector
        while (head) {
            values.push_back(head->val);
            head = head->next;
        }

        if (values.empty()) {
            return nullptr;
        }

        // Reverse the vector
        reverse(values.begin(), values.end());

        // Create new reversed linked list
        ListNode* new_head = new ListNode(values[0]);
        ListNode* current = new_head;
        for (int i = 1; i < values.size(); i++) {
            current->next = new ListNode(values[i]);
            current = current->next;
        }

        return new_head;
    }
};
