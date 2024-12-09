#include "list.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/**
* Allocate a Node and initialize its value and next pointer
* @param val  value
* @param next next pointer
* @return pointer to new Node
*/

Node *node_create(int val, Node *next) {
    Node *n = malloc(sizeof(Node));
    n->val = val;
    n->next = next;
    return n;
}

/**
 * Free a Node
 * @param n  Node to free
 */
void node_delete(Node *n) { 
    free(n);
}

/**
 * Recursively delete a linked list of Nodes
 * @param n  head of list of Nodes
*/
void list_delete(Node *head) {
    if (!head) return;
    Node* temp = head->next;
    node_delete(head);
    list_delete(temp);
}

/**
 * Append a node to the head of a linked list of Nodes
 * @param head  head of the linked list of Nodes
 * @param val   value of new Node
 * @return new head of list
 */
Node *list_append_head(Node *head, int val) { 
    Node* temp = node_create(val, head);
    return temp;
}

/**
 * Recursively append a node to the tail of a linked list of Nodes
 * @param head  head of list
 * @param val   value of new Node
 * @return new head of list (for when list is originally empty)
 */
Node *list_append_tail(Node *head, int val) { 
    if (!head){
        Node* temp = node_create(val, NULL);
        return temp;
    } 
    head->next = list_append_tail(head->next, val);
    return head;
}

/**
* Recursively print the Nodes in a linked list in order from
* head to tail 
* @param head   head of list
*/
void list_print(Node *head) {
    if (!head){
        printf("\n");
        return;
    } 
    printf("%d ", head->val);
    list_print(head->next);
}

/**
 * Split a linked list of Nodes into two sublists, left and right
 * @param head  head of original list
 * @param left  Returns the head of the left sublist via a pointer
 * @param right Returns the value of the right sublist via a pointer
 */
void list_split(Node *head, Node **left, Node **right) {
    // Handle case where list has fewer than 2 Nodes (no need to split)
    if (!head || !(head->next)){
        return;
    }
    
    // Process to split list (with 2 or more Nodes)
    Node* fast = head->next->next;
    Node* slow = head;
    while (fast && fast->next){
        fast = fast->next;
        slow = slow->next;
        if (fast->next){
            fast=fast->next;
        }
    }
    *right = slow->next;
    slow->next=NULL;
    *left = head;
}

/**
 * Merge left and right subtrees into a single linked list
 * @param left  head of left subtree
 * @param right head of right subtree
 * @return head of merged linked list
 */
Node *list_merge(Node *left, Node *right) {
    assert(left || right);

    // if left or right is empty, simply return the other
    if (!left) return right;
    if (!right) return left;
    // Get the first element
    Node* dummy = node_create(0,NULL);
    Node* curr = dummy;
    while(left && right){
        if (left->val < right->val){
            curr->next=left;
            left=left->next; 
        } else {
            curr->next=right;
            right=right->next; 
        }
        curr = curr->next;
        curr->next = NULL;
    }
    // Until left or right is empty add smallest head from either to tail of
    // merged list
    if (left) curr->next = left;
    if (right) curr->next = right;

    // Attach remainder of left or right and return

    // Return the result
    Node* head = dummy->next;
    node_delete(dummy);
    return head;
}

/**
 * Use merge sort to sort a linked list in increasing order
 * @param head  head of list to be sorted
 * @return head of sorted list
 */
Node *list_merge_sort(Node *head) {
    // Base case: list is empty or only has 1 node
    // Return the head without sorting
    if (!head || !(head->next)){
        return head;
    }
    // Recursive merge sort
    Node* right = NULL;
    Node* left = NULL;
    list_split(head, &left, &right);
    left = list_merge_sort(left);
    right = list_merge_sort(right);
    return list_merge(left, right);
}