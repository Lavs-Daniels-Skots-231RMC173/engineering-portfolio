/**
Create linear search function.
Use a arrays and linked lists
AI tools:
 - nothing is allowed for linearSearch function, this functions should use the arrays.
 - copilot is allowed for linearSearch2 function, this function should use the linked list.
 */
#include <iostream>
using namespace std;

/* This is one list element, it contains data and pointer to the next element. */
struct Node {
    int data;
    Node* next;
};


void printList(Node* node);
void append(Node** head_ref, int new_data);

// create an array of 4 integers
int arr[4] = {4, 3, 5, 2};

int linearSearch(int arr[], int n, int x) {
    /**Create linear search
     * 1. Loop through the array
     *  1.1. If the current element is equal to the value
     *     1.1.1. Return the index
     * 2. Return -1 if the value is not found
     */
    for (int i = 0; i < n; ++i) {
        if (arr[i] == x) {
          
  return i;
        }
    }
    return -1;
}

int* linearSearch2(Node* head, int x, int result[2]) {
    result[0] = -1;
    result[1] = -1;
    // create a counter and a pointer to the beginning of the linked list
    int position = 0;
    Node* current = head;
    /** Create linear search using linked lists
     * Output the position and value of the element
     * Position must be counted to measure how many elements were traversed
     * 1. Create a counter and a pointer to the beginning of the linked list
     * 2. Loop through the list until current element is NULL
     *   2.1. If the current element is equal to the value
     *     2.1.1. Save position in result array
     *     2.1.2. Save value in result array
     *     2.1.3. Return the result array
     *  2.2. Increment counter by 1
     * 2.3. Move to the next element
     * 3. Return -1, -1 if the value is not found
     */
    while (current != NULL) {
        if (current->data == x) {
            result[0] = position;
            result[1] = current->data;
            return result;
        }
        position++;
        current = current->next;
    }
    return  result;
}



int main(){
    for (int i = 0; i < 4; i++) {
        cout << arr[i] << " ";
    }


    cout << "Linear search with array" << endl;
    cout << "\tsearching for 5: ";
    cout << linearSearch(arr, 4, 5) << endl;
    cout << "\tsearching for 1: ";
    cout << linearSearch(arr, 4, 1) << endl;
    cout << "--------------------------------" << endl;
    
    cout << "Linear search with linked list" << endl;
    Node* head = NULL;
    append(&head, 4);
    append(&head, 3);
    append(&head, 5);
    append(&head, 2);

    int result[2];

    cout << "\tsearching for 5: " << endl;
    linearSearch2(head, 5, result); 
    cout << "\t\tPostion: " << result[0] << endl;
    cout << "\t\tValue: " << result[1] << endl;
    cout << "\tsearching for 1: " << endl;
    linearSearch2(head, 1, result); 
    cout << "\t\tPostion: " << result[0] << endl;
    cout << "\t\tValue: " << result[1] << endl;
    return 0;
}



void printList(Node* node) {
    /* until there is no nex element output the data and move one element further*/
    while (node != NULL) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

void append(Node** head_ref, int new_data) {
    /* The two * by Node means that we are creating a pointer to a pointer, thus giving the address for
     the pointer and allowing it to edited, not only the value it points at. */
    /* Create a new empty node and a pointer to current beginning of the linked list*/
    Node* new_node = new Node();
    Node* last = *head_ref;
    /* Add the data in the new node*/
    new_node->data = new_data;
    new_node->next = NULL;
    /* If the linked list is empty, then make the new node as head. */
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }
    /* Traverse the list and find the last node. */
    while (last->next != NULL) {
        last = last->next;
    }
    last->next = new_node; /* Link the last node to the new node. */
    /* This functions does not require a return statemnt as it's defined as void (nothing).*/
}
