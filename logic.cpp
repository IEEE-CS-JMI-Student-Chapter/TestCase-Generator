#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the insertionSort1 function below.
void insertionSort1(int n, vector<int> arr) 
{
    for(int i = 0; i < n; i++)
    {
        int j = i-1;
        int key = arr[i];
        bool check = false;
        while(j>=0 && arr[j] > key)
        {
            arr[j+1] = arr[j];
            j--;
            for(int i = 0; i < n; i++)
            {
                cout<<arr[i]<<" ";
            }
            cout<<endl;
        }
        arr[j+1] = key;
    }  
    for(int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    } 
}

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item  = 0;
        cin>>arr_item;

        arr[i] = arr_item;
    }

    insertionSort1(n, arr);

    return 0;
}

