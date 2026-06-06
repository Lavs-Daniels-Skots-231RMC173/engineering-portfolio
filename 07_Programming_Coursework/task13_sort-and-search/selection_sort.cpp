/**
Create selection sort function.
Use an array with fixed size
AI tools:
 - nothing is allowed for selectionSort function
 */
#include <iostream>
using namespace std;

// create an array of 4 integers
int arr[4] = {4, 3, 5, 2};

void selectionSort(int arr[], int n) {
    /** Create selection sort using arrays
     * 1. Loop through elements based on array size -1
     *      1.1. Set the minimum value to the current index
     *      1.2. Loop through the array starting from the next index until array size
     *        1.2.1. If the current element is less than the minimum value
     *          1.2.1. then set the minimum value to the current index in inner loop
     *     1.3. Swap the minimum value with the current index
     */
    for (int i = 0; i < n - 1; ++i) {
        // assume element at i is the minimum
        int minIndex = i;
        // find the actual minimum in the rest of the array
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // swap if a smaller element was found
        if (minIndex != i) {
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}


int main(){
    cout << "Selection sort with array" << endl;
    cout << "\tbefore sorting: ";
    for (int i = 0; i < 4; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    selectionSort(arr, 4);
    cout << "\tafter sorting: ";
    for (int i = 0; i < 4; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "--------------------------------" << endl;
    return 0;
}
