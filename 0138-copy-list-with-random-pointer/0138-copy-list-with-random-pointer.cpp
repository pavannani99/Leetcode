/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        while(!head) return nullptr;
         Node* curr = head;
        while (curr) {
            Node* copy = new Node(curr->val);
            copy->next = curr->next;
            curr->next = copy;
            curr = copy->next;
        }
curr = head;
        while (curr) {
            if (curr->random) {
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next;
        }
        
        // Step 3: Separate the copied list from the original list
        curr = head;
        Node* dummy = new Node(0);
        Node* copy = dummy;
        while (curr) {
            copy->next = curr->next;
            curr->next = curr->next->next;
            copy = copy->next;
            curr = curr->next;
        }
        
        return dummy->next;
        
        
    }
};