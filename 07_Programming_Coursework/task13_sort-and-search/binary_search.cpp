/**
Create binary search function.
Use arrays.
AI tools:
 - copilot is allowed for binary search function
 */
#include <iostream>
using namespace std;

// create an array of 4 integers
int arr[7] = {1,4,5,6,10,12,14};

// create a function that will return the index of the element we are looking for
int binarySearch(int arr[], int size, int value) {
    int left = 0; // set the left index to 0
    int right = size - 1; // set the right index to the last element of the array
    /** Create binary search
     * 1. Set the left index to 0 and the right index to the size of the array - 1
     * 2. While the left index is less than or equal to the right index
     *   2.1. Calculate the middle index
     *   2.2. If the middle element is the one we are looking for
     *     2.2.1. Return the index of the element
     *   2.3. If the middle element is smaller than the one we are looking for
     *     2.3.1. Set the left index to the middle index + 1
     *   2.4. If the middle element is greater than the one we are looking for
     *     2.4.1. Set the right index to the middle index - 1
     * 3. If the element is not in the array, return -1
     */
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == value) {
            return mid;
        } else if (arr[mid] < value) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // if the element is not in the array, return -1
    
}

int main(){
    for (int i = 0; i < 7; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    /** Calculate array size
     *  1. Create a variable to store the size of the array
     *  2. Calculate the size of the array
     *  To calculate the size of array you can use the following formula:
     *  size = size of array / size of first element of array
     */
    int size = sizeof(arr) / sizeof(arr[0]); // calculate the size of the array


    int value = 10; // set the value we are looking for
    cout << "Searching for " << value << endl;	
    int result = binarySearch(arr, size, value); // call the binarySearch function
    if (result == -1) // if the element is not in the array
        cout << "Element not found" << endl;
    else // if the element is in the array
        cout << "Element found at index " << result << endl;
    return 0;
}
