#include <iostream>  
using namespace std;
 
void selection(int arr[], int n)  
{  
    int i, j, small;  
      
    for (i = 0; i < n-1; i++)    // One by one move boundary of unsorted subarray  
    {  
        small = i; //minimum element in unsorted array  
          
        for (j = i+1; j < n; j++)  
        if (arr[j] < arr[small])  
            small = j;  
// Swap the minimum element with the first element  
    int temp = arr[small];  
    arr[small] = arr[i];  
    arr[i] = temp;  
    }  
}  
  
void printArr(int a[], int n) /* function to print the array */  
{  
    int i;  
    for (i = 0; i < n; i++)  
        std::cout<<a[i]<<" ";  
}  
  
int main()  
{  
    int n;
    std::cout<<"Enter size of array: ";
    cin>>n;
    int a[n];
    std::cout<<"Enter the array: "<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }  
    std::cout<<"Before sorting array elements are : "<<endl;  
    printArr(a, n);  
    selection(a, n);  
    std::cout<<"\n"<<"After sorting array elements are: "<<endl;    
    printArr(a, n);  
    return 0;  
}    