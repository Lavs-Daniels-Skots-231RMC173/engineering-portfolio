
#include <iostream>
using namespace std;

/* This is one list element, it contains data and pointer to the next element. */
struct Node {
    int data;
    Node* next;
};

void append(Node** head_ref, int new_data);

void printList(Node* node);

int countNodes(Node* head);

void bubbleSort(Node* head);

void bubbleSort2(Node* head);

void bubbleSort(Node* head) {
    /* Check if there are any elements in the linked list - if not end sorting */
    if (head == NULL) {
        return;
    }
   /* Count the number of nodes in list */
   int n = countNodes(head);

   /* Do n-1 passes */
   for (int i = 0; i < n - 1; ++i) {
       Node* current = head;
       /* Traverse the unsorted part and bubble largest element to end */
       for (int j = 0; j < n - i - 1; ++j) {
           if (current->data > current->next->data) {
               // swap data
               int temp = current->data;
               current->data = current->next->data;
               current->next->data = temp;
           }
           current = current->next;
       }
   }
}



void bubbleSort2(Node* head){
    /** This is a challange task - if you want to get more points for this task.
     *  Implement bubble sort algorithm for linked list.
     *  This time you don't know how many elements are in the list - use while loops to find if it's the end of the list.
     */

    /* Check if there are any elements in the linked list - if not end sorting */
    if (head == NULL) {
        return;
    }

    bool swapped;
    Node* end = NULL;
    /* Loop until only one element remains unsorted */
    do {
        swapped = false;
        Node* current = head;
        /* Traverse until last sorted node (end) */
        while (current->next != end) {
            if (current->data > current->next->data) {
                // swap data
                int temp = current->data;
                current->data = current->next->data;
                current->next->data = temp;
                swapped = true;
            }
            current = current->next;
        }
        /* Move end pointer one node backward */
        end = current;
    } while (swapped);
}

int countNodes(Node* head) {
    /* Create a counter and a pointer to the beginning of the linked list */
    int count = 0;
    Node* current = head;
    /* Traverse the list and count the elements */
    while (current != NULL) {
        count++; /* increment counter by 1 */
        current = current->next;
    }
    return count;
}

int main(){
    Node* head1 = NULL;
    Node* head2 = NULL;
    /* Append elements to the linked list */
    append(&head1, 4);
    append(&head1, 3);
    append(&head1, 5);
    append(&head1, 2);
    append(&head2, 4);
    append(&head2, 3);
    append(&head2, 5);
    append(&head2, 2);
    cout << "Bubble sort with linked list (known element count)" << endl;
    cout << "\tbefore sorting: ";
    printList(head1);
    cout << "\tafter sorting: ";
    bubbleSort(head1);
    printList(head1);
    cout << "--------------------------------" << endl;
    cout << "Bubble sort with linked list (unknown element count)" << endl;
    cout << "\tbefore sorting: ";
    printList(head2);
    cout << "\tafter sorting: ";
    bubbleSort(head2);
    printList(head2);
    cout << "--------------------------------" << endl;
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
    /* The two * by Node means that we are creating a pointer to a pointer, thus giving the address for the pointer and allowing it to edited, not only the value it points at. */
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
